#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int T, N;
  cin >> T;
  for (int t=1;t<=T;t++) {
		cin >> N;
		vector<pair<int,int> > A;
		for (int i=0;i<N;i++) {
			int a;
			cin >> a;
			A.push_back(make_pair(a,i));
		}

		sort(A.begin(),A.end());
		vector<int> B(A.size(),0);
		for (int i=0;i<A.size();i++) {
			B[i]=i;
		}

		int start=0, end=A.size();
		int ans=0;
		for (int i=0;i<A.size();i++) {
			//for (int j=0;j<A.size();j++) cout << A[j].second << " ";
			//cout << endl;
			int index = B[A[i].second];
//cout << index << " - " << ans << " (" << start << "," << end << ")" << endl;
			if (index-start < end-1-index) {
				ans += index-start;
				start++;
				for (int j=0;j<A.size();j++) if (B[j]<index) B[j]++;
			}
			else {
				ans += (end-1)-index;
				for (int j=0;j<A.size();j++) if (B[j]>index) B[j]--;
				end--;
			}
		}

		
		printf("Case #%d: %d",t,ans);
		cout << endl;
	}

  return 0;
}
