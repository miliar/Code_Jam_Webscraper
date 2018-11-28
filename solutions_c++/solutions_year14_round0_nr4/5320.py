#include <iostream>
#include <algorithm>
#define maxn 1010
#define maxvalue 12
#define exp 1e-12
using namespace std;


int n;
double a[maxn];
double b[maxn];



void solve(int num){
    int i, j;
    int resa = 0, resb = 0;
    sort(a, a+n);
    sort(b, b+n);
    int lastpos=n-1;
    for(i = n -1;i >= 0;i--){
        for(j = lastpos;j>=0;j--){
            if(a[i] > b[j]){
                resb++;
                lastpos = j-1;
                break;
            }
        }
    }
    lastpos = n - 1;
    for(i = n - 1;i >= 0;i--){
        for(j = lastpos;j>=0;j--){
            if(b[i] > a[j]){
                resa++;
                lastpos = j-1;
                break;
            }
        }
    }
    cout << "Case #" << num << ": " << resb << " " << (n - resa) << endl;
}

int main()
{
    int t;
    int tt=0;
    int i;
    cin >> t;
    while(t--){
        cin >> n;
        for(i = 0;i < n;i++){
            cin >> a[i];
        }
        for(i = 0;i < n;i++){
            cin >> b[i];
        }

        solve(++tt);
    }

    return 0;
}
