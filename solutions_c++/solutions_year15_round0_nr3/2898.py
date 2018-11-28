// Headers
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cassert>
#include<vector>
#include<map>
#include<fstream>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
#include<bitset>
#include<set>
using namespace std;
// Global declarations
typedef long long int ll;
typedef vector<int> vi;
typedef vector<char> vc;
typedef pair<int,int> pi;
const double eps = 1e-6;
int const mod  = 1e9+7;
int const INF = 1<<29;
// Macros
#define mp make_pair
#define el putchar('\n')
#define sp putchar(' ')
#define Fill(a,val) memset(a,val,sizeof a)
#define pb push_back
#define ppb pop_back
#define gcd __gcd
#define all(a) a.begin(),a.end()
#define ff first
#define ss second

struct cc{
    char data;
    bool mn;
    cc(){}
    cc(char d,bool b){
        data = d;
        mn = b;
    }
    bool operator == (cc const &ob){
        return (data==ob.data && mn == ob.mn);
    }
};
cc  mul(cc a,cc b){
    cc ret ;
    if((a.mn && b.mn)||(!a.mn && !b.mn)) ret.mn = 0;
    else ret.mn = 1;
    if(a.data == '1') {ret.data = b.data;return ret;}
    if(b.data == '1') {ret.data = a.data;return ret;}
    if(a.data == b.data) {
        ret.data = '1';
        ret.mn = 1-ret.mn;
        return ret;
    }
    if(a.data == 'i') {
        if(b.data == 'j') {
            ret.data = 'k';
            return ret;
        }
        else {
            ret.data = 'j';
            ret.mn = 1-ret.mn;
            return ret;
        }
    }
    if(a.data == 'j') {
        if(b.data == 'i') {
            ret.data = 'k';
            ret.mn = 1-ret.mn;
            return ret;
        }
        else {
            ret.data = 'i';
            return ret;
        }
    }
    if(a.data == 'k') {
        if(b.data == 'i') {
            ret.data = 'j';
            return ret;
        }
        else {
            ret.data = 'i';
            ret.mn = 1-ret.mn;
            return ret;
        }
    }
}

void print(cc c){
    if(c.mn) putchar('-');
    putchar(c.data);putchar(',');
}

int main(){
    freopen("ip.in","r",stdin);
    freopen("op2.out","w",stdout);
    int t,tcase=1;scanf("%d",&t);
    while(t--){
        int L,X;
        scanf("%d %d",&L,&X);
        string s,a;
        cin>>a;
        for(int i=0;i<X;++i){
            s += a;
        }
        int n = s.length();
        printf("Case #%d: ",tcase++);
        if(n < 3) {
            puts("NO");
            continue;
        }
        int lp = -1 , rp = -1;
        cc l[n+2] , r[n+2];
        l[0]= cc(s[0],0);
        r[n-1] = cc(s[n-1],0);
        for(int i=1;i<n;++i)
            l[i] = mul(l[i-1],cc(s[i],0));

        for(int i=n-2;i>=0;--i)
            r[i]=mul(cc(s[i],0),r[i+1]);

        /*cout<<"\n-----------------\n";
        for(int i=0;i<n;++i) {cout<<i<<"->";print(l[i]);print(r[i]),el;}
        cout<<"\n-----------------\n";*/
        cc I('i',0),J('j',0),K('k',0);
        for(int i=0;i<n-2;++i){
            if(l[i]==I && r[i+1]==I) {lp = i;break;}
        }
        for(int i=n-1;i>1;--i){
            if(r[i]==K && l[i-1]==K) {rp = i;break;}
        }
        /*for(int i=0;i<ls;++i) print(l[lp[i]]);
        el;
        for(int i=0;i<rs;++i) print(r[rp[i]]);
        el;*/
        if(lp == -1 or rp == -1) {puts("NO");continue;}
        if(lp +1 >= rp) {puts("NO");continue;}
        /*for(int i=0;i<ls;++i){
            for(int j=rs-1;j>=0 and (rp[j]> (lp[i]+1)) ;--j){
                int posL = lp[i];
                int posR = rp[j];

                if((data == 'k' && !mn) and (Data == 'i' && !Mn)) {
                    YES = true;
                    break;
                }
            }
            if(YES) break;
        }*/
        puts("YES");
    }
    return 0;
}
