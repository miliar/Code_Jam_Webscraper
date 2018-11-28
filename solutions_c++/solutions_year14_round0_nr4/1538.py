#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;
typedef set < double > sd;

int war(sd  her, sd him) 
{
	sd::iterator it1, it2;
	int result = her.size();

	for(it1 = her.begin(); it1 != her.end(); ++it1) {

		it2 = him.upper_bound(*it1);
		if(it2 != him.end()) {
			him.erase(it2);
			result--;
		}
	}

	return result;
}

int dwar(sd  her, sd him) 
{
	sd::iterator it1, it2;
	int result = 0;

	for(it1 = her.begin(); it1 != her.end(); ++it1) {
		it2 = him.lower_bound(*it1);

		if(it2 != him.end()) {
			if(it2 != him.begin())
				--it2;

			if(*it1 > *it2) {
				him.erase(it2);
				result++;
			}

			 else {	
				 it2 = him.end();
				--it2;
				him.erase(it2);
			}
		}

		else {	
			--it2;
			result++;
			him.erase(it2);
		}
	}

	return result;
}

int main ( int argc, char ** argv ) 
{
	ios::sync_with_stdio(NULL);
	
	int t, n;
	double b;
	sd her, him;

	cin >> t;
	for(int x = 1; x <= t; x++) {
		cin >> n;

		for(int i = 0; i < n; i++)
			cin >> b , her.insert(b);

		for(int i = 0; i < n; i++)
			cin >> b , him.insert(b);

		int nwar = war(her, him);
		int ndwar = dwar(her, him);

		cout << "Case #" << x << ": " << ndwar << " " << nwar << '\n';

		her.clear();
		him.clear();
	}

	return 0;
}
