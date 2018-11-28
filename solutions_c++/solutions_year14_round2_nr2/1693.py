#include <fstream>
#include <math.h>
#include <stdio.h>
//#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <stdlib.h> 
#include <set>
#include <queue>
using namespace std;
//#pragma comment(linker, "/STACK:999999999")
#define ll long long
const long long MAXN = 102;
const long double eps=0.00000000001;

typedef vector<long long> lnum;


ifstream cin("input.txt");
ofstream cout("output.txt");





int main()
{
	int qq;
	cin>>qq;
	for (int ww=0;ww<qq;ww++)
	{
		int a,b,c;
		cin>>a>>b>>c;
		cout<<"Case #"<<ww+1<<": ";
		long long r=0;
		for (int i=0;i<a;i++)
			for (int j=0;j<b;j++)
			{
				long long h=i&j;
				if (h<c)
				{
					r++;
				}
			}
		cout<<r<<endl;
	}





	
	

		return 0;
}