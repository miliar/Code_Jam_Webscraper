
/// #sh

#include<bits/stdc++.h>

using namespace std;

int main(){
    #ifndef ONLINE_JUDGE
        freopen("B-large.in", "r", stdin);
        freopen("blarge.out", "w", stdout);
    #endif // ONLINE_JUDGE

    int test;
    scanf("%d", &test);
    getchar();
    for(int t = 1; t <= test; ++t){
        string st;
        cin >> st;

        int i = 0, j = st.size() - 1;

        while(st[j] != '-' and j>=0)
            j--;

       // cout << "j = " << j << endl;

        int ans = 0;
        while(i<=j and i<st.size()){
            if(st[i] == '+'){
                ans++;
                while(st[i] != '-' and i<st.size() and i<=j)
                    i++;
            }
            else{
                ans++;
                while(st[i] != '+' and i<st.size() and i<=j)
                    i++;
            }

        }
        printf("Case #%d: %d\n", t, ans);
    }

}
