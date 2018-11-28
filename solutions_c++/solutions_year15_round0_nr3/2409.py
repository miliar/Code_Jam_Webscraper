#include <iostream>
#include <cstring>
#include <stack>
#include <cstdio>
#include <map>
using namespace std;
#define LL long long
#define MOD 1000000007
#define pcc pair<char,char>
#define ff first
#define ss second


LL arr[5][5];

LL poww(LL a, LL n)
{
	if(n==1)
	{
		return a; 
	}
	LL v=poww(a,(n/2));
	if(v<0)
	v=arr[-v][-v];
	else
	v=arr[v][v];
	if(n%2)
	{
		if(a>0)
		{
			if(v>0)
			v=arr[v][a];
			else
			v=-arr[-v][a];
		}
		else
		{
			if(v>0)
			v=-arr[v][-a];
			else
			v=arr[-v][-a];
		}
	}
	return v;
}




int main() {
 freopen("input3.txt","r",stdin);
 freopen("output1.txt","w",stdout);
 int t;
 cin>>t;int cc=0;int n;
 arr[1][1]=1;
 arr[1][2]=2;
 arr[1][3]=3;
 arr[1][4]=4;

 arr[2][1]=2;
 arr[2][2]=-1;
 arr[2][3]=4;
 arr[2][4]=-3;
 
 arr[3][1]=3;
 arr[3][2]=-4;
 arr[3][3]=-1;
 arr[3][4]=2;
 
 arr[4][1]=4;
 arr[4][2]=3;
 arr[4][3]=-2;
 arr[4][4]=-1;
 
 string s;
 LL l,x;
 string tmp;
 while(t--)
 {
 	
 	cc++;
 	cin>>l>>x;
 	cin>>tmp;
 	s="";
 	LL cnt=min(21LL,x);
 	for(int i=1;i<=cnt;++i)
 	{
 		s+=tmp;
 	}
 	for(int i=0;i<s.size();++i)
 	{
 		if(s[i]=='i')s[i]='2';
 		if(s[i]=='j')s[i]='3';
 		if(s[i]=='k')s[i]='4';
 	}
 	
 	int prod1=s[0]-'0';
 	int fl=-1;
 	if(prod1==2)fl=0;
 	else
 	for(int i=1;i<s.size();++i)
 	{
 		int nxt=s[i]-'0';
 		if(prod1<0)
 		prod1=-arr[-prod1][nxt];
 		else
 		prod1=arr[prod1][nxt];
 		
 		if(prod1==2){
 			fl=i;break;
 		}
 	}
 	prod1=s[s.size()-1]-'0';
 	int fl2=-1;
 	if(prod1==4)fl2=s.size()-1;
 	else
 	for(int i=s.size()-2;i>=0;--i)
 	{
 		int nxt=s[i]-'0';
 		if(prod1<0)
 		prod1=-arr[nxt][-prod1];
 		else
 		prod1=arr[nxt][prod1];
 		if(prod1==4){
 			fl2=i;break;
 		}
 	}
 	LL prod2=s[0]-'0';
 	for(int i=1;i<tmp.size();++i)
 	{
 		int nxt=s[i]-'0';
 		if(prod2<0)
 		prod2=-arr[-prod2][nxt];
 		else
 		prod2=arr[prod2][nxt];
 	}
 	
 	
 	prod2=poww(prod2,x);
 /*	cout<<prod2<<" "<<fl<<" "<<fl2<<"\n";
 	prod2=poww(prod2,2);
 	cout<<prod2<<" "<<fl<<" "<<fl2<<"\n";*/
	string anse;
 	if(prod2==-1 && fl>=0 && fl2>fl+1)
 	anse="YES";
 	else anse="NO";
 	
 	
 	
 	
 	
 	
 	cout<<"Case #"<<cc<<": "<<anse<<"\n";
 	
 	
 }
 
    
  return 0;
}
