#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;

int main ()
{
  int T;
  cin >> T;
  for(int t = 0; t < T; t++) {
    int N;
    cin >> N;
    deque<double> nums1(N), nums2(N);
    for(int i = 0; i < N; i++)
      cin >> nums1[i];
    for(int i = 0; i < N; i++)
      cin >> nums2[i];
    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());
    reverse(nums1.begin(), nums1.end());
    reverse(nums2.begin(), nums2.end());
    int q1 = 0, q2 = 0;
    vector<bool> used(N, false);
    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++) {
        // force player 2 to play his highest
        if (nums1[j] < nums2[i] && !used[j]) {
          used[j] = true;
          break;
        }
      }
    }
    for(int i = 0; i < N; i++)
      if (!used[i])
        q2++;

    int k = 0;
    reverse(nums1.begin(), nums1.end());
    reverse(nums2.begin(), nums2.end());
    while (nums1.size() > 0) {
      // check if all of nums2 > nums1
      bool done = true;
      for(int i = 0; i < int(nums1.size()); i++) {
        if (nums2[i] > nums1[i]) {
          done = false;
          break;
        }
      }
      if (done) {
        q1 = N-k;
        break;
      }
      k++;
      nums1.erase(nums1.begin());
      nums2.erase(nums2.begin()+nums2.size()-1);
    }
    cout << "Case #" << t+1 << ": " << q1 << " " << q2 << endl;
  }
}
