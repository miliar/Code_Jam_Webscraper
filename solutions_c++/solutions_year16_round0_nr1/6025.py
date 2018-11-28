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


set <int> dig;

void check(int num){
    while(num >0){
        dig.insert(num%10);
        num/=10;
    }
}

int main() {
	//ios_base::sync_with_stdio(false); cin.tie(0);
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	int t,n;
	cin >> t;


	forn(j,t){
        cin >> n;
        cout << "Case #" << j+1 << ": ";
        if(n == 0){
            cout << "INSOMNIA" << endl;
            continue;
        }
        dig.clear();
        int i = 0;
        while(si(dig) < 10 ){
            i++;
            check(n*i);
        }
        cout << n*i << endl;
	}


	return 0;
}
