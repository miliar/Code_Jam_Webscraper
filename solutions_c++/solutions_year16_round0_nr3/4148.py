#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
long long int pow1(int,int); 
int main()
{
	int T,i,j,N,J1,k;
	long long double nu;
//	std::fstream IP("input.txt", std::ios_base::in);
	std::fstream IP("C-small-attempt0.in", std::ios_base::in);
	IP>>T;
	std::fstream OP("OPsmall.txt", std::ios_base::out);
	IP>>N;
//	cout<<N<<"check1\n";
	IP>>J1;
//	cout<<J1<<"check2\n";
	int S[N];
	long long int rep=0,count=0,temp;
	S[0]=1;
	S[N-1]=1;
	for(i=1;i<N-1;i++)
		S[i]=0;
	for(j=0;j<N;j++)
			cout<<S[j];
//	cout<<"check10\n";
	OP<<"Case #1:\n";
	while((count<J1)&&(rep<pow1(2,N-1)))
	{
//		for(j=0;j<N;j++)
//			cout<<S[j];
//		cout<<"check\n";
		long long int flag[9];
		bool out_flag=true;
		for(j=2;j<=10;j++)
		{
			nu=pow1(j,N-1)+1;
			for(k=1;k<N-1;k++)
				nu=nu+S[k]*pow1(j,N-1-k);
//			cout<<nu<<"check12\n";
			flag[j-2]=-1;
			for(k=2;k<=sqrt(nu);k++)
				if(nu%k==0)
				{
					flag[j-2]=k;
					break;
				}
			if(flag[j-2]==(-1))
			{
				out_flag=false;
				break;
			}
		}
//		cout<<out_flag<<"check15\n";
		if(out_flag==true)
		{
			for(j=0;j<N;j++)
				OP<<S[j];
			OP<<" ";
			for(j=0;j<9;j++)
			{
				OP<<flag[j];
				OP<<" ";
//				cout<<flag[j]<<"check13 ";
			}
			OP<<"\n";
//			cout<<"\n";
			count++;
		}
//		cout<<out_flag<<"check16\n";
		rep++;
		temp=rep;
		for(j=N-2;j>0;j--)
		{
			S[j]=temp%2;
			temp=temp/2;
		}
//		cout<<count<<"check17\n";
	}		
//	cout<<J1<<"check3\n";
	return 0;
}
long long int pow1(int a,int b)
{
	long long int temp=1;
	for(int ff=0;ff<b;ff++)
		temp=temp*a;
	return temp;
}