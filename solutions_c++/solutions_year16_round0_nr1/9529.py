#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

#define pb push_back
#define pf push_front
#define mp make_pair
#define sz(a) (int)a.size()
#define i128 __int128
#define INF 0x3f3f3f3f
// LLONG_MIN LLONG_MaX INT_MIN INT_MaX



int main(){
    int n;
    cin >> n;
    bool check[10];
    for(int i=1; i<=n; i++){
        bool flag = true;
        memset(check, 0, sizeof(check));
        int cnt = 1;
        int x;
        cin >> x;
        if(x == 0){
            cout << "Case #" << i << ": " << "INSOMNIA\n";
            continue;
        }
        int a;        
        while(1){
            flag = true;
            a = x * cnt;
            int temp = a;
            while(temp != 0){
                check[temp % 10] = true;
                temp /= 10;
            }
            for(int j=0; j<10; j++)
                if(!check[j])
                    flag = false;
            if(flag)
                break;
            cnt++;
        }
        cout << "Case #" << i << ": " << a << endl;    
    }
    return 0;
}