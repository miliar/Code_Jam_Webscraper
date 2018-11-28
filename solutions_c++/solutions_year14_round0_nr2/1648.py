#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <list>
#include <set>
#include <numeric>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
using namespace std;
typedef long long LL;

void run(int Case)
{
	long double C,F,X;
	cin >> C >> F >> X;
	long double m=X/2;
	long double s=0;
	long double s2=0;
	int i;
	for(i=1;;i++)
	{
		long double d=C/(2+(i-1)*F);
		if(s*d<s2*s2)
		{
			s+=s2;
			s2=0;
		}
		s2+=d;
		if(s+s2>=m){
			break;
		}
		m=min(s+s2+X/(2+i*F),m);
	}
	cout << "Case #" << Case << ": " << m << endl;
	//cout << i << ", " << C/(2+(i-1)*F) << ", " << s << ", "<< s2 << endl;
}

int main() {
	//std::cout << std::numeric_limits<long double>::digits10 << std::endl;
	cout.precision(20);
	int T;
	cin >> T;
	for (int t=1;t<=T;t++) {
		run(t);
	}
}
