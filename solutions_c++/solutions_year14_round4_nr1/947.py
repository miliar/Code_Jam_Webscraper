#include<bits/stdc++.h>
#define sc(n) scanf("%d",&n)
#define pn(n) printf("%d\n",n)
#define slc(n) scanf("%lld",&n)
#define pln(n) printf("%lld\n",n)
#define ps(n) printf("%d ",n) //
using namespace std;
int S[10010];
int n,x;
int fun()
{
	sort(S,S+n);
	int ans=n;
	int l=0;
	for(int j=n-1;(j>0)&&(j>l);j--){
		if(S[j]+S[l]<=x){
			ans--;
			l++;
		}
	}
	return ans;
}
int main()
{
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int t,i;
	cin>>t;
	int test=1;
	while(t--){
		cin>>n>>x;
		for(i=0;i<n;i++){
			cin>>S[i];
		}
		cout<<"Case #"<<(test++)<<": "<<fun()<<endl;
	}
	
	return 0;
}
