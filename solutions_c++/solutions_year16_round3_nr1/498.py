/*****************************************************/
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
#define   sigma_size    26
#define   lson          l,m,v<<1
#define   rson          m+1,r,v<<1|1
#define   LL            long long
#define   ull           unsigned long long
#define   mem(x,v)      memset(x,v,sizeof(x))
#define   lowbit(x)     (x&-x)
#define   mk            make_pair

const int    INF   = 0x3f3f3f3f;
const LL     INFF  = 1e18;
const double pi    = 3.141592653589793;
const double inf   = 1e18;
const double eps   = 1e-9;
const LL     mod   = 1e9+7;
const int    maxmat= 10;

inline int RI(){
    int ret=0;
    char tmp;
    while(!isdigit(tmp=getchar()));
    do{
        ret=(ret<<3)+(ret<<1)+tmp-'0';
    }
    while(isdigit(tmp=getchar()));
    return ret;
}
/*****************************************************/

struct Node{
	int N,k;
	bool operator <(const Node &a)const{
		return k<a.k;
	}
}node[28];
priority_queue<Node>q;
int main(int argc, char const *argv[])
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for (int kase=1;kase<=T;kase++){
		int N,num=0;
		cin>>N;
		for (int i=0;i<N;i++){
			cin>>node[i].k;
			num+=node[i].k;
			node[i].N=i;
			q.push(node[i]);
		}
		printf("Case #%d:",kase);
		while (!q.empty()){
			Node top=q.top(); q.pop();
			top.k--;
			num--;
			printf(" %c",top.N+'A');
			if (top.k) q.push(top);
			if (num>0&&num!=2){
				top=q.top(); q.pop();
				top.k--,num--;
				printf("%c",top.N+'A');
				if (top.k) q.push(top);
			}
		}
		cout<<endl;
	}
	return 0;
}