#include <iostream>
#include <vector>
#include <map>

using namespace std;

string s, ss;
long long t, l;
long long x;
string dp[100000];

map<string, string> mp;

long long min(long long a, long long b) {
    if (a < b)
        return a;
    return b;
}

string divi(string a, string b) {
	if (b[1] == '1') {
		if (a[0] != b[0])
			a[0] = '-';
		else
			a[0] = '+';
		return a;
	}
	if (b[0] == '-')
		b[0] = '+';
	else
		b[0] = '-';
	
	string c = "+1", res = "  ";
	res[0] = b[1];
	res[1] = a[1];
	
	res = mp[res];
	c[1] = res[1];
	if (a[0] != b[0])
		a[0] = '-';
	else
		a[0] = '+';
	if (a[0] != res[0])
		c[0] = '-';
	return c;
}

string multi(string a, string b) {
    string c = "+1", res = "  ";
    res[0] = b[1];
    res[1] = a[1];
    
    res = mp[res];
    c[1] = res[1];
    if (a[0] != b[0])
        a[0] = '-';
    else
        a[0] = '+';
    if (a[0] != res[0])
        c[0] = '-';
    return c;
}

string pw(string a, long long n) {
    if (n == 1)
        return a;
    if (n == 0)
        return "+1";
    if (n%2) {
        string c = pw(a, n/2);
        return multi(a, multi(c, c));
    } else {
        string c = pw(a, n/2);
        return multi(c, c);
    }
}

int main() {
	
	mp[string("11")] = "+1";
	mp[string("1i")] = "+i";
	mp[string("1j")] = "+j";
	mp[string("1k")] = "+k";
	
	mp[string("i1")] = "+i";
	mp[string("ii")] = "-1";
	mp[string("ij")] = "+k";
	mp[string("ik")] = "-j";
	
	mp[string("j1")] = "+j";
	mp[string("ji")] = "-k";
	mp[string("jj")] = "-1";
	mp[string("jk")] = "+i";
	
	mp[string("k1")] = "+k";
	mp[string("ki")] = "+j";
	mp[string("kj")] = "-i";
	mp[string("kk")] = "-1";
	
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #"<<i <<": ";
		cin >> l >> x;
		cin >> ss;
		s = ss;
		for (int j = 0; j < min(4, x-1); j++)
			s += ss;
		//cout << s << endl;
		
		dp[0] = "+";
		dp[0] += s[0];
		//cout << dp[0]<<endl;
		for (int j = 1; j < s.length(); j++) {
			dp[j] = "+1";
			string res = "  ";
			res[0] = dp[j-1][1];
			res[1] = s[j];
			//cout << res << " ";
			res = mp[res];
			//cout << res << " ";
			if (dp[j-1][0] != res[0])
				dp[j][0] = '-';
			dp[j][1] = res[1];
			//cout << dp[j] << endl;
		}
        
        
		if (pw(dp[l-1], x) != "-1") {
			cout << "NO"<<endl;
			continue;
		}
		
		//find i
		long long first_i = -1;
		long long last_k = -1;
		for (int j = 0; j < s.length(); j++) {
			if (dp[j] == "+i") {
				first_i = j;
				break;
			
			}
		}
		for (int j = s.length()-2; j >= 0; j--) {
			if (divi(dp[s.length()-1], dp[j]) == "+k") {
				last_k = j+1;
				break;
			
			}
		}
		//cout << first_i << " " << last_k << endl;
        if (x-1 <= 4) {
            if (first_i != -1 && last_k != -1) {
                if (first_i <last_k-1)
                    cout << "YES"<<endl;
                else
                    cout << "NO"<<endl;
            } else
                cout << "NO"<<endl;
        } else {
            if (first_i != -1 && last_k != -1) {
                if (first_i <last_k-1+ (l*(x-4)))
                    cout << "YES"<<endl;
                else
                    cout << "NO"<<endl;
            } else
                cout << "NO"<<endl;
    }

        
        
	}
	return 0;
}