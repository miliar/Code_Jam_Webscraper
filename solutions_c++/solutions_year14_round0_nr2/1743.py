// QualRound.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"

#include "iostream"
#include "string"
#include "string.h"
#include "vector"
#include "algorithm"
using namespace std;

int main()
{
//	freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-small-attempt.out","w",stdout);
	freopen("B-Large.in","r",stdin);
	freopen("B-Large.out","w",stdout);
	int T=0;
	cin>>T;
	for(int tc=0;tc<T;tc++)
	{
		double C,F,X;
		cin>>C>>F>>X;
		double time=0;
		double speed=2.0;
		while(1)
		{
			if((X-C)/speed>X/(speed+F))
			{
				time+=C/speed;
				speed+=F;
			}
			else
			{
				time+=X/speed;
				break;
			}
		}
		printf("Case #%d: %.8lf\n",tc+1,time);
	}
	return 0;
}