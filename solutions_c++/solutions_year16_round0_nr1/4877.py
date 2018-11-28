#include<bits/stdc++.h>
using namespace std;
int b[10];
int main()
{
    freopen("sample.txt", "r", stdin);
    freopen("Count_Sheep_out.txt", "w", stdout);
    int t;
    cin >> t;
    int test = 1;
    while(test <= t) {
        memset(b,0,sizeof(b));
        int n;
        cin >> n;
        long long val;
        int count = 0;
        int ans = 1;
        if(n == 0) {
            cout << "Case #" << test << ":" << " " << "INSOMNIA" << endl;
        }
        else {
        while(count != 10) {
            val = ans*n;
            //cout << val << " ";
            while(val) {
                b[val%10]=1;
                val = val/10;
            }
            count = 0;
            for(int i=0;i<10;i++) {
                count += b[i];
            }
            ans++;
        }
         cout << "Case #" << test << ":" << " " << (long long)(ans-1)*n << endl;
        }
        test++;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
