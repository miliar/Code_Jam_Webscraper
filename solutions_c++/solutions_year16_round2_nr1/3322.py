#include <bits/stdc++.h>

using namespace std;

int main()
{
    int i, j, k, t;
    string s;
    freopen("cd31.in", "r", stdin);
    freopen("cd_ans.txt", "w", stdout);
    int a[26];
    map <int, string> mp;
    mp[0] = "ZERO";
    mp[1] = "ONE";
    mp[2] = "TWO";
    mp[3] = "THREE";
    mp[4] = "FOUR";
    mp[5] = "FIVE";
    mp[6] = "SIX";
    mp[7] = "SEVEN";
    mp[8] = "EIGHT";
    mp[9] = "NINE";
    int flag, cnti;
   // stack <int> st;
    cin>>t;
    int v[10], ban[10];

    for (int l = 1; l <= t; l++) {
        cin>>s;
        memset(a, 0, sizeof(a));
        memset(v,0,sizeof(v));
        for (i = 0; i < s.length(); i++) {
            a[s[i]-65]++;
        }

        v[0] = a['Z'-65];
        a['Z'-65] = 0;
        v[2] = a['W'-65];
        a['W'-65] = 0;
        v[4] = a['U'-65];
        a['U'-65] = 0;
        v[1] = a['O'-65] - v[4] - v[2] - v[0];
        //a['O'-65] = a['O'-65] - v[1];
        v[5] = a['F'-65] - v[4];
        //a['F'-65] -= v[5];
        v[3] = a['R'-65] - v[0] - v[4];
        v[6] = a['X'-65];
        v[8] = a['G'-65];
        v[7] = a['S'-65] - v[6];
        v[9] = a['I'-65] - v[5]- v[6]-v[8];
        cout<<"Case #"<<l<<": ";
        for (i = 0; i < 10; i++) {
            for (j = 0; j < v[i]; j++) {
                cout<<i;
            }
        }
        cout<<endl;
    }

    return 0;
    }
/*    for (int l = 1; l <= t; l++) {
        cin>>s;
        memset(a, 0, sizeof(a));
        memset(v,0,sizeof(v));
        memset(ban, 0, sizeof(ban));
        for (i = 0; i < s.length(); i++) {
            a[s[i]-65]++;
        }
        stack<int> st;
        int last;
        do {
        cnti = 0;
        for (i = 0; i < 10; i++) {
            if(ban[i] == false) {
                flag = 0;
                string str = mp[i];
               // cout<<str<<endl;
                while (flag == 0) {
                    for (j = 0; j < str.length(); j++) {
                        //cout<<str[j]<<"\n";
                        if (a[str[j]-65] == 0) {
                            flag = 1;
                            break;
                        }
                        else {
                            a[str[j]-65]--;
                        }
                    }
                    if (flag == 0) {
                        st.push(i);
                        v[i]++;
                    }
                    else {
                        for (int k = 0; k < j; k++) {
                            a[str[k]-65]++;
                        }
                    }
                }
            }
        }
        for (int k = 0; k < 26; k++) {
            if (a[k]) {
                if(!st.empty()) {
                string str = mp[st.top()];
                ban[st.top()] = true;
                v[st.top()]--;
                st.pop();
                for (j = 0; j < str.length(); j++) {
                    a[str[j]-65]++;
                }
                }
                cnti = 1;
            }
        }
        }while(cnti==1);
            cout<<"Case #"<<l<<": ";
        for (i = 0; i < 10; i++) {
            for (j = 0; j < v[i]; j++) {
                cout<<i;
            }
        }
        cout<<endl;
    }

    return 0;
}
*/
