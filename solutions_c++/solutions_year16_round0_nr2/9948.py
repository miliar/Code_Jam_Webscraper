#include <bits/stdc++.h>
using namespace std;

stack <int> st;

int main(){
    int t;
    cin >> t;
    int ca = 0;
    while(t--){
        ca++;
        string s;
        cin >> s;
        int count = 0;
        long ans = 0;
        for(int i = s.length() - 1; i >= 0; i--){
            if(s[i] == '-'){count++;}
            if(s[i] == '-') st.push(1);
            else{st.push(0);}
        }
        if(count == 0) ans = 0;
        else{
            while(count > 0){
                if(st.top() == 1){
                    while(!st.empty() && st.top() == 1){
                        st.pop();
                        count--;
                    }
                }else if(count > 0 && st.top() == 0){
                    int x = 0;
                    while(st.top() == 0){
                        st.pop();
                        x++;
                        count++;
                    }
                    for(int i = 0; i < x; i++) st.push(1);
                }
                ans++;
            }
        }
        cout << "Case " << "#" << ca << ": " << ans << endl;
    }
}
