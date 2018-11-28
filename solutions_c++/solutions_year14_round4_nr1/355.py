#include<bits/stdc++.h>
#define f first
#define s second
using namespace std;
typedef pair<int,int>par;
int main(){
	int T,t=0;
	scanf("%d",&T);
	while(T--){t++;
		int n,x;
		scanf("%d%d",&n,&x);
		multiset<int>st;
		for(int i=0;i<n;i++){
			int k;
			scanf("%d",&k);
			st.insert(k);
			}
		int ans=0;
		while(!st.empty()){
			multiset<int>::iterator it=st.end();
			--it;
			int k=*it;
			st.erase(it);
			it=st.upper_bound(x-k);
			if(it!=st.begin()){
				st.erase(--it);
				}
			ans++;
			}
		printf("Case #%d: %d\n",t,ans);
		}
    return 0;
    }
