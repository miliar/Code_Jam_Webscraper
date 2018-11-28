#include <stdio.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <queue>
#include <cstdio>
#include <fstream>
using namespace std;

int N=40;
unsigned long long fsq[] = {0, 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321,			4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521,
			400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321,
			40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201,
			1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121,
			1232346432321, 1234567654321, 4000008000004, 4004009004004};

int main()
{
	freopen("C-large-1.in", "r", stdin);
	freopen("C-large-1.out", "w", stdout);
	int T=0;
	cin>>T;
	for (int t=1; t<=T; t++){
		unsigned long long n1=-1, n2=-1;
		cin>>n1>>n2;
		int number=0;
		for (int i=0; i<N; i++)
			if (fsq[i]>=n1&&fsq[i]<=n2)
				number++;
		cout<<"Case #"<<t<<": "<<number<<"\n";
	}
	return 0;
}