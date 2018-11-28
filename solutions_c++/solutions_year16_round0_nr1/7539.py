#include <bits/stdc++.h>

using namespace std;

using LL = long long;
using ULL = unsigned long long;
#define vi vector<int>
#define vs vector<string>
#define vl vector<LL>
#define pb push_back
#define endl "\n"


bool seen[10];
ULL seen_count = 0;

void update1(ULL num) {
   assert(num <= 9);
   if (seen[num] == false) {
      seen[num] = true;
      seen_count++;
   }
}


void update(ULL num) {
   if (num <= 9) {
      update1(num);
   } else {
      while (num > 0) {
         ULL d = num % 10;
         num = num / 10;
         update1(d);
      }
   }
}

ULL solve(ULL input) {
   memset(seen, 0, sizeof(seen));
   seen_count = 0;
   ULL curr = input;
   update(curr);
   while (seen_count < 10) {
      curr += input;
      assert(curr > input);
      update(curr);
   }
   return curr;
}


int main()
{
	ios_base::sync_with_stdio(false);
	ULL T = 0;
	cin >> T;
	for (ULL i = 1; i <= T; ++i) {
	   ULL input;
	   cin >> input;
	   if (input == 0)
	      cout << "Case #" << i << ": INSOMNIA" << endl;
	   else
	      cout << "Case #" << i << ": " << solve(input) << endl;
	}

	return 0;
}

