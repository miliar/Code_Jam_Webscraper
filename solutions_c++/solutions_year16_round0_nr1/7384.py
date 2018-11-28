#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <sstream>
#include <numeric>
#include <bitset>
#define REP(i, a, b) for ( int i = int(a); i <= int(b); i++ )
#define PB push_back
#define MP make_pair
#define for_each(it, X) for (__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define DFS_WHITE -1
#define DFS_BLACK 1
#define MAXN 1000
#define pi 3.141592653589793
#define ARRAY_SIZE(A) sizeof(A)/sizeof(A[0])
#define INF 1<<30
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int, int> ii;
void splitNumber(std::vector<int>& digits, ll number) {
  if (0 == number) { 
    digits.push_back(0);
  } else {
    while (number != 0) {
      ll last = number % 10;
      digits.PB(last);
      number = (number - last) / 10;
    }
  }
  reverse(digits.begin(),digits.end());
}
void updateSet(set<int>&myset, ll n)
{
	vi arr;
	splitNumber(arr, n);
	for(int i =0 ;i < arr.size(); i++)
		myset.insert(arr[i]);
}
int main()
{
	int tc = 0;
	cin>>tc;
	for(int i = 1; i <= tc ; i++)
	{
		ll n =0;
		cin>>n;
		set<ll>visited;
		set<int>digits;
		ll count = 0;
		int ans = 0;
		bool bt = true;
		ll finalAns = 0;
		while(bt)
		{
				ll temp = n * (count + 1);
				if(visited.find(temp)!=visited.end())
				{
					bt =false;
					break;
				}
				ans = ans+1;
				count++;
				updateSet(digits,temp);
				visited.insert(temp);
				if(digits.size()==10)
				{
					finalAns = temp;
					break;
				}
		}
		if(!bt)
		cout<<"Case #"<<i<<": INSOMNIA"<<endl;
	else
		cout<<"Case #"<<i<<": "<<finalAns<<endl;
	}
	return 0;
}