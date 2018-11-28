/*************************************************************************
	> File Name: pA.cpp
	> Author: fuyu0425/a0919610611
	> School: National Chiao Tung University
	> Team: NCTU_Ragnorok
	> Mail: a0919610611@gmail.com
	> Created Time: 西元2016年04月09日 (週六) 13時58分20秒
 ************************************************************************/
#include <bits/stdc++.h>
using namespace std;
typedef long long int LL;
bool used[10];
int digit=0;
bool check(long long int num)
{
		while(num)
		{
			LL d=num%10;
			num/=10;
			if(!used[d])
			{
				used[d]=true;
				digit++;
			}
			if(digit==10)return true;
		}
		return false;
}
int main()
{

	int T;
	cin>>T;
	int kase=0;
	while(T--)
	{	
		memset(used,0,sizeof(used));
		digit =0;
		LL n;
		cin>>n;
		if (kase++) cout<<endl;
		cout<<"Case #"<<kase<<": ";
		if(n==0)
		{
			cout<<"INSOMNIA";
			continue;
		}else
		{	
			LL now=n;
			while(!check(now))
			{
				now+=n;
			}
			cout<<now;
		}
	}
     return 0;
}
