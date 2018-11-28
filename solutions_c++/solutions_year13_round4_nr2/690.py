// GCJ2013R3.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_set>

#pragma warning(disable:4996)

using namespace std;

long long T,P,N;

void init()
{
	cin >> T;
}

void work()
{
	long long x,y;
	int a[64];
	long long er[64];
	for (int ca=1; ca<=T; ca++)
	{
		cin >> N >> P;
		cout << "Case #" << ca << ": ";
		
		long long p;
		x=0;
		
		er[0]=1;
		for (int i=1;i<=N;i++)
		{
			er[i] = er[i-1] << 1;
		}
		int startz=0;
		p=P;
		for (int i=0; i<N; i++)
		{
			if (p >= er[N-i])
				break;
			startz++;
		}
		p=P-1;
		for (int i=0; i<N; i++)
		{
			if (p < er[N-i-1])
			{
				a[i]=1;
			}
			else
			{
				a[i]=0;
				p -= er[N-i-1];
			}
			//cout << a[i] << endl;
		}
		
		y=0;
		for (int i=0; i<startz; i++)
		{
			y=y*2+1;
		}
		x=0;
		for (int i=0; i<N; i++)
		{
			if (a[i])
			{
				break;
			}
			else
			{
				x=x*2+1;
			}
		}

		y=er[N]-y-1;
		if (x>0)
		{
			x=x*2;
		}
		if (er[N]==P)
			x=er[N]-1;
		cout << x << " " << y << endl;
		
	}
}


int main()
{
	freopen("C:\\Users\\yuazh\\Downloads\\B-large.in", "r", stdin);
	freopen("C:\\Users\\yuazh\\Downloads\\B-large.out", "w", stdout);
	init();
	work();

	return 0;
}



