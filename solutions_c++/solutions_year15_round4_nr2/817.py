#ifdef __GNUC__
#include <ext/hash_map>
#include <ext/hash_set>
#else
#include <hash_map>
#include <hash_set>
#endif

namespace std
{
 using namespace __gnu_cxx;
}

#include <fstream>
#include <vector>
#include <string>
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <algorithm>
#include <math.h>
#include <cstdlib>
#include <climits>
#include <iomanip> 
using namespace std;

typedef long long LL;
typedef long double LD;
template<class T>

T prime(T a , T b)
{
	cout << a << "\t"<<b << endl;
	if ( a >= b)
		return (prime(b , a));
	if(a == 0)
		return b;
	return prime(a , b%a);
}

string its(int n)
{
	string ret;
	if(n == 0)
	{
		ret = "0";
		return ret;
	}
	while(n > 0)
	{
		ret += (n % 10 + '0');
		n /= 10;
	}
	reverse(ret.begin() , ret.end());
	return ret;
}

double cal(double v0, double x0, double v1, double x1,double V, double X) {
	double t1 = ((V * X - V * x1)/(x0 - x1))/v0;
	double t2 = (V * X - V * x0)/ (x1 - x0) / v1;
	return max(t1, t2);
	
}

int main()
{
//==============in put=================
	ifstream curFile("B-small-attempt0.in");
	vector<double> result;
	int T; // testcases count
	double V;
	double X;
	int N;
	if(curFile.is_open())
	{
		curFile >> T;
		for(int c = 0 ; c < T ; c++)
		{
//==============solution==================
			cout << "Enter Test case:" << c + 1 << endl;
			curFile >> N;
			curFile >> V;
			curFile >> X;
			vector<double> v;
			vector<double>x;
			for (int i = 0 ; i < N ; i ++) {
				double vt,  vx;
				curFile >> vt;
				curFile >> vx;
				v.push_back(vt);
				x.push_back(vx);
			}
			if (N == 1) {
				if (x[0] == X)
					result.push_back(V/v[0]);
				else
					result.push_back(-2);
			}
			else if (N == 2) {
				if (x[0] == X) {
					if (x[1] != X)
						result.push_back(V/v[0]);
					else
						result.push_back(V/(v[0] + v[1]));
				}
				else if (x[1] == X) 
						result.push_back(V/v[1]);
				else {
					if (x[0] > X) {
						if (x[1] > X)
							result.push_back(-2);
						else {
							result.push_back(cal(v[0], x[0], v[1],x[1],V,X));
						}
					}
					else {
						if (x[1] < X)
							result.push_back(-2);
						else {
							result.push_back(cal(v[0], x[0], v[1],x[1],V,X));

						}
					}
				}
			}
//==============solution end==============
		}	
	}
	curFile.close();
//==============out put==================
	ofstream outfile;
	outfile.open("result.txt");
	if(outfile.is_open())
	{
		outfile << setprecision(10);
		for(int i = 0; i < result.size() ; i++) {
			if (result[i] > -1) {
			outfile << "Case #" << i + 1<< ": " <<result[i] << endl;
			cout << "Case #" << i + 1<< ": " <<result[i] << endl;
			}
			else {
			outfile << "Case #" << i + 1<< ": " <<"IMPOSSIBLE" << endl;
			cout << "Case #" << i + 1<< ": " <<"IMPOSSIBLE"<< endl;

			}
		}
	}
	outfile.close();
	return 0;
}
