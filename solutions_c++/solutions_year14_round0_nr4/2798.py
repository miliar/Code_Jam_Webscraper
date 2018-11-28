#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <vector>

using namespace std;

int main()
{
	// freopen("D-large.in","r",stdin);
	// freopen("4.out","w",stdout);
	int T;
	int n;
	double tmp;
	vector<double> a,b;
	cin >> T;
	for (int tt = 0; tt<T; tt++){
		int ans1 = 0,ans2 = 0;
		a.clear();
		b.clear();
		cin >> n;
		for (int i = 0; i < n; i++){
			cin >> tmp;
			a.push_back(tmp);
		}
		for (int i = 0; i < n; i++){
			cin >> tmp;
			b.push_back(tmp);
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());

		bool fb[1000] = {false};
		for (int i = a.size() - 1; i >= 0; i--){
			bool flag = false;			
			for (int j = b.size() - 1; j >= 0; j--){
				if ((a[i] > b[j]) && !fb[j]){
					flag = true;
					fb[j] = true;
					break;
				}
			}
			if (flag) ans1++;
		}

		bool fb1[1000] = {false};
		for (int i = 0; i < a.size(); i++){
			bool flag = false;			
			for (int j = 0; j < b.size(); j++){
				if ((b[j] > a[i]) && !fb1[j]){
					flag = true;
					fb1[j] = true;
					break;
				}
			}
			if (!flag) ans2++;
		}

		//--------------------- print -----------------
		cout << "Case #" << tt+1 << ": ";
		cout << ans1 << ' ' << ans2;
		cout << endl;
	}
	
}