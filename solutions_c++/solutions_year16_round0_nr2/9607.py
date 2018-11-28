#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

map<string, int> memo;

int br_get(string s) {
    
    queue<string> q;
    
    q.push(s);
    memo.clear();
    memo[s] = 0;
    
    while(!q.empty()) {
        s = q.front();
        //cerr << s << "@" << memo[s] << endl;
        int dist = memo[s];
        q.pop();
        
        for (int i = 0; i < s.size(); ++i) {
            
            if (s[i] == '+') {
                s[i] = '-';
            } else {
                s[i] = '+';
            }
            
            string t = s;
            reverse(t.begin(), t.begin() + i + 1);
            
            if (!memo.count(t)) {
                memo[t] = dist + 1;
                q.push(t);
            }
        } 
    }
    
    string t = "";
    for (int i = 0; i < s.size(); ++i) {
        t += "+";
    }
    return memo[t];
}

string c;

// rev / plus
int dp[105][105][2];

int get(int i, int j, int plus) {
    int& r = dp[i][j][plus];
    
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
        
        
        r = min(r, 1 + get(i, z, plus^1) 
                        + get(z + 1, j,  plus^1));
    }
    
    return r;
}

int solve(string s) {
    c = s;
    
    memset(dp, -1, sizeof(dp));
    
    return get(0, c.size() - 1, 1);
}



int main(int argc, char **argv) {
      
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int t; cin >> t;
    
    for (int test = 1; test <= t; ++test) {
        
        string x;
        cin >> x;
        
        memo.clear();
        
        int ans = br_get(x);
        
        cerr << endl;
        cerr << x << endl;
        
        printf("Case #%d: ", test);
        fprintf(stderr, "Case #%d: ", test);

            cout << ans;
            cerr << ans;
        
        cout << endl;
        cerr << endl;
    }
        
	return 0;
}
