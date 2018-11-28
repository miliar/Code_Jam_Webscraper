#include<bits/stdc++.h>
using namespace std;

typedef long long llint;
typedef unsigned long long ullint;
int main()
{ 


int t;
cin>>t;
int t1=t;
char ch=getchar();

while(t--)
{ 
   


string s;
  map<char,int> mp;
  mp.clear();
  int arr[10]={0,0,0,0,0,0,0,0,0,0};
  
  
getline(cin,s);
for(int i=0;i<s.length();i++)
{  mp[s[i]]++;
	
}

int count=mp['Z'];
mp['E']-=count;
mp['R']-=count;
mp['O']-=count;
arr[0]=count;

count=mp['W'];
mp['T']-=count;
mp['O']-=count;
arr[2]=count;

count=mp['X'];
mp['S']-=count;
mp['I']-=count;
arr[6]=count;

count=mp['U'];
mp['F']-=count;
mp['R']-=count;
mp['O']-=count;
arr[4]=count;


count=mp['S'];
mp['E']-=2*count;
mp['V']-=count;
mp['N']-=count;
mp['S']-=count;
arr[7]=count;


count=mp['O'];
mp['N']-=count;
mp['E']-=count;
arr[1]=count;

count=mp['G'];
mp['E']-=count;
mp['I']-=count;
mp['T']-=count;
mp['H']-=count;
arr[8]=count;

count=mp['H'];
mp['E']-=2*count;
mp['T']-=count;
mp['R']-=count;
arr[3]=count;








count=mp['F'];
mp['E']-=count;
mp['I']-=count;
mp['V']-=count;
arr[5]=count;




count=mp['N'];
mp['E']-=count/2;
mp['I']-=count/2;
arr[9]=count/2;

	cout<<"Case #"<<t1-t<<": ";
for(int i=0;i<10;i++)
{
	int a=0;

	while(a<arr[i])
	{cout<<i;
	a++;}
}
cout<<endl;
}


















return 0;}

