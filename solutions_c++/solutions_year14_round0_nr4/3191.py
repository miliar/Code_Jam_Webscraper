#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

#define N 1010

double sa[N];
double sb[N];

int main()
{
//    freopen("D:\\GCJ\\D-large.in","r",stdin);
//    freopen("D:\\GCJ\\D-large.txt","w",stdout);

    int T,n;
    cin >> T;
    for (int cas = 0; cas < T; cas++){
        cin >> n;
        for (int i=0; i< n; i++){
            cin >> sa[i];
        }
        for (int i=0; i< n; i++){
            cin >> sb[i];
        }
        sort(sa,sa+n);
        sort(sb,sb+n);
        int id = 0;
        int ans_b = 0;
        for (int i=0;i<n;i++){
            while(id<n&&sb[id]<sa[i]){
                id++;
            }
            if (id==n){
                ans_b = n-i;
                break;
            } else {
                id++;
            }
        }
        id = n-1;
        int ans_a = 0;
        bool all = true;
        for (int i=n-1;i>=0;i--){
            while(id>=0&&sb[id]>sa[i]){
                id--;
            }
            if (id<0){
                ans_a = n-i-1;
                all = false;
                break;
            } else {
                id--;
            }
        }
        if (all) ans_a = n;
        cout << "Case #"<<cas+1<<": "<<ans_a << " " << ans_b << endl;
    }
    return 0;
}
