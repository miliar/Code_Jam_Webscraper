#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(NULL); cin.tie(NULL);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tests; cin >> tests;
    for(int test = 1;test <= tests;test++){
        int h,w,k;
        cin >> k >> h >> w;
        bool ans;
        if(h == 1){
            if(k > 2){ans = false;}
            else if(k == 1){ans = true;}
            else if(k == 2){
                if(w % 2 == 1){ans = false;}
                else{ans = true;}
            }
        }
        else if(h == 2){
            if(k <= 2){ans = true;}
            else if(k == 4){ans = false;}
            else if(k == 3){
                if(w == 3){ans = true;}
                else{ans = false;}
            }
        }
        else if(h == 3){
            if(k == 1){ans = true;}
            else if(k == 3){
                if(w == 1){ans = false;}
                else{ans = true;}
            }
            else if(k == 2){
                if(w % 2 == 0){ans = true;}
                else{ans = false;}
            }
            else if(k == 4){
                if(w < 4){ans = false;}
                else{ans = true;}
            }
        }
        else if(h == 4){
            if(k <= 2){ans = true;}
            else if(k == 3){
                if(w == 3){ans = true;}
                else{ans = false;}
            }
            else if(k == 4){
                if(w <= 2){ans = false;}
                else{ans = true;}
            }
        }
        cout << "Case #" << test << ": ";
        if(ans == true){cout << "Gabriel" << '\n';}
        else{cout << "Richard" << '\n';}
    }
    return 0;
}
