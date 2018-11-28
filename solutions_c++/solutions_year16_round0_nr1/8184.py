#include <bits/stdc++.h>
#define M 1000000007
#define LL long long int

using namespace std;

bool check(int visted[])
{
    bool ch = true;

    for (int i = 0; i < 10; i++) {
        if (visted[i] == 0) {
            ch = false;
            break;
        }
    }

    return ch;
}

int main() {
    int t, n, i, temp;

    freopen( "A-large.in", "r", stdin );
	freopen( "output1.txt", "w", stdout );

    scanf("%d", &t);
    int j = 0;

    while (j < t) {
        j++;
        scanf("%d", &n);
        int ans;
        map <int, int> m;
        int visted[10];
        int k = n;


        for (i = 0; i < 10; i++) visted[i] = 0;
        bool flag = true;


        while (1) {
            temp = n;
            //cout<<temp<<endl;
            if (m[n] == 1) {
                cout<<"Case #"<<j<<": INSOMNIA"<<endl;
                flag = false;
                break;
            }

            m[n] = 1;

            while (temp > 0) {
                visted[temp%10] = 1;
                temp = temp / 10;
            }

            if (check(visted) == true) {
                ans = n;
                break;
            }

            n += k;
        }

        if (flag == true) cout<<"Case #"<<j<<": "<<ans<<endl;
    }
}
