#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <vector>
#include <iterator>
#include <set>
#include <bitset>
#include <ctime>
#include <iomanip>
#include <map>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int test=1; test<=t; test++) {
		int n;
		cin>>n;
		double a[n], b[n];
		for(int i=0; i<n; i++) {
			cin>>a[i];
		}
		for(int i=0; i<n; i++) {
			cin>>b[i];
		}
		bool c[n];
		memset(c, false, sizeof c);
		stable_sort(a, a+n);
		stable_sort(b, b+n);
		/*for(int i=0; i<n; i++)
			cout<<a[i]<<" ";
		cout<<endl;
		for(int i=0; i<n; i++)
			cout<<b[i]<<" ";
		cout<<endl;*/
		int wr = 0, dw = 0;
		for(int i=n-1, j=n-1; j>=0; ) {
			if(a[i] < b[j])
				j--;
			else {
				j--;
				i--;
				wr++;
			}
		}
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(!c[j] && a[i] < b[j]) {
					c[j] = true;
					dw++;
					break;
				}
			}
		}
		cout<<"Case #"<<test<<": ";
		cout<<wr<<" "<<n-dw<<"\n";
	}
	return 0;
}