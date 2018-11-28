#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <ctype.h>
#include <stack>
#include <queue>
#include <limits.h>
#include <fstream>
#include <map>
#include <set>

#define rep(i, a) for(long long int i = 0; i < a; i++)
#define rep1(i, a) for(long long int i = 1; i <= a; i++)
#define fo(i, a, b) for(long long int i = a; i < b; i++)
#define defo(i, a, b) for(long long int i = a; i >= b; i--)
#define ll long long
#define Int long long int
#define pr(i) printf("Case #%lld: ",i)
#define pb push_back
#define sz(a) ((long long int)(a.size()))
#define x first
#define y second
#define fin(e) freopen("e.txt","r",stdin)
#define fout(e) freopen("e.txt","w",stdout)
#define mp make_pair
#define SET(x, a) memset(x, a, sizeof(x));
#define pi  3.1415926535897
#define mod 1000000007
#define retunr return
using namespace std;

typedef vector<long long int> vi;
typedef vector<ll> vll;
typedef pair<long long int, long long int> pii;
typedef pair<ll, ll> pll;
map<pair<string,string>,string> mul;
int main(){
    freopen("inpp.in","r",stdin);
    freopen("output.txt","w",stdout);
    int test;
    Int l = 0;
    mul[mp("1","1")] = "1";
    mul[mp("1","i")] = "i";
    mul[mp("1","j")] = "j";
    mul[mp("1","k")] = "k";
    mul[mp("i","1")] = "i";
    mul[mp("i","i")] = "-1";
    mul[mp("i","j")] = "k";
    mul[mp("i","k")] = "-j";
    mul[mp("j","1")] = "j";
    mul[mp("j","i")] = "-k";
    mul[mp("j","j")] = "-1";
    mul[mp("j","k")] = "i";
    mul[mp("k","1")] = "k";
    mul[mp("k","i")] = "j";
    mul[mp("k","j")] = "-i";
    mul[mp("k","k")] = "-1";
    cin>>test;
    while(test--){
        l++;
        int a,b;
        cin>>a>>b;
        string str;
        cin>>str;
        string str1="";
        int c=0,ve=0,i,j;
        for(i=0;i<b;i++){
            str1 =str1+str;
        }
        str = str1;
        string p = "1";
        for(i=0;i<str.size();i++){
            string temp = "";
            temp=temp+str[i];
            //cout<<temp<<"\n";
            p = mul[mp(p,temp)];
            if(p=="-1"){
                p = "1";
                ve++;
            }
            if(p=="-i"){
                p = "i";
                ve++;
            }
            if(p=="-j"){
                p = "j";
                ve++;
            }
            if(p=="-k"){
                p = "k";
                ve++;
            }
            if(c==0&&p=="i"&&ve%2==0){
                c++;
                p = "1";
                ve = 0;
            }
            else if(c==1&&p=="j"&&ve%2==0){
                c++;
                p = "1";
                ve = 0;
            }
            //cout<<p<<"\n";
        }
        pr(l);
        if(c==2&&p=="k"&&ve%2==0){
            cout<<"YES\n";
        }
        else{
            cout<<"NO\n";
        }
    }
    return 0;
}
