#include <bits/stdc++.h>
using namespace std;
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define forex(i,j) for(int i=0;i<(j);i++) // 0 .. N-1
#define forin(i,j) for(int i=0;i<=(j);i++) // 0 .. N
#define printv(v) {for(int i=0;i<v.size();i++) cout<<v[i]<<" ";cout<<"\n";}
#define printa(a,len) {for(int i=0;i<len;i++) cout<<a[i]<<" ";cout << "\n";}

typedef long long ll;
typedef pair<int,int> pii;

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<ll> vll;
typedef vector<pii> vpii;

#define mp make_pair
#define pb push_back
#define uset unordered_set
#define umap unordered_map
#define mset multiset
#define mmap multimap
#define umset unordered_multiset
#define ummap unordered_multimap
#define all(v) (v).begin(),(v).end()

//int xx[]={0,1,0,-1,-1,-1,1,1,-1};int yy[]={1,0,-1,0,1,1,-1,-1}; //E S W N NE SE SW NW
int main() {
_
int T;cin>>T;

for(int XX=1;XX<=T;XX++){
    string s;int k;
    cin>>s>>k;
    int sz=s.size();
    string temp="";
    for(int i=0;i<sz;i++)temp+='+';
    int lo=0,hi=sz-1;
    int steps=0;
    while(lo<sz && s[lo]=='+')lo++;
    while(hi>=0 && s[hi]=='+')hi--;
    while(temp!=s && hi-lo+1 >=k){
        for(int i=0;i<k;i++){
            if(s[lo+i]=='-')s[lo+i]='+';
            else s[lo+i]='-';
        }
        steps++;
        if(s[hi]=='-'){
        for(int i=0;i<k;i++){
            if(s[hi-i]=='-')s[hi-i]='+';
            else s[hi-i]='-';
        }
        steps++;
        }
        while(lo<sz && s[lo]=='+')lo++;
        while(hi>=0 && s[hi]=='+')hi--;
    }
    int flag=0;
    if(s!=temp){
        flag=1;
    }
    if(flag)
    cout<<"Case #"<<XX<<": "<<"IMPOSSIBLE"<<"\n";
    else
    cout<<"Case #"<<XX<<": "<<steps<<"\n";
}
return 0;
}
