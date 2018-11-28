#include <iostream>

using namespace std;

int main() {
    int T, max, sum, ans;
    string people;
    cin >> T;
    for(int cas = 1; cas <= T; cas++) {
        cin >> max >> people;
        sum = 0;
        ans = 0;
        for(int ix = 0; ix < people.size(); ix++) {
        	// cout << "\t" << sum << " " << ix << " " << ans << endl;
        	if(sum < ix && people[ix] != '0') {
        		ans += ix - sum;
        		sum += ix - sum;
        	}

        	sum += people[ix]-'0';
        }

        cout << "Case #" << cas << ": " << ans << endl;
    }

    return 0;	
}
