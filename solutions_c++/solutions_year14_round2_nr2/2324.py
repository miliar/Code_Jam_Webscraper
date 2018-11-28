#include<iomanip>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<ctype.h>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<fstream>

#define min(a,b) a<b?a:b;

using namespace std;

//ifstream inx("ad.txt");
ofstream onx("o.txt");
int and(int a,int b)
{
	return a&b;
}
long long cal(int a,int b,int k)
{long long ans=0;
	
for(int i=0;i<a;i++)
	for(int j=0;j<b;j++)
		if(and(i,j)<k)ans++;


return ans;
}
int main()
{
	
	int ntc
		;
	cin>>ntc;
	int cas=1;
	int a,b,k;
	long long ans=0;
	while(ntc--)
	{
		cin>>a>>b>>k;

		ans=cal(a,b,k);
		onx<<"Case #"<<cas++<<": ";
		//cout<<"Case #"<<cas++<<": ";
		
		//fprintf(onx,"%.7f\n",seconds);
	   //onx << setprecision(7) << std::fixed;
		onx<<  ans << '\n';
//cout<<  ans << '\n';

	}
	//system("pause");
}