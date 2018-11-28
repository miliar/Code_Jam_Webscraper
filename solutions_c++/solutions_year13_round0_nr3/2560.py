#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
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

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(int)(b);i++)
#define REP(i,a) for(int i=0;i<(int)(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back

typedef vector<int> vi;
typedef vector<vector<int> > vvi;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

void printvec(vector<int> a)
{
 cout<<"Vecteur:  ";
 REP(i,a.size()) cout<<a[i]<<"  ";
 cout<<endl;
}

bool isPal(long long int x) {
	string s = i2a(x);
	string r = s;
	reverse(ALL(r));

	if(s == r) return true;
	return false;
}

int main()
{

   freopen("C-large-1.in","r",stdin);
   freopen("C-large-1.out","w",stdout);



	int cases;
	scanf("%d",&cases);

	vector<long long> numbers;
	numbers.PB(1);
	numbers.PB(4);
	numbers.PB(9);
	numbers.PB(121);
	numbers.PB(484);
	numbers.PB(10201);
	numbers.PB(12321);
	numbers.PB(14641);
	numbers.PB(40804);
	numbers.PB(44944);
	numbers.PB(1002001);
	numbers.PB(1234321);
	numbers.PB(4008004);
	numbers.PB(100020001);
	numbers.PB(102030201);
	numbers.PB(104060401);
	numbers.PB(121242121);
	numbers.PB(123454321);
	numbers.PB(125686521);
	numbers.PB(400080004);
	numbers.PB(404090404);
	numbers.PB(10000200001LL);
	numbers.PB(10221412201LL);
	numbers.PB(12102420121LL);
	numbers.PB(12345654321LL);
	numbers.PB(40000800004LL);
	numbers.PB(1000002000001LL);
	numbers.PB(1002003002001LL);
	numbers.PB(1004006004001LL);
	numbers.PB(1020304030201LL);
	numbers.PB(1022325232201LL);
	numbers.PB(1024348434201LL);
	numbers.PB(1210024200121LL);
	numbers.PB(1212225222121LL);
	numbers.PB(1214428244121LL);
	numbers.PB(1232346432321LL);
	numbers.PB(1234567654321LL);
	numbers.PB(4000008000004LL);
	numbers.PB(4004009004004LL);

	/*
	for(int i = 1; i <= 10000010; i++) {
		if(isPal(i)) {
			long long x = (long long)i * (long long)i;
			if(isPal(x)) {
				numbers.PB(x);
			}
		}
	}
	*/


	REP(k, cases) {
		printf("Case #%d: ", k + 1);

		long long int a, b;
		cin>>a>>b;
		int count = 0;
		REP(i,numbers.size()) {
			long long x = numbers[i];

			if(x >= (long long)a && x <= (long long)b) count++;
		}

		printf("%d\n", count);
	}


    return 0;
}
