/*
 *Aditya Gourav @ adi.pearl
 */
#include<bits/stdc++.h>
using namespace std;

#define R(f) freopen(f,"r",stdin);
#define W(f) freopen(f,"w",stdout);
#define TEST int num_cases; cin>>num_cases;for(int case_id=1;case_id <= num_cases;++case_id)

typedef unsigned long long ull;

/** Main Code starts here :) **/
#define SUBMIT
int main(){

    #ifdef SUBMIT
    R("B-large.in");
    W("B-large.txt");
    #endif

    TEST{
        string s;
        cin >> s;
        printf("Case #%d: ", case_id);

        int ans = 0;
        char c = s[s.length()-1];
        for(int i = s.length()-2; i >= 0; --i){
            if(s[i] != c)
                ans++;
            c = s[i];
        }

        if(s[s.length()-1] == '-')
            ans++;

        cout << ans << endl;

    }


return 0;
}
