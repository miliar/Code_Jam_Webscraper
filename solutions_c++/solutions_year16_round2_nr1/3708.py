#include <bits/stdc++.h>
using namespace std;

#define eprintf(...) fprintf(stderr,__VA_ARGS__)

string num[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool check(vector<int> &x) {
    for(int i=0;i<10;i++) {
        int times=2000; vector<int> c(26,0);
        for(int j=0;j<num[i].length();j++) c[num[i][j]-'A']++;
        for(int j=0;j<26;j++) {
            if(c[j]==0) continue;
            times=min(times,x[j]/c[j]);
        }
        for(int j=0;j<26;j++) x[j]-=times*c[j];
    }
    bool ok=true;
    for(int i=0;i<26;i++) if(x[i]) ok=false;
    return ok;
}

int main() {
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);

    int tc; cin>>tc;
    for(int T=1;T<=tc;T++) {
        string s; cin>>s;
        int n=s.length();
        vector<int> cnt(26,0);
        for(int i=0;i<n;i++) cnt[s[i]-'A']++;
        vector<int> ans;
        while(true) {
            bool br=true;
            for(int j=0;j<26;j++) if(cnt[j]!=0) br=false;
            if(br) break;
            for(int i=0;i<10;i++) {
                vector<int> c(26,0);
                for(int j=0;j<num[i].length();j++) c[num[i][j]-'A']++;
                bool ok=true;
                for(int j=0;j<26;j++) if(cnt[j]<c[j]) ok=false;
                if(ok) {
                    vector<int> ch=cnt;
                    for(int j=0;j<26;j++) ch[j]-=c[j];
                    bool x=check(ch);
                    if(x) {
                        ans.push_back(i);
                        for(int j=0;j<26;j++) cnt[j]-=c[j];
                    }
                }
            }
        }
        sort(ans.begin(),ans.end());
        printf("Case #%d: ",T);
        for(int i:ans) printf("%d",i);
        printf("\n");
    }
}
