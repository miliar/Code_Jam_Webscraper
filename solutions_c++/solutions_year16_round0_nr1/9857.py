#include <iostream>
#include <stdio.h>
#include <map>
#include <set>
using namespace std;

void solve(long long n) {
    int cnt = 1;
    map<int, bool> mm;
    while (1) {
        long long m = n * cnt;
        int i = 1;
        while (i) {
            if (m == 0 && i != 1) {
                break;
            }
            int a = m % 10;
            m /= 10;
            mm[a] = true;
            i++;
        }
        if (mm.size() == 10) {
            cout<<n * cnt<<endl;
            return;
        }
        cnt++;
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin>>T;
    int t = 0;
    while (t < T) {
        t++;
        printf("Case #%d: ", t);
        long long n;
        cin>>n;
        if (n == 0) {
            cout<<"INSOMNIA\n";
        }
        else {
            solve(n);
        }
    }
    return 0;
}