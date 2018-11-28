//#include<iostream>
//#include<cstdlib>
//#include<string>
//#include<cstdio>
//using namespace std;
//char s1[50001],s2[50001];
//int n1,n2,Min,sum;
//int main()
//{
//	//freopen("in.txt","r",stdin);
//	int T,num=0;
//	cin>>T;
//	while(T--)
//	{
//		Min=50000;
//		cin>>s1>>s2;
//		n1=strlen(s1);
//		n2=strlen(s2);
//		for(int i=0;i<n1-n2+1;i++)
//		{
//			sum=0;
//			for(int j=i;j<n2+i;j++)
//			{
//				if(s1[j]!=s2[j-i])
//					sum++;
//			}
//			if(sum<Min)
//				Min=sum;
//			sum=0;
//		}
//		cout<<"Case #"<<++num<<": "<<Min<<endl;
//	}
//}


#include<iostream>
#include<fstream>
#include<cmath>
#include<cstdio>
using namespace std;
int T,sum,a,first,last;
long long int A,B,c;
ofstream outfile;
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	outfile.open("output.txt");
	int num=0;
	cin>>T;
	while(T--)
	{
		sum=0;
		cin>>A>>B;
		int a=sqrt((float)A);
		int b=sqrt((float)B);
		if(a*a<A)
			a++;
		for(int i=a;i<=b;i++)
		{
			c=i;
			first=c%10;
			while(c>=10)
				c/=10;
			last=c%10;
			if(first!=last)
				continue;
			c=i*i;
			first=c%10;
			while(c>=10)
				c/=10;
			last=c%10;
			if(first==last)
				sum++;
		}
		outfile<<"Case #"<<++num<<": "<<sum<<endl;
	}
}  