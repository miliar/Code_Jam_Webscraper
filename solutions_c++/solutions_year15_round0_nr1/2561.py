#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t){
		int smax, standing=0, toAdd=0;
		cin >> smax;
		string s;
		cin >> s;
		standing = s[0] - '0';
		for(int i = 1; i < s.size(); ++i){
			int num = s[i] - '0';
			if(num != 0){
				if(standing < i){
					toAdd += i - standing;
					standing +=  (i - standing);
				}
				standing += num;
			}
		}
		cout << "Case #" << t << ": " << toAdd << endl;
	}
	return 0;
}