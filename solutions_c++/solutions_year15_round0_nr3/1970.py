#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

string s, a;
int m[4][4]={{1, 2, 3, 4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1}};

int solve(int val) {
    int res=(s[0]-'i')+2;
    if(res==val) return 0;
    for(int i=1; i<s.size(); i++) {
        int v=(s[i]-'i')+2, sign=res>0 ? 1 : -1;
        int a=abs(res)-1, b=v-1;
        if(val==4) swap(a, b);
        res=sign*m[a][b];
        if(res==val) return i;
    }
    return -1;
}

int main() {
    int n, x, t, T=1;
    scanf("%d", &t);
    while(t--) {
        s="";
        scanf("%d %d", &n, &x);
        cin >> a;
        int res=(a[0]-'i')+2;
        for(int i=1; i<a.size(); i++) {
            int v=(a[i]-'i')+2, s=res>0 ? 1 : -1;
            res=s*m[abs(res)-1][v-1];
        }
        printf("Case #%d: ", T++);
        vector<int> v;
        v.push_back(res);
        while(1) {
            int s1=res>0 ? 1 : -1, s2=v[0]>0 ? 1 : -1, f=0;
            res=s1*s2*m[abs(res)-1][abs(v[0])-1];
            for(int i=0; i<v.size(); i++) if(v[i]==res) {
                f=1;
                break;
            }
            if(f) break;
            v.push_back(res);
        }
        int tam=(int)v.size();
        if(v[(x-1)%tam]!=-1) printf("NO");
        else {
            for(int i=0; i<min(16, x); i++) s+=a;
            ll ret1=solve(2);
            reverse(s.begin(), s.end());
            ll ret2=solve(4);
            if(ret1==-1 || ret2==-1) printf("NO");
            else {
                ret2=1ll*n*x-ret2-1;
                if(ret2<=ret1) printf("NO");
                else printf("YES");
            }
        }
        printf("\n");
    }
    return 0;
}
