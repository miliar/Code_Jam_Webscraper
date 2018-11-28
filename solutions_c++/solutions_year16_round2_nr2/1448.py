#include <iostream>
#include <string>

using namespace std;

int power(int x)
{
    int ans = 1;
    for (int i = 0; i < x; ++i ) 
        ans *= 10;
    return ans;
}

int abs(int x)
{
    return x>0? x: -x;
}


bool check(int a, string ac) {

    for (int i = ac.size()-1; i >= 0; --i) {
        if ( ac[i] != '?') {
            if (a%10 != (ac[i]-'0'))
                return false;
        }
        a /= 10;
    }
    
    return true;
}

void mp(int x, int s)
{
    if (s==1) {
        cout << x;
    }
    else if(s == 2) {
        if (x <= 9) {
            cout << '0'<<x;
        }
        else
            cout<<x;
    }
    else if (s == 3) {
        if (x > 99) 
            cout << x;
        else if (x > 9 )
            cout << '0' << x;
        else 
            cout << "00"<<x;
    }
}
int main()
{
    int t; cin>>t;
    int tc=0;
    while (t--) {
        ++tc;
        string c, j;
        cin>>c>>j;

        int mindiff = 10000;
        int cans , jans;
        int bound = power(c.size());
        for (int a = 0; a < bound; ++a) {
            for (int b = 0; b < bound; ++b) {
                if ( check(a, c) && check(b, j) ) {
                    if (abs(a-b) < mindiff) {
                        mindiff= abs(a-b);
                        cans = a; jans = b;
                    }
                }
            }
        }
        cout << "Case #"<<tc<<": ";
        mp(cans, c.size());
        cout<< " ";
        mp(jans, c.size());
        cout<<endl;
    }
    return 0;
}
