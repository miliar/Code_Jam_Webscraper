#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

vector<int> primes;

void init_primes() {
    const int N = 1e8;
    vector<bool> not_prime(N + 1, 0);
    
    for (long long i = 2; i <= N; ++i) {
        if (!not_prime[i]) {
            primes.push_back(i);
            for (long long j = i * 2; j <= N; j += i) {
                not_prime[j] = 1;
            }
        }
    }
}

int divisor(long long x) {
    for (long long i = 2; i * i <= x; ++i) {
        if (x % i == 0) {
            return i;
        }
    }
    
    return -1;
}

long long convert_to(long long x, int n) {
    long long a = 1;
    long long r = 0;
    for (int i = 0; i < 20; ++i) {
        if (x & (1 << i)) {
            r += a;
        }
        a *= n;
    }
    
    return r;
}

vector<int> proof(long long x) {
    vector<int> res;
    for (int n = 2; n <= 10; ++n) {
        long long c = convert_to(x, n);
        
        int div = divisor(c);
        if (div == -1) {
            return vector<int>();
        }
        res.push_back(div);
    }
    
    return res;
}

string str(long long x) {
    string s;
    bool start = 0;
    for (int i = 25; i >= 0; --i) {
        if (x & (1 << i) || start) {
            start = 1;
            s += '0' + ((x & (1 << i)) != 0);
        }
    }
    return s;
}

string c;

// rev / plus
int dp[105][105][2][2];

int get(int i, int j, int rev, int plus) {
    int& r = dp[i][j][rev][plus];
    
    if (r != -1) {
        return r;
    }

    if (i == j) {
        return r = ((c[i] == '+') != plus);
    }
    
    for (int z = i; z <= j; ++z) {
        if ((c[i] == '+') != plus) {
            break;
        }
        
        if (z == j) {
            return r = 0;
        }
    }
    
    r = 1e9;
    for (int z = i; z + 1 <= j; ++z) {
        r = min(r, 1 + get(i, z, rev^1, plus^1) 
                        + get(z + 1, j, rev^1, plus^1));
    }
    
    return r;
}

int solve(string s) {
    c = s;
    
    memset(dp, -1, sizeof(dp));
    
    return get(0, c.size() - 1, 0, 1);
}



int main(int argc, char **argv) {
    freopen("out.txt", "w", stdout);
    


    
    //init_primes();
    //cerr << "Primes: " << primes.size() << endl;
    
    int n = 16;
    
    cout << "Case #1:" << endl;
    
    
    int good = 0;
    
    for (int i = 0; i < (1 << (n-2)); ++i) {
        long long t = (i << 1);
        t |= (1 << 0);
        t |= (1 << (n-1));
        
        vector<int> res = proof(t);
        
        if (!res.empty()) {
            cout << str(t);
            for (int z = 0; z < res.size(); ++z) {
                cout << " " << res[z];// << "|" << convert_to(t, z + 2) << "|" << convert_to(t, z + 2) % res[z];
            }
            cout << endl;
            ++good;
        }
        
        if (good == 50) {
            return 0;
        }
    }
    
    return 0;
    
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int t; cin >> t;
    
    for (int test = 1; test <= t; ++test) {
        
        string x;
        cin >> x;
        
        int ans = solve(x);
        
        printf("Case #%d: ", test);
        fprintf(stderr, "Case #%d: ", test);

            cout << ans;
            cerr << ans;
        
        cout << endl;
        cerr << endl;
    }
        
	return 0;
}
