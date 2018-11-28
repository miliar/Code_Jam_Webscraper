// Coder: Piyush Kidambi

#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<char> vc;

#define pb push_back
#define mp make_pair
#define I vector<int>::iterator
#define ss(a) scanf("%s",a)
#define si(a) scanf("%d",&a)
#define sll(a) cin>>a
#define pi(a) printf("%d ",a)
#define pll(a) cout<<a
#define ps(a) printf("%s ",a)
#define For(i,n) for(i=0;i<n;i++)
#define FOR(i,n) for(i=n-1;i>=0;i--)
#define nl printf("\n")
#define all(a)  a.begin(),a.end()
#define ll long long int
#define MOD 1000000007
#define MAX 1000100
int main()
{
	int t,ca=1;
	si(t);
	while(t--){
		int n;
		si(n);
		string s;
		cin>>s;
		int len=s.size();
		int cnt=0,x=0,i;
		For(i,len){
			if(i==0)cnt+=(int)(s[i]-'0');
			else{
				if(s[i]=='0')continue;
				if(cnt>=i){
					cnt+=(int)(s[i]-'0');
				}
				else{
					x+=(i-cnt);
					cnt+=(i-cnt)+(int)(s[i]-'0');
				}
			}
		}
		printf("Case #%d: %d",ca,x);
		nl;
		ca++;
	}
	return 0;
}
