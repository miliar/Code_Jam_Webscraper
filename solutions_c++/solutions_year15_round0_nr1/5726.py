#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<(n);i++)
#define MP make_pair
#define PB push_back
typedef long long ll;
int main(){
	int t,s[1000],sm;
	string tmp;
	scanf("%d",&t);
	for(int times=0;times<t;times++){
		scanf("%d",&sm);
		cin>>tmp;
		rep(i,tmp.size()){
			s[i]=tmp[i]-'0';
		}
		int sum=s[0],ans=0;
		for(int i=1;i<=sm;i++){
			if(sum<i){
				ans+=i-sum;
				sum+=i-sum;
			}
			sum+=s[i];
		}
		printf("Case #%d: %d\n",times+1,ans);
	}
}
