#include <cmath>
#include <climits>
#include <queue>
#include <vector>
#include <unordered_map>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	long long int t, n, p = 1, seen_all;
	unordered_map<long long int, int> mp;
	string inp;
	cin >> t;
	while(t--)
	{
		seen_all = 0;
		mp.clear();
		cin >> n;
		if (n==0) {
			cout << "Case #"<<p<<": INSOMNIA"<<endl;
			++p;
			continue;
		} 
		long long int k = 1;
		while(seen_all < 10) {
			long long int temp = k*n;
			//cout << temp << " " << seen_all << endl;
			while (temp > 0) {
				if (mp[temp%10] == 0) {
					seen_all++;
					mp[temp%10] = 1;
				}
				temp/=10;
			}
			k++;
		}
		cout << "Case #"<<p<<": "<<(k-1)*n<<endl;
		++p;
	}	
	return 0;
}
