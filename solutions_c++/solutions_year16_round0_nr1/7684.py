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
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

	ios_base::sync_with_stdio(false); 
	cin.tie(0);

    int nc;
    cin >> nc;

    forn(c, nc) {
        tint n;
        cin >> n;
        
        cout << "Case #" << c+1 << ": ";
        if (n == 0)
            cout << "INSOMNIA" << endl;
        else {
            vector<bool> seen(10, false);
            bool end = false;
            tint act = 0;
            while (!end) {
                act += n;
                
                tint temp = act;
                while (temp > 0) {
                    seen[temp%10] = true;
                    temp /= 10;
                } 
                
                bool all = true;
                forn(i, 10)
                    if (!seen[i])
                        all = false;

                if (all) end = true;
            }
            cout << act << endl; 
        }
    }

	return 0;
}
