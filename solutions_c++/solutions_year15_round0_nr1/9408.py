#include<iostream>
using namespace std;

int main()
{
    string s;
    int t, n, x, sum_till_now, ans;
    cin >> t;

    for(int k = 1; k <= t; k++) {
	cin >> n;
	cin >> s;

	sum_till_now = s[0]-'0';
	ans = 0;

	for(int i = 1; i <= n; i++) {
	    x = s[i] - '0';

	    if(i > sum_till_now) {
	    	ans +=  i - sum_till_now;
		sum_till_now += i - sum_till_now;
	    }
	    sum_till_now += s[i] - '0';
	}

	cout << "Case #" << k << ": " << ans << endl;
    }

    return 0;
}
