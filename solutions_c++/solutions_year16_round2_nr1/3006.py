#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Al.out","w",stdout);
ll k,i,t;
cin>>t;
for(k=1;k<=t;k++)
{map<ll,ll> ans;
map<ll,ll> alphabets;
string s;
cin >>s;
ll i;
for(int i=0; i<s.size() ;i++)
{
alphabets[s[i]-'A']++;
if(s[i]=='W') ans[2]++; if(s[i]=='Z') ans[0]++; if(s[i]=='G') ans[8]++; if(s[i]=='U') ans[4]++; if(s[i]=='X') ans[6]++;
}
ans[3]=alphabets['T'-'A']-ans[2]-ans[8];ans[7]=alphabets['S'-'A']-ans[6];ans[5]=alphabets['V'-'A']-ans[7];ans[9]=alphabets['I'-'A']-ans[8]-ans[6]-ans[5];ans[1]=alphabets['O'-'A']-ans[2]-ans[0]-ans[4];

cout<<"Case #"<<k<<": ";
for(i=0;i<10;i++)	
for(int j=0;j<ans[i];j++)
cout<<i;
cout<<endl;	
	

}

   return 0;

}


