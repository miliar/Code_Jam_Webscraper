// By: @shariquemohd

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string.h>
#include<vector>
#include<utility>

//-----------------

#define ull unsigned long long int
#define lli long long int
#define li long int
#define ft first
#define sc second
#define pb push_back
#define mp make_pair

//typedef pair<int,int> pii;
//typedef pair<int,pii> pip;

template <typename T>T power(T e, T n, T m){T x=1,p=e;while(n){if(n&1)x=mod(x*p,m);p=mod(p*p,m);n>>=1;}return x;}
template <typename T> T InverseEuler(T a, T m){return (a==1? 1:power(a, m-2, m));}
template <typename T> T gcd(T a, T b){return __gcd(a,b);}
template <typename T> T lcm(T a, T b){return (a*(b/gcd(a,b)));}

//-------------------

using namespace std;

const int MAX=1005;

int cnt[26],num[10];

int main(){

    freopen("A-large.in","r",stdin);
    freopen("AoL.out","w",stdout);
    int T,len,i;
    char s[2005];
    cin>>T;
    for(int z=1;z<=T;z++){
        memset(cnt,0,sizeof(cnt));
        scanf("%s",s);
        len=strlen(s);

        for(i=0;i<len;i++){
            cnt[s[i]-'A']+=1;
        }
        memset(num,0,sizeof(num));

        //for(i=0;i<26;i++)
        //    cout<<i<<" "<<cnt[i]<<"\n";

        num[0]=cnt['Z'-'A'];
        num[8]=cnt['G'-'A'];
        num[2]=cnt['W'-'A'];
        num[6]=cnt['X'-'A'];
        num[4]=cnt['U'-'A'];
        num[5]=cnt['F'-'A']-num[4];
        num[3]=cnt['T'-'A']-num[2]-num[8];
        num[7]=cnt['V'-'A']-num[5];
        num[1]=cnt['O'-'A']-num[0]-num[2]-num[4];
        num[9]=cnt['I'-'A']-num[8]-num[6]-num[5];

        cout<<"Case #"<<z<<": ";
        for(i=0;i<=9;i++){
            for(int j=0;j<num[i];j++){
                cout<<i;
            }
        }
        cout<<"\n";
    }

    return 0;
}
