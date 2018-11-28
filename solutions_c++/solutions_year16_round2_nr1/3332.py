#include<bits/stdc++.h>
#define MAX 10000
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
#define ellapse printf("Time : %0.3lf\n",clock()*1.0/CLOCKS_PER_SEC);
using namespace std;/*//E,SE,S,SW,W,NW,N,NEint dr[8]={0,1,1,1,0,-1,-1,-1};int dc[8]={1,1,0,-1,-1,-1,0,1};*/
typedef long long l64d;
typedef unsigned long int ud;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;int ans[19]={};
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    //std::ios::sync_with_stdio(false);    int t,cnt[30];    string inp;    cin>>t;    for(int i=0;i<t;i++) {        memset(cnt, 0, sizeof cnt);        memset(ans,0,sizeof ans);        cout<<"Case #"<<(i+1)<<": ";        cin>>inp;        for(int j=0;j<inp.size();j++) {            cnt[inp[j]-'A']++;        }        if(cnt['Z'-'A']) {            cnt['E'-'A'] -= cnt['Z'-'A'];            cnt['R'-'A'] -= cnt['Z'-'A'];            cnt['O'-'A'] -= cnt['Z'-'A'];            ans[0] = cnt['Z'-'A'];            cnt['Z'-'A'] = 0;        }        if(cnt['W'-'A']) {            cnt['T'-'A'] -= cnt['W'-'A'];            cnt['O'-'A'] -= cnt['W'-'A'];            ans[2] = cnt['W'-'A'];            cnt['W'-'A'] = 0;        }        if(cnt['X'-'A']) {            cnt['S'-'A'] -= cnt['X'-'A'];            cnt['I'-'A'] -= cnt['X'-'A'];            ans[6] = cnt['X'-'A'];            cnt['X'-'A'] = 0;        }        if(cnt['G'-'A']) {            cnt['E'-'A'] -= cnt['G'-'A'];            cnt['I'-'A'] -= cnt['G'-'A'];            cnt['H'-'A'] -= cnt['G'-'A'];            cnt['T'-'A'] -= cnt['G'-'A'];            ans[8] = cnt['G'-'A'];            cnt['G'-'A'] = 0;        }        if(cnt['U'-'A']) {            cnt['F'-'A'] -= cnt['U'-'A'];            cnt['O'-'A'] -= cnt['U'-'A'];            cnt['R'-'A'] -= cnt['U'-'A'];            ans[4] = cnt['U'-'A'];            cnt['U'-'A'] = 0;        }        if(cnt['H'-'A']) {            cnt['T'-'A'] -= cnt['H'-'A'];            cnt['R'-'A'] -= cnt['H'-'A'];            cnt['E'-'A'] -= 2*cnt['H'-'A'];            ans[3] = cnt['H'-'A'];            cnt['H'-'A'] = 0;        }        if(cnt['F'-'A']) {            cnt['I'-'A'] -= cnt['F'-'A'];            cnt['V'-'A'] -= cnt['F'-'A'];            cnt['E'-'A'] -= cnt['F'-'A'];            ans[5] = cnt['F'-'A'];            cnt['F'-'A'] = 0;        }        if(cnt['V'-'A']) {            cnt['S'-'A'] -= cnt['V'-'A'];            cnt['E'-'A'] -= 2*cnt['V'-'A'];            cnt['N'-'A'] -= cnt['V'-'A'];            ans[7] = cnt['V'-'A'];            cnt['V'-'A'] = 0;        }        if(cnt['I'-'A']) {            cnt['N'-'A'] -= 2*cnt['I'-'A'];            cnt['E'-'A'] -= cnt['I'-'A'];            ans[9] = cnt['I'-'A'];            cnt['I'-'A'] = 0;        }        if(cnt['O'-'A']) {            ans[1] = cnt['O'-'A'];        }        for(int j=0;j<10;j++) {            for(int k=0;k<ans[j];k++) {                cout<<j;            }        }        cout<<"\n";    }
    #ifdef Xanxiver
    //ellapse;
    #endif // Xanxiver
}
