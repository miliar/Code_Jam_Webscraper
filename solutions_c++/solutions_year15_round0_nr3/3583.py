#include <bits/stdc++.h>
using namespace std;
vector <char> multiply(vector <char> A,vector <char> B);

int main() {

	int T,X,L,flag=0,check=0,i,len;
	string str,str1;
	cin>>T;
	for(int k=1;k<=T;k++)
	{
		check=0;
		str1="";
		cin>>X>>L;
		cin>>str;
		for(int i=0;i<L;i++)
		{
			str1.insert(str1.length(),str);
		}
		vector <char> V(2),x(2);
		V[0]='0';
		V[1]='1';
		flag=0;
		for(i=0,len=str1.length();i<len;i++)
		{
		if(flag==0)
		{
		x[0]='0';
		x[1]=str1[i];
		V=multiply(V,x);
		//cout<<i<<" "<<V[1]<<" ";
		if((V[0]=='0')&&(V[1]=='i'))
		{
		flag=1;	
		V[1]='1';
		}
		}
		else if(flag==1)
		{
			x[0]='0';
			x[1]=str1[i];
			V=multiply(V,x);
		//	cout<<V[1]<<" ";
		//	cout<<i<<" ";
			if((V[0]=='0')&&(V[1]=='j'))
			{
				flag=2;
				V[1]='1';
			}
		}
		else
		{
			x[0]='0';
			x[1]=str1[i];
		//	cout<<i<<" ";
			V=multiply(V,x);
			if((V[0]=='0')&&(V[1]=='k'))
			{
				flag=3;
			}
		}
	
	}
	if((V[0]=='0')&&(V[1]=='k')&&(flag>2))
	check=1;
	if(check==1)
	cout<<"Case #"<<k<<": "<<"YES"<<endl;
	else
	cout<<"Case #"<<k<<": "<<"NO"<<endl;
	}
	// your code goes here
	return 0;
}

vector <char> multiply(vector <char> A,vector <char> B)
{
	vector <char> fin(2);
	fin[0]='0';
	if(A[1]=='1')
	{
		if(B[1]=='1')
		{
			fin[1]='1';
		}
		if(B[1]=='i')
		{
			fin[1]='i';
		}
		if(B[1]=='j')
		{
			fin[1]='j';
		}
		if(B[1]=='k')
		{
			fin[1]='k';
		}
	}
	else if(A[1]=='i')
	{
		if(B[1]=='1')
		{
			fin[1]='i';
		}
		if(B[1]=='i')
		{
			fin[0]='1';
			fin[1]='1';
		}
		if(B[1]=='j')
		{
			fin[1]='k';
		}
		if(B[1]=='k')
		{
			fin[0]='1';
			fin[1]='j';
		}
	}
	else if(A[1]=='j')
	{
		if(B[1]=='1')
		{
			fin[1]='j';
		}
		if(B[1]=='i')
		{
			fin[0]='1';
			fin[1]='k';
		}
		if(B[1]=='j')
		{
			fin[0]='1';
			fin[1]='1';
		}
		if(B[1]=='k')
		{
			fin[1]='i';
		}
	}
	else
	{
		if(B[1]=='1')
		{
			fin[1]='k';
		}
		if(B[1]=='i')
		{
			fin[1]='j';
		}
		if(B[1]=='j')
		{
			fin[0]='1';
			fin[1]='i';
		}
		if(B[1]=='k')
		{
			fin[0]='1';
			fin[1]='1';
		}
	}
	fin[0]=((((fin[0]-'0')+(A[0]-'0')+(B[0]-'0'))%2)+'0');
	return fin;
}