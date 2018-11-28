#include <bits/stdc++.h>
using namespace std;
#define lim
#define ll long long
//ll a[lim+1];
#define pb push_back

string getans(string s)
{
	int a[26];
	for(int i=0;i<26;i++)
	a[i]=0;
	int kk=s.length();
	for(int i=0;i<kk;i++)
	a[s[i]-'A']++;
	string ans="";
	 while(a['z'-'a'])
	 {
	 	ans+="0";
	 	a['Z'-'A']--;
	 	a['E'-'A']--;
	 	a['R'-'A']--;
	 	a['O'-'A']--;
	 }
	  while(a['w'-'a'])
	 {
	 	ans+="2";
	 	a['T'-'A']--;
	 	a['W'-'A']--;
	 	a['O'-'A']--;
	 	//a['O'-'A']--;
	 }
	  
	  while(a['x'-'a'])
	 {
	 	ans+="6";
	 	a['S'-'A']--;
	 	a['I'-'A']--;
	 	a['X'-'A']--;
	 	//a['O'-'A']--;
	 }
	 while(a['s'-'a'])
	 {
	 	ans+="7";
	 	a['S'-'A']--;
	 	a['E'-'A']--;
	 	a['V'-'A']--;
	 	a['E'-'A']--;
	    a['N'-'A']--;
	 }
	 while(a['v'-'a'])
	 {
	 	ans+="5";
	 	a['F'-'A']--;
	 	a['I'-'A']--;
	 	a['V'-'A']--;
	 	a['E'-'A']--;
	 }
	  while(a['g'-'a'])
	 {
	 	ans+="8";
	 	a['E'-'A']--;
	 	a['I'-'A']--;
	 	a['G'-'A']--;
	 	a['H'-'A']--;
	 	a['T'-'A']--;
	 }
	  while(a['f'-'a'])
	 {
	 	ans+="4";
	 	a['F'-'A']--;
	 	a['O'-'A']--;
	 	a['U'-'A']--;
	 	a['R'-'A']--;
	 }
	  while(a['r'-'a'])
	 {
	 	ans+="3";
	 	a['T'-'A']--;
	 	a['H'-'A']--;
	 	a['R'-'A']--;
	 	a['E'-'A']--;
	    a['E'-'A']--;
	 }
	  
	  while(a['o'-'a'])
	 {
	 	ans+="1";
	 	a['O'-'A']--;
	 	a['N'-'A']--;
	 	a['E'-'A']--;
	 	// a['E'-'A']--;
	  //  a['E'-'A']--;
	 }
	  while(a['n'-'a'])
	 {
	 	ans+="9";
	 	a['N'-'A']--;
	 	a['I'-'A']--;
	 	a['N'-'A']--;
	 	a['E'-'A']--;
	    //a['E'-'A']--;
	 }
	 //int kkl=ans.length();
	 sort(ans.begin(),ans.end());
	 return ans;
	 
	 
	
}
int main() 
{
int t;
//freopen("input.txt","r",stdin);
cin>>t;
string s;
for(int i=1;i<=t;i++)
{
	cin>>s;
	
	
	cout<<"Case #"<<i<<": "<<getans(s)<<endl;
}
}