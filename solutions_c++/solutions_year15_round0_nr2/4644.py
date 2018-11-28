#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <fstream>
using namespace std;

#define SZ(X) (int)(X).size()
#define ALL(X) (X).begin(),(X).end()
#define ALLR(X) (X).rbegin(),(X).rend()

const double EPS = 1e-9;
const int INF = 1<<28;
const long long INFL = 1LL<<62;

int main()
{
	ifstream fin;
	fin.open("B-small-attempt2.in",ios::in);
	ofstream fout;
	fout.open("outb.txt",ios::out);
	int t;
	fin >> t;
	for(int c=1;c<=t;++c)
	{
		int d;
		fin >> d;
		priority_queue<int> pq;
		while(d--)
		{
			int p;
			fin >> p;
			pq.push(p);
		}
		int ans = pq.top(),min=0;
		while(pq.top() > 1)
		{
			int div = pq.top()/2;
			if(pq.top() == 9)
			{
				if(pq.size() == 1)
					div = 3;
				else
				{
					pq.pop();
					if(pq.top() == 6 || pq.top() <= 3)
						div = 3;
					pq.push(9);
				}
			}
			if(ans >= (pq.top()+min))
				ans = pq.top()+min;
			min++;
			pq.push(div);
			pq.push(pq.top()-div);
			pq.pop();
			
		}
		fout << "Case #"<<c<<": "<<ans<<endl;
		
	}
	fin.close();
	fout.close();
}
