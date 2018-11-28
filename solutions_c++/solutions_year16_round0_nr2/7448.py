#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define inf 0x7fffffff
#define SCD(t) scanf("%d",&t)
#define SCLD(t) scanf("%ld",&t)
#define SCLLD(t) scanf("%lld",&t)
#define SCC(t) scanf("%c",&t)
#define SCS(t) scanf("%s",t)
#define SCF(t) scanf("%f",&t)
#define SCLF(t) scanf("%lf",&t)
#define pr pair<int,int>
#define mp(a,b) make_pair(a,b)
#define pb push_back
#define fr first
#define sc second
#define mset(arr,val) memset(arr,val,sizeof(arr));

const int MAX = 1000005;
const int MOD = 1e9+7;
int main(){
	// freopen("B-large.in","r",stdin);
	// freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int i = 1;i<=t;i++){
		string s;
		cin>>s;
		string s2 = "";
		for(int j=0;j<s.length();j++){
			if(j > 0 && s[j] == s[j-1]) continue;
			else{
				s2 = s2 + s[j];
			}
		}
		int sz = s2.length();
		if(s2[sz-1] == '+') sz--;
		cout<<"Case #"<<i<<": "<<sz<<endl;
	}
}