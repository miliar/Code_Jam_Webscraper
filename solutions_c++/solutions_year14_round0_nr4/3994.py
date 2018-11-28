#include <bits/stdc++.h>
using namespace std;

int main()
{
      int testCases;
      cin >> testCases;
      for (int testNumber = 1; testNumber <= testCases; ++testNumber)
      {
	    cout << "Case #" << testNumber << ": ";
	    int N, tmp;
	    cin >> N;
	    vector <int> Naomi (N), Ken (N);
	    for (int i = 0; i < N; ++i)
		  scanf ("%d.%d", &tmp, &Naomi[i]);
	    for (int i = 0; i < N; ++i)
		  scanf ("%d.%d", &tmp, &Ken[i]);
	    sort (Naomi.begin(), Naomi.end());
	    sort (Ken.begin(), Ken.end());

	    int j = N - 1, war = N;
	    for (int i = N - 1; i >= 0; --i) {
		  while (j >= 0 && Ken[i] < Naomi[j])
			j --;
		  if (j >= 0) {
			war --;
			j -= 1;
		  }
	    }
	    int dwar = 0;
	    j = 0;
	    for (int i = 0; i < N; ++i) {
		  while (j < N && Ken[i] > Naomi[j])
			j ++;
		  if (j < N) {
			dwar ++;
			j ++;
		  }
	    }
	    cout << dwar << " " << war << endl;
      }
      return 0;
}

