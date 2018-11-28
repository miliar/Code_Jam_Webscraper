#include <iostream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
using namespace std;
#include<stdio.h>
bool mycmp(int a,int b)
{
	return a < b;
}
int HowManyTimes(int n, int T, int & N)
{
	int ret = 0;
	while(n<= T)
	{
		n += n-1;
		ret ++;
	}
	N = n+T;
	return ret;
}
int compute(int v, vector<int> p)
{
	if(v == 1) return p.size();
	if(p.size() == 1)
	{
		return v <= p[0];
	}
	else
	{
		vector<int> q;
		for(int j = 1; j< p.size(); ++j) q.push_back(p[j]);
		int N = 0;
		return min(compute(v,q)+1,HowManyTimes(v,p[0],N)+compute(N,q));
	}
}
int main( )
{
	int T;
	int C,N;
	cin >> T;
	for(int t = 1; t<= T; ++t){
		cin >> C >> N;
		vector<int> p;
		int a;
		for(int i = 0; i< N; ++i) {
			cin >> a;
			p.push_back(a);
		}
		sort(p.begin(),p.end(),mycmp);
		int ret = compute(C,p);
		cout << "Case #" << t << ": " << ret << endl;
	}
}
