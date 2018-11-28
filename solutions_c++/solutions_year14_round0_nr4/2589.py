/*************************************************************************
    > File Name: D-small.cpp
    > Author: Hu Pengxiang
    > Mail: hpxiangsky@gmail.com 
    > Created Time: Sat 12 Apr 2014 10:05:56 PM CST
 *************************************************************************
 Function:
		1. 
 History:
		1. Created by Hu Pengxiang on Sat 12 Apr 2014 10:05:56 PM CST
 ************************************************************************/

#include<iostream>
#include<algorithm>
#include<list>
using namespace std;

int deceitfulWar(double *A, double *B, int N)
{
	int point = 0;
	int pb1 = 0;
	for(int i = 0;i < N;++i)
	{
		if(A[i] >= B[pb1])
		{
			pb1++;
			point++;
		}
	}
	return point;
}

int war(double *A, double *B, int N)
{
	int point = 0;
	list<double> b;
	list<double>::iterator iter;
	for(int i = 0;i < N;++i)
		b.push_back(B[i]);
	bool bGetPoint;
	for(int i = 0;i < N;++i)
	{
		bGetPoint = false;
		for(iter = b.begin();iter != b.end();++iter)
		{
			if(*iter > A[i])
			{
				b.erase(iter);
				bGetPoint = true;
				break;
			}
		}
		if(!bGetPoint)
		{
			b.pop_front();
			point++;
		}
	}
	return point;
}

int main()
{
	int T;
	int p1, p2;
	cin >> T;
	for(int c = 0;c < T;++c)
	{
		int N;
		cin >> N;
		double A[N], B[N];
		for(int i = 0;i < N;++i)
			cin >> A[i];
		for(int i = 0;i < N;++i)
			cin >> B[i];
		sort(A, A+N);
		sort(B, B+N);

		p1 = deceitfulWar(A, B, N);
		p2 = war(A, B, N);
		cout << "Case #" << c+1 << ": " << p1 << " " << p2 << endl;
	}
	return 0 ;
}



