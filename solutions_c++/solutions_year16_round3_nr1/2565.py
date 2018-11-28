#include<iostream>
#include<cstdio>
#include<set>
#include<cstring>
#include<algorithm>
#include<queue>
using namespace std;
#define INF 0x3f3f3f3f
typedef unsigned long long LLu;
typedef long long LL;
const int maxn=2*1e5+100;
#define lson l,mid,rt<<1
#define rson mid+1,r,rt<<1|1
const int MOD = 1e9+7;
int A[30];
int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("1.out","w",stdout);
	int t,case1=0;
	scanf("%d",&t);
	while(t--){
		priority_queue<pair<int,int> >q;
		printf("Case #%d:",++case1);
		int i;
		int n;
		scanf("%d",&n);
		int sum=0;
		for(i=0;i<n;i++){
			scanf("%d",&A[i]);
			sum+=A[i];
			q.push(make_pair(A[i],i));
		}
		while(!q.empty()){
			pair<int,int>a=q.top();
			q.pop();
			if(sum&1){
				printf(" %c",a.second+'A');
				sum--;
				if(a.first!=1)
				q.push(make_pair(a.first-1,a.second));
				continue;
			}
			if(!q.empty()){
				pair<int,int>b=q.top();
				q.pop();
				if(a.first-b.first>=2){
					printf(" %c%c",a.second+'A',a.second+'A');
					if(a.first>2)
					q.push(make_pair(a.first-2,a.second));
					sum-=2;
					q.push(make_pair(b.first,b.second));
				}
				else{
					printf(" %c%c",a.second+'A',b.second+'A');
					if(a.first>1){
						q.push(make_pair(a.first-1,a.second));
						}
					if(b.first>1){
						q.push(make_pair(b.first-1,b.second));
					}
					sum-=2;
				}
			}
			else{
				printf(" %c%c",a.second+'A',a.second+'A');
				if(a.first>2){
					q.push(make_pair(a.first-2,a.second));
				}
				sum-=2;
			}
		}
		puts("");
	}
	return 0;
}
