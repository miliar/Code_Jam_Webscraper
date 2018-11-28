#include <bits/stdc++.h>

using namespace std;

long long int n;

vector< pair< long long int, vector <long long int> > > found;

vector<int> nb (16,0);

long long int determinediv (long long int num) {
    for(long long int i=2;i<=ceil(sqrt(num));i++) {
        if(num%i == 0) {
            return i;
        }
    }
    return -1;
}

void solve (int p, int b) {
    if(found.size() == 50) {
        return;
    }
    if(p == 15) {
        bool allnonprime = true;
        vector<long long int> div;
        for(int base=2;base<=10;base++) {
            n=0;
            for(int i=15;i>=0;i--) {
                long long kk = 1;
                for(int k=0;k<i;k++) {
                    kk *= base;
                }
                n += kk * nb[i];
            }
            long long int divisor = determinediv(n);
            if(divisor == -1) {
                allnonprime = false;
                break;
            }
            else {
                div.push_back(divisor);
            }
        }
        if(allnonprime) {
            found.push_back(make_pair(n, div));
        }
        return;
    }
    nb[p] = b;
    solve(p+1, 0);
    if(p+1 != 15) {
        solve(p+1, 1);
    }
}

int main()
{
    nb[0] = nb[15] = 1;
    solve(0,1);
    cout << "Case #1:" << endl;
    for(int i=0;i<found.size();i++) {
        cout << found[i].first;
        for(int j=0;j<(found[i].second).size();j++) {
            cout << " " << (found[i].second)[j];
        }
        cout << endl;
    }
    return 0;
}
