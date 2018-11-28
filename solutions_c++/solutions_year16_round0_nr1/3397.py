#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("cj.in","r",stdin);
    freopen("cj.out","w",stdout);
    int t; cin >> t;
    for(int tc=1 ; tc<=t ; tc++){
        int n; cin >> n;
        if(n==0){
            cout << "Case #" << tc << ": INSOMNIA" << endl;
            continue;
        }
        int temp = n;
        int rep = 0;
        set<int> st;
        while(true){
            int x = temp;
            while(x>0){
                st.insert(x%10);
                x/=10;
            }
            if(st.size() == 10) break;
            temp += n;
            rep++;
        }
        cout << "Case #" << tc << ": " << temp << endl;
    }
}