#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#define ll long long
using namespace std;
const int N= 3e5+10;
vector<int> head[N];
struct Edge{
    int v;
    int weight;
}e[N<<1];
struct Node{
    int dis;
    int weight;
    int u;
    bool operator < (Node &a) {
        if(dis == a.dis) return weight < a.weight;
        else return dis < a.dis;
    }

}node[100];
int n,m,cnt=0,ustart,via[N],wvalue[N];

void addEdge(int u,int v,int w){
    e[cnt] = Edge{v,w};
    head[u].push_back(cnt++);
}
int main(){
	freopen("in.txt","r",stdin);
	memset(via,0,sizeof(via));
	memset(wvalue,0,sizeof(wvalue));
    cin >> n >> m;
    for(int i=1,a,b,w;i<=m;i++){
        scanf("%d%d%d",&a,&b,&w);
        addEdge(a,b,w);
        addEdge(b,a,w);
    }
    cin >> ustart;
    sort(node,node+100);
    set<Node> s;
    //s.insert(Node(0,0,ustart));


    queue<int> q,qnext;
    q.push(ustart);
    via[ustart] =2;
    while(q.size() || qnext.size()){
        if(q.size()== 0){
            while(qnext.size()){
                via[qnext.front()] = 2;
                q.push(qnext.front());
                qnext.pop();
            }
        }
        int x=q.front();
        q.pop();
        for(int i=0;i<head[x].size();i++){
            Edge *p = &e[head[x][i]];
            if(via[p->v] == 0) {
                qnext.push(p->v);
                wvalue[p->v] = p->weight;
                via[p->v] = 1 ;
            }else if(via[p->v] == 1){
                wvalue[p->v] = min(p->weight,wvalue[p->v]);
            }
        }
    }
    ll ans=0;
    for(int i=1;i<=n;i++) {
        cout << wvalue[i] << endl;
    }
    cout << ans << endl;
	return 0;
}
