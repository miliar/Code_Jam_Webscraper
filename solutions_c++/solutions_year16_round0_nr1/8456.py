#include <bits/stdc++.h>

using namespace std;

#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),(a).end()
#define DEBUG(x) {cout<< #x <<" = " << x <<endl;}

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;

vector<bool> check;

bool ok(){
    for(int i = 0; i <= 9; ++i)
        if (!check[i])
            return false;
    return true;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    ios::sync_with_stdio(false);
    int test;
    cin>>test;
    int test_case = 1 ;
    while (test--){
        ll n;
        cin >> n;
        check.assign(11,false);
        if (n == 0)
            {
                cout << "Case #" << test_case << ": " <<  "INSOMNIA" << endl;
                test_case++;
                continue;
            }
        ll d = 1;
        while (1){
            ll tg = n * d;
            //DEBUG(tg);
            while (tg){
                check[tg%10] = true;
                tg/=10;
            }
            if (ok())
                {
                    cout<<"Case #"<< test_case <<": "<< n*d <<endl;
                    break;
                }
            else
                d++;
        }
        check.clear();
        test_case++;
    }

    return 0;
}
