#include <bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define upperlimit 1000100
#define INF 1e18
#define eps 1e-8
#define endl '\n'
#define mp make_pair
#define pb push_back
#define pcc pair<char,char>
#define pii pair<int,int>
#define pll pair<ll,ll>
#define tr(container,it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
#define F first
#define S second

using namespace std;

ll gcd(ll n1,ll n2){
	if(n1%n2==0)return n2;
	return gcd(n2,n1%n2);
}
ll powmod(ll base,ll exponent)
{
	ll ans=1;
	while(exponent){
		if(exponent&1)ans=(ans*base)%mod;
		base=(base*base)%mod;
		exponent/=2;
	}
	return ans;
}
int hs[26];
vector <int> answer;
int main()
{
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);

	freopen("A-large.in","r",stdin);
	freopen("Alargeout.txt","w",stdout);

    int t,i,j,k;
    string s;
    int n;
    cin>>t;
    for(k=1;k<=t;k++){
        cin>>s;
        n=s.size();
        answer.clear();
        for(i=0;i<26;i++)hs[i]=0;
        for(i=0;i<n;i++)hs[s[i]-'A']++;
        int temp;
        temp='W'-'A';
        while(hs[temp]){
            hs[temp]--;
            answer.pb(2);
            hs['T'-'A']--;
            hs['O'-'A']--;
        }
        temp='X'-'A';
        while(hs[temp]){
            hs[temp]--;
            answer.pb(6);
            hs['S'-'A']--;
            hs['I'-'A']--;
        }
        temp='G'-'A';
        while(hs[temp]){
            hs[temp]--;
            answer.pb(8);
            hs['E'-'A']--;
            hs['I'-'A']--;
            hs['H'-'A']--;
            hs['T'-'A']--;
        }
        temp='S'-'A';
        while(hs[temp]){
            hs[temp]--;
            answer.pb(7);
            hs['E'-'A']--;
            hs['V'-'A']--;
            hs['E'-'A']--;
            hs['N'-'A']--;
        }
        temp='V'-'A';
        while(hs[temp]){
            hs[temp]--;
            answer.pb(5);
            hs['F'-'A']--;
            hs['I'-'A']--;
            hs['E'-'A']--;
        }
        temp='F'-'A';
        while(hs[temp]){
            hs[temp]--;
            answer.pb(4);
            hs['O'-'A']--;
            hs['U'-'A']--;
            hs['R'-'A']--;
        }
        temp='T'-'A';
        while(hs[temp]){
            hs[temp]--;
            answer.pb(3);
            hs['H'-'A']--;
            hs['R'-'A']--;
            hs['E'-'A']--;
            hs['E'-'A']--;
        }
        temp='Z'-'A';
        while(hs[temp]){
            hs[temp]--;
            answer.pb(0);
            hs['E'-'A']--;
            hs['R'-'A']--;
            hs['O'-'A']--;
        }
        temp='O'-'A';
        while(hs[temp]){
            hs[temp]--;
            answer.pb(1);
            hs['N'-'A']--;
            hs['E'-'A']--;
        }
        temp='N'-'A';
        while(hs[temp]){
            hs[temp]--;
            answer.pb(9);
            hs['I'-'A']--;
            hs['N'-'A']--;
            hs['E'-'A']--;
        }
        cout<<"Case #"<<k<<": ";
        sort(answer.begin(),answer.end());
        n=answer.size();
        for(i=0;i<n;i++)cout<<answer[i];
        cout<<endl;
    }

	return 0;
}
