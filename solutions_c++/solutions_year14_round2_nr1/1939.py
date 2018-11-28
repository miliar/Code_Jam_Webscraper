#include<iostream>
using namespace std;

int f(string s1,string s2)
{
	int c1=0,c2=0,count=0;
	while(c1<s1.length() || c2<s2.length())
	{
		if(s1[c1]!=s2[c2])
		{
			if(s1[c1-1]==s1[c1]){
				while(s1[c1]==s1[c1-1]){
					c1++;count++;
				}
				//count++;
			}
		
			else {if(s2[c2-1]==s2[c2]){
				while(s2[c2]==s2[c2-1]){
					c2++;count++;
				}
			//count++;
			}
			else {return -1;}
		}
		
		}
		else{c1++;c2++;}
		
	
		
	}
	return count;
}
	

int main()
{
/*	string s1="gcj",s2="cj";
	int k=f(s1,s2);
	if(k>=0) cout<<k<<endl;*/
	
	
	int t;cin>>t;
	for(int i=0;i<t;i++)
	{
		int n,result=0,p;cin>>n;
		string s;cin>>s;
		
		for(int j=0;j<n-1;j++)
		{
			string s1;
			cin>>s1;
			//cout<<s<<" "<<s1<<endl;
			p=f(s,s1);
			if(p<0) {break;}
			else result+=p;
		}
		if(p<0) {cout<<"Case #"<<i+1<<": "<<"Fegla Won"<<endl;}
		else cout<<"Case #"<<i+1<<": "<<result<<endl;
	}
}
