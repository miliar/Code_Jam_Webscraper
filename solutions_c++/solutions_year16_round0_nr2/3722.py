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
#include <queue>
#include <cstring>
#include <fstream>
#define ll long long int
using namespace std;
int main()
{
   //freopen("in.txt", "r", stdin);
   //freopen("out.txt", "w", stdout);
   int t;
   scanf("%d\n", &t);
   for(int i = 1; i <= t; i++)
   {
	   string s;
	   getline(cin, s);
	   int res = 0;
	   char prev = '+';
	   for(int i = s.size()-1; i >= 0; i--)
	   {
		   if(s[i] != prev)
		   {
			   res++;
			   prev = s[i];
		   }
	   }
	   printf("Case #%d: %d\n", i, res);
   }
   return 0;
}
