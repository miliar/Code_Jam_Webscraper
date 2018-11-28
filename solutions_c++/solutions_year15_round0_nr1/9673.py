#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <stdio.h>

using namespace std;

int main()
{

	freopen("A-small-attempt1.in","r",stdin);
   freopen("output.txt","w",stdout);


	int t;
	cin >> t;
	//cout << t << endl;
	int d = 0;
	while (t--) {

		
		
	//	cout << "eaf" << endl;
		int n;
		cin >> n;
		string s;
		cin >> s;
		int min_count = s[0] -48;
		int ans = 0;
		for ( int i = 1; i < s.size();i++) {

				int x = s[i] - 48;
				int num_require = i;

				if ( (min_count < num_require ) && x != 0) {
					ans += num_require - min_count;
					min_count += num_require + x;
				}
				else {
					min_count += x;
				}



		}
		d += 1;
		cout << "Case #"<<d << ": "<<ans << endl;

	}
	return 0;


}