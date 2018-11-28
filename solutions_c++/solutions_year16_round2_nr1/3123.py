#include <bits/stdc++.h>
using namespace std;
#define ll          long long int
#define mem(a,x)    memset(a,x,sizeof(a))
#define vi          vector<int>
#define vii         vector<vi>
#define pi          pair<int,int>
#define pii         pair<int,pi>
#define si(x)       scanf("%lld",&x)
#define sl(x)       scanf("%I64d",&x)
#define ss(s)       scanf("%s",s)
#define rep(i,a,b)  for(i=a;i<b;i++)

#define tr(it,container) for(auto it=container.begin();it!=container.end();++it)
#define F           first
#define S second
#define gc          getchar_unlocked
#define pb          push_back
#define mp          make_pair
#define all(a)      a.begin(),a.end()
#define sortall(a)  sort(all(a))
#define M         	1000000007
#define N           100005
ll pwr(ll a,ll b,ll mod) {a%=mod;if(a<0)a+=mod;ll ans=1; while(b) {if(b&1) ans=(ans*a)%mod; a=(a*a)%mod; b/=2; } return ans; }
ll gcd(ll a,ll b) {while(b) {ll temp=a; a=b; b=temp%b; } return a; }

int f(char c){
	return (c-'A');
}

int main(){
	
	int t;
	cin>>t;
	int g=1;
	while(t--){
        int a[10]={0},b[26]={0};
        string s;
		cin>>s;
		int n=s.length(),i,j;
		for(i=0;i<n;i++){
			b[s[i]-'A']++;
		}
		int tmp;
		tmp = b[25];b[f('E')] -= tmp;b[f('R')] -= tmp;b[f('O')] -= tmp;
		a[0] = tmp;
		tmp = b[f('X')];b[f('S')] -= tmp;b[f('I')] -= tmp;
		a[6] = tmp;
		tmp = b[f('U')];b[f('F')] -= tmp;b[f('O')] -= tmp;b[f('R')] -= tmp;
		a[4] = tmp;
		tmp = b[f('R')];b[f('T')] -= tmp;b[f('H')] -= tmp;b[f('E')] -= 2*tmp;
		a[3] = tmp;
		tmp = b[f('S')];b[f('V')] -= tmp;b[f('N')] -= tmp;b[f('E')] -= 2*tmp;
		a[7] = tmp;
		tmp = b[f('H')];b[f('E')] -= tmp;b[f('I')] -= tmp;b[f('G')] -= tmp;b[f('T')] -= tmp;
		a[8] = tmp;
		tmp = b[f('W')];b[f('O')] -= tmp;b[f('T')] -= tmp;//b[f('R')] -= tmp;
		a[2] = tmp;
		tmp = b[f('O')];b[f('N')] -= tmp;b[f('E')] -= tmp;//b[f('R')] -= tmp;
		a[1] = tmp;
		tmp = b[f('N')];
		tmp /= 2;
		b[f('I')] -= tmp;b[f('E')] -= tmp;//b[f('R')] -= tmp;
		a[9] = tmp;
		tmp = b[f('F')];b[f('I')] -= tmp;b[f('V')] -= tmp;b[f('E')] -= tmp;
		a[5] = tmp;
		cout<<"Case #"<<g<<": ";
		for(i=0;i<10;i++){
			for(j=0;j<a[i];j++){
				cout<<i;
			}
		}
		cout<<endl;
		g++;
	}

	return  0;
}