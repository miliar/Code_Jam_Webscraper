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
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
#include <set>

using namespace std;

typedef long long int ll;

bool isPalindrome(ll num) {
  int n, digit, rev = 0;
  n = num;
  do
  {
    digit = num%10;
    rev = (rev*10) + digit;
    num = num/10;
  } while (num!=0);
  return (n == rev);
}

vector<int> counts;
map<ll, bool> is_palindrome;
map<ll, bool> is_good;
vector<ll> palindromes;
int total = 0;
void gen(string num,int dig,int of)
{
  int i=0;
  if(of<=dig/2&&dig%2 || of<dig/2&&!(dig%2))
  {
    for(int j=0;j<=9;j++)
    {
      num[i+of]=num[dig-1-of]=j+'0';
      gen(num,dig,of+1);
      if(num[0]>'0' && (of==dig/2-1&&!(dig%2) || of==dig/2&&dig%2)) {
        ll number = atoll(&num[0]);
        palindromes.push_back(number);
        is_palindrome[number] = true;
        counts.push_back(number);
      }
    }
  }
}

int main() {
	int t;
  	scanf("%d", &t);

  	string a="00000000000";
    for(int i = 0; i < 8; i++)
    {
        a[i+1]='\0';
        gen(a,i,0);
    }

    vector<ll> good_ones;
    for (int i = 0; i < palindromes.size(); i++) {
      ll n = palindromes[i];
      if (isPalindrome(n * n)) {
        good_ones.push_back(n * n);
      }
    }

	for(int c = 1; c <= t; c++) {
		int cnt = 0;
		ll a, b;
		scanf("%lld %lld", &a, &b);

    int res = 0;
    for (int i = 0; i < good_ones.size(); i++) {
      ll n = good_ones[i];
      if (n >= a && n <= b) {
        res++;
      }
    }

		printf("Case #%d: %d\n", c, res);
	}
	return 0;
}
