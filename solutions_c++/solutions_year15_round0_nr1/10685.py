#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>
#include <set>
#include <string>
#include <cstdio>
#include <cmath>
#include <queue>
#include <iterator>
#include <climits>
#include <complex>
#include <deque>
#include <iomanip>
#include <map>
using namespace std;

#define X real()
#define Y imag()

typedef complex<double> Point;

string nums;

int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	cin>>T;
	for(int ii = 0 ; ii < T ; ii ++)
	{
		int n ;
		cin>> n ;
		n ++;
		int w = 0;
		int j = 0;
		cin>>nums;
		for(int i = 0 ; i < n ; i ++)
		{
			if(i > j)
			{
				w += i - j;
				j += i - j;
			}
			j += nums[i] -'0';
		}
		cout<<"Case #"<<ii + 1<<": "<<w<<endl;
	}
}