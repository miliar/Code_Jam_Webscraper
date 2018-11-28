#include<iostream>

using namespace std;

int A[10][10];
void f1()
{
	int a,b,c;
	return;
}

int main()
{
	int t,state=0;
	cin>>t;
	for(int test=0;test<t;test++){
		state=0;
	A[1][1]=1;
	A[1][2]=2;
	A[1][3]=3;
	A[1][4]=4;
	A[2][1]=2;
	A[2][2]=-1;
	A[2][3]=4;
	A[2][4]=-3;
	A[3][1]=3;
	A[3][2]=-4;
	A[3][3]=-1;
	A[3][4]=2;
	A[4][1]=4;
	A[4][2]=3;
	A[4][3]=-2;
	A[4][4]=-1;
	f1();
	int l,x,a,b,c,i,j,k;
	int B[100000];
	int C[100000];
	string str2;
	string str1="";
	cin >> l >> x;
	f1();
	cin >> str2;
	for(i=0;i<x;i++)
		str1+=str2;
	cout<<"Case #"<<test+1<<": ";
	for(i=0;i<str1.length();i++)
	{
		if(i==0)
		{
			if(str1[i]=='1')
				B[i]=1;
			else
				B[i]=str1[i]-'g';
			f1();
		}
		else
		{
			if(str1[i]=='1')
				B[i]=B[i-1];
			else
			{
				if(B[i-1]>0)
					B[i]=A[B[i-1]][str1[i]-'g'];
				else
					B[i]=(-1)*A[(-1)*B[i-1]][str1[i]-'g'];
				f1();
			}
		}
	}
	for(i=str1.length()-1;i>=0;i--)
	{
		f1();
		if(i==str1.length()-1)
		{
			f1();
			if(str1[i]=='1')
				C[i]=1;
			else
				C[i]=str1[i]-'g';
		}
		else
		{
			if(str1[i]=='1')
				C[i]=C[i+1];
			else
			{
				f1();
				if(C[i+1]>0)
					C[i]=A[str1[i]-'g'][C[i+1]];
				else
					C[i]=(-1)*A[str1[i]-'g'][(-1)*C[i+1]];
			}
		}
	}
	f1();
	//for(i=0;i<l*x;i++)cout<<B[i]<<" ";cout<<endl;
	//for(i=0;i<l*x;i++)cout<<C[i]<<" ";cout<<endl;
	for(i=0;i<str1.length();i++)
	{
		if(B[i]==2)
		{
			int sum=-10;
			for(j=i+1;j<str1.length();j++)
			{
				if(sum==3)
				{
					if(C[j]==4)
					{
						cout << "YES\n";
						state=1;
						break;
					}
				}
				if(sum==-10)
				{
					if(str1[j]=='1')
						sum=1;
					else
						sum=str1[j]-'g';
				}
				else
				{
					if(str1[j]!='1' && sum>0)
						sum=A[sum][str1[j]-'g'];
					else if(str1[j]!='1' && sum<0)
						sum=(-1)*A[sum*(-1)][str1[j]-'g'];
				}
				if(state==1)
					break;
			}
		}
			if(state==1)
				break;
	}
	if(state==0)
	cout<<"NO\n";
	}
	return 0;
}
