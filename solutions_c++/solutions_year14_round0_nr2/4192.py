#include<iostream>
#include<cstdio>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
//int arr[51][51];
double arr[1005];
double brr[1005];
int crr[1005];
int main()
{
	int i,j,t,k,n,a,b,r,ii,l,m,nao,ken,tst;
	//fstream cin;
	double p,ans,x,y,c,f,ct,tim,z;
	//cin.open("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2014\\Quali\\B\\Small Input.txt",ios::in);
	//freopen("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2014\\Quali\\B\\Small Output.txt","w",stdout);
	cin>>t;
	for(tst=1;tst<=t;tst++)
	{
		cout<<"Case #"<<tst<<": ";
		cin>>c>>f>>x;
		p=2;
		ct=0;
		tim=0;
		while(ct<x)
		{
			ans=c/p;
			if((x-ct)/p<ans)
			{
				break;
			}
			tim+=ans;
			ct+=p*ans;
			z=(x-ct)/p;//xpctd time
			if(c<=z*f)
			{
				p+=f;
				ct-=c;
			}
		}
		tim+=(x-ct)/p;
		printf("%.9f",tim);
		
		
		
		
		cout<<endl;
	}
	return 0;
}