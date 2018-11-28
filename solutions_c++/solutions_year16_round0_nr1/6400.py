#include <iostream>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
#include <iomanip>
#include <map>

using namespace std;

#define mp make_pair
#define pb push_back

typedef long long ll;


int main(){

  int t;
  ll n, n2;

  string pancakes;
  cin >> t;

  for (int i = 1; i <= t; ++i)
  {
    cin >> n;

    if(n == 0){
      cout << "Case #" << i << ": " << "INSOMNIA" << "\n";
      continue;
    }

    vector<int> nums(10, 0);
    int so_far = 0;

    int x = 1;
    while(so_far < 10){
      n2 = n*x;

      while(n2 > 0){
        ll res = n2%10;
        n2/=10;
        if(nums[res] == 0) so_far++;
        nums[res]++;

      }
      x++;
    }


    cout << "Case #" << i << ": " << n*(x-1) << "\n";
  }

  return 0;
}
