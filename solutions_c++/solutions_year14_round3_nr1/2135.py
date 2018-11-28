#include <iostream>
#include <string>
using namespace std;
int gcd ( int a, int b )
{
  int c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}

int main()
{
    int T=0;
    cin>>T;
    for(int j=1; j<=T; j++) {
        string s;
        cin>>s;

        int i=0, n=0;
        while(s[i]!='/') {
            n = 10*n + s[i]-'0';
            i++;
        }
        i++;
        int d=0, len=s.length();
        while(i!=len) {
            d = 10*d + s[i]-'0';
            i++;
        }

        int f = gcd(n,d);
        n /= f;
        d /= f;
        // cout << n << d << endl;
        int ans=0;
        bool imp = false;
        while(d>1) {
            if(d%2) {
                imp = true;
                break;
            }
            else if(n<d) {
                ans++;
            }
            d /= 2;
        }

        if(imp)
            cout << "Case #" << j << ": " << "impossible" <<  endl;
        else
            cout << "Case #" << j << ": " << ans <<  endl;
    }
}
