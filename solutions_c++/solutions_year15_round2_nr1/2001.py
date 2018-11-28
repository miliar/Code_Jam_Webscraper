/*input

*/
#include <bits/stdc++.h>
#define X first
#define Y second
#define ll long long
#define d1(x) cout<<#x<<" "<<x<<endl;
#define d2(x,y) cout<<#x<<" "<<x<<" "<<#y<<" "<<y<<endl;
#define d3(x,y,z) cout<<#x<<" "<<x<<" "<<#y<<" "<<y<<" "<<#z<<" "<<z<<endl;
using namespace std;
int visited[1000007];
int d[1000007];
int nn;
void bfs(vector<vector<int> > &v,int node){
    int cur;
    queue<int> q;
    q.push(node);
    d[node]=0;
    visited[node]=1;
    while(!q.empty())
    {   
        cur=q.front();
        q.pop();
        //d3(cur,d[cur],nn);
        if(cur==nn)return;
            for (int i = 0; i < v[cur].size(); i++){
                //d1(v[cur][i]);
                if(!visited[v[cur][i]]){
                    visited[v[cur][i]]=1;
                    //d1(d[nn]);
                    d[v[cur][i]]=d[cur]+1;
                    q.push(v[cur][i]);
                }
            }
    }
}
int reverse(int a){
    int b=0;
    while(a){
        b*=10;
        b+=(a%10);
        a/=10;
    }
    return b;
}
void presolve(){
    nn=1000001;
    memset(visited,0,sizeof(visited));
    memset(d,0,sizeof(d));
    vector<vector<int> > v(nn+1);
    for (int i = 1; i < nn; i++){
        v[i].push_back(i+1);
        v[i].push_back(reverse(i));
    }
    bfs(v,1);
}
void solve(){
    int n;
    cin>>n;
    cout<<d[n]+1;
}
int main(){
    freopen("C:/Users/Enjoy/Desktop/input.txt","r",stdin);
    freopen("C:/Users/Enjoy/Desktop/output.txt","w",stdout);
    int t;cin>>t;
    int i=1;
    presolve();
    while(t--){
        cout<<"Case #"<<(i++)<<": ";
        solve();
        cout<<endl;
    }
}