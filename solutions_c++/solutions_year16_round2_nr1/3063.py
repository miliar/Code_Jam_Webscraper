//  Created by Vignesh Manoharan

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <cstring>
#include <cassert>
#include <numeric>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<vi> vvi;
typedef vector<ii> vii;

const int INF = 1000000000;
const ll LINF = 1e17;
const double PI =3.141592653589793238;
const int mod=1000000007;
#pragma unused(INF,PI,LINF,mod)
#define F(i,a,n) for(int i=(a);i<(n);i++)

template<typename T,typename TT> ostream& operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream& operator<<(ostream &s,vector<T> t){
    for(int i=0;i<(t).size();i++)s<<t[i]<<((i<(t).size()-1)?" ":"");return s; }
template<typename T> ostream& operator<<(ostream &s,set<T> t){for(T x:t) s<<x<<" ";return s; }
template<typename T> istream& operator>>(istream &s,vector<T> &t){
    for(int _i=0;_i<t.size();_i++) s>>t[_i];return s; }

#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()



int main(int argc, const char * argv[]) {
#ifdef local_test
    // input
    //    freopen("input","w",stdout);
    //    cout<<"1000000\n";
    //    F(i,0,1000000) cout<<i<<"\n";
    freopen("input","r",stdin);
    freopen("output","w",stdout);
#endif
    int t;
    cin>>t;
    for(int tc=1; tc<=t; tc++){
        string s;
        cin>>s;
        vi alph(26);
        vi nums;
        for(char c:s) alph[c-'A']++;
//        cout<<alph<<"\n";
        while(alph['Z'-'A']>0){
            nums.push_back(0);
            for(char c:"ZERO")
                alph[c-'A']--;
        }
        while(alph['X'-'A']>0){
            nums.push_back(6);
            for(char c:"SIX")
                alph[c-'A']--;
        }
        while(alph['W'-'A']>0){
            nums.push_back(2);
            for(char c:"TWO")
                alph[c-'A']--;
        }
        while(alph['U'-'A']>0){
            nums.push_back(4);
            for(char c:"FOUR")
                alph[c-'A']--;
        }
        while(alph['G'-'A']>0){
            nums.push_back(8);
            for(char c:"EIGHT")
                alph[c-'A']--;
        }
        while(alph['F'-'A']>0){
            nums.push_back(5);
            for(char c:"FIVE")
                alph[c-'A']--;
        }
        while(alph['H'-'A']>0){
            nums.push_back(3);
            for(char c:"THREE")
                alph[c-'A']--;
        }
        while(alph['I'-'A']>0){
            nums.push_back(9);
            for(char c:"NINE")
                alph[c-'A']--;
        }
        while(alph['S'-'A']>0){
            nums.push_back(7);
            for(char c:"SEVEN")
                alph[c-'A']--;
        }
        while(alph['O'-'A']>0){
            nums.push_back(1);
            for(char c:"ONE")
                alph[c-'A']--;
        }
//        cout<<nums<<"\n";
        sort(all(nums));
        printf("Case #%d: ",tc);

        for(int i:nums)
            cout<<i;
        cout<<"\n";
    }
}
