#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<int(n);i++)
#define forsn(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define dforsn(i,s,n) for(int i=(int)(n-1);i>=int(s);i--)
#define si(a) ((int)(a).size())
#define pb push_back
#define mp make_pair
#define endl '\n'
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long int tint;

int main() {
	ios_base::sync_with_stdio(false); 
	cin.tie(0);

    int nc;
    cin >> nc;

    forsn(c, 1, nc+1) {
        string s;
        cin >> s;

        int n = si(s), cnt = 0;
        forn(i, n) {
            while (i+1 < n && s[i+1] == s[i])
               i++;
            if (i == n-1 && s[i] == '+')
                break; 
            else
                cnt++;
        }

        cout << "Case #" << c << ": " << cnt << endl;
    }

	return 0;
}
