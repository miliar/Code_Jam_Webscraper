#include <bits/stdc++.h>
using namespace std;
int a[26];

int reduce(string s)
{
	for(int i=0;i<s.size();i++){int j=(int) (s[i]-'A'); a[j]--;}
}

int main()
{
	fstream cout2;
	cout2.open("answer.txt");

	int t; cin>>t; for(int tt=1;tt<=t;tt++)
	{	
	string s;
	cin>>s;
	for(int i=0;i<26;i++) a[i]=0;
	for(int i=0;i<s.size();i++){int j=(int) (s[i]-'A'); a[j]++;}	
	string ans="";

	for(int k=0;k<a[25];){reduce("ZERO"); ans= ans+"0";}		
	for(int k=0;k<a[20];){reduce("FOUR"); ans= ans+"4";}		
	for(int k=0;k<a[5];){reduce("FIVE"); ans= ans+"5";}		
	for(int k=0;k<a[17];){reduce("THREE"); ans= ans+"3";}		
	for(int k=0;k<a[23];){reduce("SIX"); ans= ans+"6";}
	for(int k=0;k<a[18];){reduce("SEVEN"); ans= ans+"7";}
	for(int k=0;k<a[7];){reduce("EIGHT"); ans= ans+"8";}
	for(int k=0;k<a[8];){reduce("NINE"); ans= ans+"9";}
	for(int k=0;k<a[4];){reduce("ONE"); ans= ans+"1";}
	for(int k=0;k<a[19];){reduce("TWO"); ans= ans+"2";}
	
	sort(ans.begin(),ans.end());	
	cout2<<"Case #"<<tt<<": "<<ans<<endl;
	}
	cout2.close();
	//for(char c='A';c<='Z';c++) cout<<c<<" - "<<endl;
}
