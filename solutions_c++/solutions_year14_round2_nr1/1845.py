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

#define rep(i, a) for(int i = 0; i < a; i++)
#define rep1(i, a) for(int i = 1; i <= a; i++)
#define fo(i, a, b) for(int i = a; i < b; i++)
#define defo(i, a, b) for(int i = a; i >= b; i--)
#define ll long long
#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a.size()))
#define x first
#define y second
#define SET(x, a) memset(x, a, sizeof(x));
using namespace std;

typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
int abs(int a){
    if(a<0){
        return -1*a;
    }
    return a;
}
int main(){
    freopen("a.in","r",stdin);
    freopen("b.out","w",stdout);
    int test,l=0;
    cin>>test;
    while(test--){
        l++;
        string s1,s2,s3="",s4="";
        vector<int> v1,v2;
        int n;
        cin>>n;
        cin>>s1>>s2;
        int i,x=1;
        char c = s1[0];
        char c2 = s2[0];
        for(i=1;i<s1.size();i++){
            if(s1[i]==c){
                x++;
            }
            else{
                v1.push_back(x);
                x = 1;
                s3=s3+c;
                c = s1[i];
            }
        }
        v1.push_back(x);
        x = 1;
        s3=s3+c;
        /*cout<<s3<<"\n";
        for(i=0;i<v1.size();i++){
            cout<<v1[i]<<" ";
        }
        cout<<"\n";*/
        for(i=1;i<s2.size();i++){
            if(s2[i]==c2){
                x++;
            }
            else{
                v2.push_back(x);
                x = 1;
                s4=s4+c2;
                c2 = s2[i];
            }
        }
        v2.push_back(x);
        x = 0;
        s4=s4+c;
        /*cout<<s4<<"\n";
        for(i=0;i<v2.size();i++){
            cout<<v2[i]<<" ";
        }
        cout<<"\n";*/
        if(s3!=s4){
            cout<<"Case #"<<l<<": "<<"Fegla Won\n";
        }
        else{
            int ans = 0;
            for(i=0;i<v1.size();i++){
                ans+=abs(v1[i]-v2[i]);
            }
            cout<<"Case #"<<l<<": "<<ans<<"\n";
        }
    }
}
