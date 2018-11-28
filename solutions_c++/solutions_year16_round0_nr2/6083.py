#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<int(n);i++)
#define forsn(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define dforsn(i,s,n) for(int i=(int)(n-1);i>=int(s);i--)
#define si(a) ((int)(a).size())
#define pb push_back
#define mp make_pair
//#define endl '\n'
#define all(a) a.begin(),a.end()
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long int tint;

int main() {
	//ios_base::sync_with_stdio(false); cin.tie(0);
    freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	int t;
	string s;
	cin >> t;

	forn(j,t){
        cin >> s;
        int res = 0;
        for(int i = 0;i+1<si(s);i++){
            if(s[i] != s[i+1])res++;
        }
        if(s[si(s)-1]=='-')res++;
        cout << "Case #" << j+1 <<": " << res << endl;
	}


	return 0;
}
