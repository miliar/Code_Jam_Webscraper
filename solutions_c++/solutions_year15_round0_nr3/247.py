#include<bits/stdc++.h>
/*krypto...........................jagsxi....!! */
using namespace std;
int look[10005];

int mapped(char c)
{
	if(c=='i')
	return 2;
	if(c=='j')
	return 3;
	if(c=='k')
	return 4;
}
int mat1[5][5]={0,0,0,0,0,
	         0,1,2,3,4,		
	         0,2,-1,4,-3,
	         0,3,-4,-1,2,
	         0,4,3,-2,-1
			 };
			 
int mat2[5][5]={0,0,0,0,0,		
	         0,1,-2,-3,-4,
	         0,2,1,4,-3,
	         0,3,-4,1,2,
	         0,4,3,-2,1
			 };
			 


int main()
{

    freopen("in3.txt", "r", stdin);
  freopen("3.txt", "w", stdout);
	ios_base::sync_with_stdio(false);
	int t,l,x,lgt;
	cin>>t;
	string s,temp;
	for(int i=1; i<=t; i++)
	{
		cin>>l>>x;
		cin>>s;
		temp=s;
		lgt=l*x;
		for(int j=0; j<x-1; j++)
		s=s+temp;

		look[1]=mapped(s[0]);
		for(int j=2; j<=lgt; j++)
		{
			if(look[j-1]>0)
			look[j]=mat1[abs(look[j-1])][mapped(s[j-1])];
			else
			look[j]=-mat1[abs(look[j-1])][mapped(s[j-1])];
		}
		bool flag=false;
		int a1,a2,a3,t1,t2,t3;
		for(int j=1; j<=lgt; j++)
		{
			for(int k=j+1; k<=lgt; k++)
			{
				a1=look[j];
				a2=look[k];
				a3=look[lgt];
				
				if(a1!=2)
				continue;
				
				if(a1>0 && a2>0 || a1<0 && a2<0)
				t1=mat2[abs(a2)][abs(a1)];
				else
				t1=-mat2[abs(a2)][abs(a1)];;
				
				if(a2>0 && a3>0 || a1<0 && a2<0)
				t2=mat2[abs(a3)][abs(a3)];
				else
				t2=-mat2[abs(a3)][abs(a2)];;
				
				if(t1==3 && t2==4)
				{
					j=lgt+1;
					flag=true;
					break;
				}
			}
		}
		if(flag)
		cout<<"Case #"<<i<<": "<<"YES"<<endl;
		else
		cout<<"Case #"<<i<<": "<<"NO"<<endl;
	}
	return 0;
}
