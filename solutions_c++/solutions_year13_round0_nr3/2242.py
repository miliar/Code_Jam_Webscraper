/*
 * main.cpp
 *
 *  Created on: 2013-4-13
 *      Author: bu540402
 */
#include<iostream>
#include<cmath>
#include<stack>
using namespace std;
#define en 10000005
#define LL long long
LL base[40]={1,
		4,
		9,
		121,
		484,
		10201,
		12321,
		14641,
		40804,
		44944,
		1002001,
		1234321,
		4008004,
		100020001,
		102030201,
		104060401,
		121242121,
		123454321,
		125686521,
		400080004,
		404090404,
		10000200001ll,
		10221412201ll,
		12102420121ll,
		12345654321ll,
		40000800004ll,
		1000002000001ll,
		1002003002001ll,
		1004006004001ll,
		1020304030201ll,
		1022325232201ll,
		1024348434201ll,
		1210024200121ll,
		1212225222121ll,
		1214428244121ll,
		1232346432321ll,
		1234567654321ll,
		4000008000004ll,
		4004009004004ll,
		100000020000001ll};
int main()
{
	//freopen("data.in","r",stdin);
	int t;
	cin>>t;
	for(int cas=1;cas<=t;cas++)
	{
		printf("Case #%d: ",cas);
		LL a,b;
		cin>>a>>b;
		int cnt=0;
		for(int i=0;i<40;i++)
		{
			if(base[i]>=a&&base[i]<=b)
				cnt++;
		}
		cout<<cnt<<endl;
	}
}

