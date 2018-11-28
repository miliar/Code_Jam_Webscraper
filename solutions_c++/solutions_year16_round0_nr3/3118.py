#include <iostream>

using namespace std;
unsigned long long int joker[16];
int main()
{
    unsigned long long int t;
    cin >> t;
    freopen("a.out","w",stdout);
    for (unsigned long long int xdr=0;xdr<t;xdr++)
    {
    cout << "Case #1:" << endl;
        unsigned long long int n,j;
        cin >> n >> j;
        unsigned long long int ret=0;
        for (unsigned long long int i=32769;i<=65535&&ret<50;i+=2)
        {
            unsigned long long int l=i;
            string s="";
            for (unsigned long long int x=0;x<16;x++)
            {
                if (l%2==0){s='0'+s;}else{s='1'+s;}
                l/=2;
            }

            for (unsigned long long int base=2;base<=10;base++)
            {
                unsigned long long int now=0;
                unsigned long long int yh=1;
                for (int p=15;p>=0;p--)
                {
                    now+=yh*(s[p]=='1'?1:0);
                    yh*=base;
                }

                for (unsigned long long int p=2;p*p<=now;p++)
                {
                    if (now%p==0){joker[base]=p;goto yu;}
                }
                goto ui;
                yu:
                bool perre;
            }
            ret++;
            cout << s << ' ' << joker[2] << ' ' << joker[3] << ' ' <<joker[4] << ' ' <<joker[5] << ' ' <<joker[6] << ' ' <<joker[7] << ' ' <<joker[8] << ' ' <<joker[9] << ' ' <<joker[10] << endl;
            ui:
            bool p;
        }
    }
    return 0;
}
