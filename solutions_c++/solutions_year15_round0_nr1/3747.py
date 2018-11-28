#include<bits/stdc++.h>
using namespace std;

int main() {
    int i, j, k, n;   char str[1005];
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    cin>>n;
    for(int run = 1; run <= n;   run++) {
        cin>>k>>str;

        int count = 0;  int hold = str[0] - '0';
        for(i=1;    str[i]!=0;  i++) {
            if(hold < i) {
                int inc = (i - hold);
                count += inc;
                hold += (str[i] - '0' + inc);
            }
            else {
                hold += (str[i] - '0');
            }
        }

        cout<<"Case #"<<run<<": "<<count<<endl;
    }

    return 0;
}
