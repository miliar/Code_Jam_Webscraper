#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <stdlib.h>
#include <ctime>
#include <queue>
#include <set>
#include <iostream>
#include <stack>
#include <list>
#include <iterator>

typedef unsigned long long ull;
#define mp make_pair
#define pb push_back

const long double eps = 1e-9;
const double pi = acos(-1.0);
const long long inf = 1e18;

using namespace std;
vector <int> A;
vector <int> B;
int p;
bool func( int i)
{
	return (i>p);
}
int main()
{
	ifstream in ("in.txt");
	int t;
	in>>t;
	ofstream fout ("out.txt");
	for (int po=1; po<=t; ++po)
	{
		A.clear();
		B.clear();
		int min=100;
		int kol;
		int m;
		in>>m;
		for (int i=0; i<m; ++i)
		{
			int a;
			in>>a;
			A.push_back(a);
		}
		for (p=1; p<=9; ++p)
		{
			kol=0;
			B.clear();
			for (int i=0; i<m; ++i)
				B.push_back(A[i]);
			vector <int>::iterator it=find_if(B.begin(), B.end(), func);
			while (it!=B.end())
			{
				int i=it-B.begin();
				kol++;
				int k=p;
				B.push_back(k);
				B[i]-=k;
				it=find_if(B.begin(), B.end(), func);
			}
			if ((p+kol)<=min)
				min=p+kol;
		}

		
		fout<<"Case #"<<po<<": "<<min<<endl;
	}	
	fout.close();
	in.close();
	return 0;
}