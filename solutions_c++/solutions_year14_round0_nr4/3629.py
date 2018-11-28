#include<iostream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;

const double EPS = 10E-9;

int main () {

	int casos;
	cin >> casos;
	for (int t=1; t<=casos; t++) {

		int n;
		cin >> n;
		vector<double> a(n), b(n);
		vector<bool> used(n,false);
		
		for (int i=0; i<n; i++) cin >> a[i];
		for (int i=0; i<n; i++) cin >> b[i];
		
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());

//		for (int i=0; i<n; i++) cout << a[i] << " "; cout << endl;
//		for (int i=0; i<n; i++) cout << b[i] << " "; cout << endl;
		
		int s1 = 0;
		
		for (int i=0 ; i<n; i++) {
			bool found = false;
			for(int j=0; j<n && !found; j++) if(!used[j]) {
				if(a[i] < b[j] - EPS) {
					found = true;
					used[j] = true;
				}
			}
			if(!found) {
				s1 ++;
				for(int j=0; j<n && !found; j++) if(!used[j]) {
					used[j] = true;
					break;
				}
			}
		}

		int s2 = 0;
		int ab=0, ae=n-1, bb=0, be=n-1;
		while(ab <= ae){
			if(a[ab] < b[bb] - EPS) {
				ab++;
				be--;
			} else {
				s2++;
				ab++;
				bb++;
			}
		}
		cout << "Case #" << t << ": " << s2 << " "<< s1 << endl;
	}

	return 0;
}
