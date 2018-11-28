#include <bits/stdc++.h>
using namespace std;

int a[10];

int main(){
    int t;
    cin >> t;
    int ca = 0;
    while(t--){
        ca++;
        int n;
        cin >> n;
        for(int i = 0; i <= 9; i++) a[i] = 0;
        if(n == 0) cout << "Case " << "#" << ca << ": "<< "INSOMNIA" << endl;
        else{
            int count = 0;
            int l = 1;
            long long ans = 0;
            while(count < 10){
                int x = n*l;
                ans = x;
                while(x > 0){
                    if(a[x%10] == 0){
                        count++;
                        a[x%10] = 1;
                    }
                    x/=10;
                }
                l++;
            }
           cout << "Case " << "#" << ca << ": "<< ans << endl;
        }
    }
}
