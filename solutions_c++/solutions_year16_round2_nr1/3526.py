#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main() {
	
	
	ll tc;cin>>tc;
	for(ll iii=1;iii<=tc;iii++)
	{
		ll cnt[10]={0},alpha[26]={0};

		string s;
		cin>>s;
		ll n = s.length();
		
		for(ll i=0;i<n;i++)
		{
			alpha[s[i]-65]+=1;
		}
		
		
		cnt[0]+=alpha[25];
		cnt[2]+=alpha[22];
		
		cnt[3]+= (alpha[7]-alpha[6]);if(cnt[3]<0)cnt[3]=0;
		cnt[4]+=alpha[20];
		
		cnt[6]+=alpha[23];
		cnt[7]+= (alpha[18]-alpha[23]);if(cnt[3]<0)cnt[7]=0;
		cnt[5]+=	alpha[21]-cnt[7];if(cnt[5]<0)cnt[5]=0;
		
		
		cnt[8]+=alpha[6];
		cnt[9]+=alpha[8]-cnt[6]-cnt[5]-cnt[8];if(cnt[9]<0)cnt[9]=0;
		
		cnt[1]+= s.length()-cnt[0]*4 -cnt[2]*3 -cnt[3]*5 -cnt[4]*4 -cnt[5]*4 -cnt[6]*3 -cnt[7]*5-cnt[8]*5-cnt[9]*4 ;
		cnt[1]/=3;
		
	cout<<"Case #"<<iii<<": ";	
	for(ll i=0;i<10;i++)
	{
		for(ll j=0;j<cnt[i];j++)
		cout<<i;
	}
	cout<<"\n";	
	}
	
	
	return 0;
}