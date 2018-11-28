#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T,n,k;
    cin >> T;
    bool found [10];
    for(int t=1;t<=T;t++) {
        cin >> n;
        k = n;
        memset(found,0,sizeof(found));
        bool br;
        for(int t=0;t<1000;t++) {
            int p = k;
            while(p) {
                found [p%10] = 1;
                p /= 10;
            }
            br = true;
            for(int j=0;j<10;j++)
                if(!found[j])
                    br = false;
            if(br)
                break;
            k += n;
        }
        cout << "Case #" << t << ": ";
        if(!br) {
            cout << "INSOMNIA" << endl;
        }
        else {
            cout << k << endl;
        }
    }
    return 0;
}
