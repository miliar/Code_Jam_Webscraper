#include<bits/stdc++.h>
#define ll long long
#define M 1000000007
using namespace std;

int optimized(vector<int> &v, int k) {
    
    int n = v.size();
    int ans=0;

    while(true) {
        int i=0;
        while (i<n && v[i]==1) {
            i++;
        }

        if(i == n)break;

        int cnt = 0;
        while(i<n && v[i] == 0 && cnt<k) {
            cnt++;
            i++;
        }

        if(cnt == k) {
            while(cnt>0) {
                i--;
                v[i] = 1;
                cnt--;
            }
        } else {
            if (n-i < k) {
                ans = -1;
                break;
            }
            cnt = 0;
            while (cnt < k) {
                v[i] = 1 - v[i];
                i++;
                cnt++;
            }
        }

        ans++;
    }
    return ans;

}

void solve(int t) {

    string str;
    int k;
    cin>>str>>k;
    vector<int> v(str.size(), 0);
    for(int i=0; i<str.size(); i++) {
        if(str[i] == '+') {
            v[i] = 1;
        }
    }
   
//*
    int ans = optimized(v, k);
    if(ans == -1) {
        cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
    } else {
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    /**/
}


int main() {
    //A-small-attempt0 (1).in
    freopen("A-large (1).in", "r", stdin); freopen("output.txt", "w", stdout);

    int tc = 1;
    cin>>tc;
    
    for(int t=1; t<=tc; t++) {
        solve(t);
    }

}