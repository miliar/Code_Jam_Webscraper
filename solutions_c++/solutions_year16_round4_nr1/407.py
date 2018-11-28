#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<queue>
#include<vector>
#include<set>
#include<stack>
#include<map>
#include<ctime>
#include<bitset>
#define LL long long
#define db double
#define EPS 1e-8
#define inf 1e9

using namespace std;
int cntnum[300];
bool flagok=1;
string sousuo(char shengli, int n) {
    if (n==0)
        if (cntnum[shengli]>0){
            cntnum[shengli]--;
            return string(1,shengli);
        }
        else {
            flagok=0;
            return "$";
        };
    if (shengli=='P') {
        string s1=sousuo('P',n-1);
        string s2=sousuo('R',n-1);
        if (s1<s2) return s1+s2;
        else return s2+s1;
    }
    if (shengli=='R') {
        string s1=sousuo('R',n-1);
        string s2=sousuo('S',n-1);
        if (s1<s2) return s1+s2;
        else return s2+s1;
    }
    if (shengli=='S') {
        string s1=sousuo('S',n-1);
        string s2=sousuo('P',n-1);
        if (s1<s2) return s1+s2;
        else return s2+s1;
    }
}
int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T,cas=1;
    scanf("%d",&T);
    while (T--){
        int n,r,p,s;
        scanf("%d%d%d%d",&n,&r,&p,&s);
        vector<string> str;
        string s1;
        cntnum['R']=r;
        cntnum['P']=p;
        cntnum['S']=s;
        flagok=1;
        s1=sousuo('P',n);
        if (flagok)
            str.push_back(s1);
        cntnum['R']=r;
        cntnum['P']=p;
        cntnum['S']=s;
        flagok=1;
        s1=sousuo('R',n);
        if (flagok)
            str.push_back(s1);
        cntnum['R']=r;
        cntnum['P']=p;
        cntnum['S']=s;
        flagok=1;
        s1=sousuo('S',n);
        if (flagok)
            str.push_back(s1);
        if (str.size()==0){
            printf("Case #%d: ",cas++);
            puts("IMPOSSIBLE");
        }
        else {
            sort(str.begin(),str.end());
            printf("Case #%d: ",cas++);
            cout<<str[0]<<endl;
        }
    }
    return 0;
}
