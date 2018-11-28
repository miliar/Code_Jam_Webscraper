#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define ii pair<int,int>
#define INF 1000000000
#define UNIQUE(x) (x).resize(distance((x).begin(),unique(all(x))))
int ans[5][5]={
    {0,0,0,0,0},
    {0,1,2,3,4},
    {0,2,-1,4,-3},
    {0,3,-4,-1,2},
    {0,4,3,-2,-1}
};
int main() {
    int tc;
    cin>>tc;
    for (int kk=0;kk<tc;kk++) {
        int cur=1,sign=1;
        int l,x;
        string tmp,s;
        cin>>l>>x;
        cin>>tmp;
        for (int i=0;i<x;i++) s+=string(tmp);
        int idx=0,n=l*x;
        bool hasi=0,hasj=0,hask=0;
        while(idx<n) {
            int r=s[idx]-'i'+2;
            cur=ans[cur][r];
            if (cur<0) {
                cur=-cur;
                sign=-sign;
            }
            idx++;
            if (cur==2&&sign==1) {
                hasi=1;
                break;
            }
        }
        cur=1,sign=1;
        while(idx<n) {
            int r=s[idx]-'i'+2;
            cur=ans[cur][r];
            if (cur<0) {
                cur=-cur;
                sign=-sign;
            }
            idx++;
            if (cur==3&&sign==1) {
                hasj=1;
                break;
            }
        }
        cur=1,sign=1;
        while(idx<n) {
            int r=s[idx]-'i'+2;
            cur=ans[cur][r];
            if (cur<0) {
                cur=-cur;
                sign=-sign;
            }
            idx++;
        }
        if (cur==4&&sign==1) {
            hask=1;
        }
        printf("Case #%d: %s\n", kk+1,((hasi&&hasj&&hask)?"YES":"NO"));
    }

}