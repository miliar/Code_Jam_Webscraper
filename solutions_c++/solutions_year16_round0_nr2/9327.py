/* sourabh1024  */
#include<bits/stdc++.h>

#define si(n)		(scanf("%d",&n))
#define pi(n)		(printf("%d",n))
#define sl(n)		(scanf("%I64d",&n))
#define pl(n)		(printf("%I64d",n))

#define lli long long int
#define ii pair<int,int>
#define vii pair< ii ,int>
#define pb(a) push_back(a)
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large-out.txt","w",stdout);
	ios::sync_with_stdio(false);
	int t,ca=0;
	cin>>t;
	while(t--) {
		ca++;
		string str;
		cin>>str;
		str+='+';
		int len = str.length();
		lli ans=0;
		for(int i=0;i<len;i++) {
			if(i<len-1 && str[i+1]!=str[i]) ans++;
		}
		cout<<"Case #"<<ca<<": "<<ans<<endl;
	}
	return 0;
}

