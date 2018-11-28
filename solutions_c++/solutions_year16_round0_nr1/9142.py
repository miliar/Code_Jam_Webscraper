#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, n, i;
    freopen("in1.in","r",stdin);
    freopen("output2.out","w",stdout);

    cin>>t;

    for (int x = 1; x <= t; x++) {
        cin>>n;
        int visted[10];
        map <int, int> m;
        int temp;
        bool ch = false;
        int k = n;

        //for (int j = 0; j < 10; j++) visted[j] = 0;
        memset(visted, 0, sizeof(visted));

        while (true) {
            temp = n;

            if (m[n] == 1) {
                cout<<"Case #"<<x<<": "<<"INSOMNIA"<<endl;
                //ch = true;
                break;
            }

            m[n] = 1;

            while (temp) {
                int ind = temp % 10;
                visted[ind] = 1;
                temp /= 10;
            }

            bool flag = true;

            for (i = 0; i < 10; i++) {
                if (visted[i] == 0) flag = false;
            }

            if (flag == true) {
                cout<<"Case #"<<x<<": "<<n<<endl;
                break;
            }

            n = n + k;
        }
    }

    return 0;
}
