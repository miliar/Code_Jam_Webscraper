#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main(){
	int t;
	ofstream output("output.txt");
	ifstream input("input.txt");
	input>>t;
string s;
input>>s;int ans=0;int l=0;
for(int k=1;k<=t;k++)
{

if(s[0]=='-')
	ans++;

for(int i=1;i<s.size();i++)
{
if(s[i-1]=='+'&&s[i]=='-')
ans+=2;
}
output<<"case #"<<k<<": "<<ans<<endl;
ans=0;
input>>s;
}
output.close();
input.close();
}