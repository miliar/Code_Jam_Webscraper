#include <bits/stdc++.h>
#define s(x) scanf("%d", &x)
using namespace std;

int main()
{
    int t;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    s(t);
    int cas = 1;
    while(t--) {


        int ppl = 0, standing = 0, smax, i;
        string str;

        s(smax);
        cin >> str;

        for(i = 0; i < str.size(); i++) {
            str[i] = str[i] - '0';
            if(standing >= i) {
                standing += str[i];
            }
            else {
                ppl = ppl + (i - standing);
                standing = str[i] + i;
            }
        }

        cout <<"Case #"<<cas++<<": "<<ppl<<endl;
    }
}
