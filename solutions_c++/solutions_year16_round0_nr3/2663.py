#include <bits/stdc++.h>

#define cout fout
#define MAXN 14

using namespace std;

typedef long long ll;

ofstream fout("C-small-attempt0.out");

int T;
int N, J;
ll powers[11][MAXN];
vector < string > ans;
string nowNum;
vector < int > tempDivisors;
vector < vector < int > > divisors;

int isPrime(ll x) {
    ll limit = sqrt(x);
    for (int i=3; i<=limit; i++)
        if (x%i == 0) return i;
    return -1;
}

ll toBase(int base) {
    ll retVal = 0LL;
    for (int i=0; i<nowNum.size(); i++) {
        retVal *= (ll)base;
        retVal += (ll)(nowNum[i]-'0');
    }
    return retVal;
}

bool isOK() {
    for (int i=2; i<=10; i++) {
        ll tempNum = toBase(i);
        tempDivisors[i-2] = isPrime(tempNum);
    }
    for (int i=2; i<=10; i++)
        if (tempDivisors[i-2] == -1)
            return false;
    return true;
}

int main()
{
    cin >> T >> N >> J;

    for (int i=2; i<=10; i++)
        tempDivisors.push_back(-1);
    for (int i=0; i<16; i++)
        nowNum += '1';

    for (int i=0; i<(1 << MAXN) && ans.size()<J; i++) {
        nowNum[0] = '1';
        for (int j=0; j<MAXN; j++) {
            if (i&(1 << j)) nowNum[j+1] = '1';
            else nowNum[j+1] = '0';
        }
        nowNum[MAXN+1] = '1';

        if (isOK()) {
            ans.push_back(nowNum);
            divisors.push_back(tempDivisors);
        }
    }

    cout << "Case #1: \n";
    for (int i=0; i<J; i++) {
        cout << ans[i] << " ";
        for (int j=2; j<=10; j++)
            cout << divisors[i][j-2] << " ";
        cout << "\n";
    }

    return 0;
}
