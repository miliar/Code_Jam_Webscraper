#include <iostream>
#include <algorithm>

using namespace std;

pair<int, int> arr[1000];

int main()
{
  int T;
  cin >> T;
  for(int case_num = 1; case_num <= T; ++case_num) {
    int N;

	cin >> N;
    for(int i = 0; i < N; ++i) {
	  int z;
	  cin >> z;
	  arr[i] = make_pair(z, i);
	}

    sort( &arr[0], &arr[N] );

    int ans = 0;
    for(int i = 0, off = 0, sz = N - 1; i < N - 1; ++i) {
	  const int place = arr[i].second;
	  const int left = place - off;
	  const int right = sz - place;
	  if(left > right) {
	    ans += right;
		--sz;
		for(int j = i + 1; j < N; ++j) {
		  if(arr[j].second > place) arr[j].second--;
		}
	  } else {
	    ans += left;
		++off;
		for(int j = i + 1; j < N; ++j) {
		  if(arr[j].second < place) arr[j].second++;
		}
	  }
	}

	cout << "Case #" << case_num << ": " << ans << endl;
  }
  return 0;
}

