// By manrajsingh
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define d1(a)cout<<#a<<": "<<a<<"\n";
#define d2(a,b)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<"\n";
#define d3(a,b,c)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<"\n";
#define d4(a,b,c,d)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<" , "<<#d<<": "<<d<<"\n";

map<char,int> m;

int main() {
    int t,x=0;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin>>t;
    while(t--){
        ll ans[15];
        memset(ans, 0, sizeof(ans));
        x++;
        string s;
        cin>>s;
        for(ll i=0;i<s.length();i++){
            m[s[i]]++;
        }
        /*
        for(auto i=m.begin();i!=m.end();i++){
        	cout<<i->first<<" "<<i->second<<"\n";
        }*/
        while(m['X']){
            m['S']--;m['I']--;m['X']--;
            ans[6]++;
        }
        while(m['G']){
            m['E']--;m['I']--;m['G']--;m['H']--;m['T']--;
            ans[8]++;
        }
        while(m['S']){
            m['S']--;m['E']--;m['V']--;m['E']--;m['N']--;
            ans[7]++;
        }
        while(m['H']){
            m['T']--;m['H']--;m['R']--;m['E']--;m['E']--;
            ans[3]++;
        }
        while(m['Z']){
            m['Z']--;m['E']--;m['R']--;m['O']--;
            ans[0]++;
        }
        while(m['T']){
            m['T']--;m['W']--;m['O']--;
            ans[2]++;
        }
        while(m['R']){
            m['F']--;m['O']--;m['U']--;m['R']--;
            ans[4]++;
        }
        while(m['F']){
            m['F']--;m['I']--;m['V']--;m['E']--;
            ans[5]++;
        }
        while(m['O']){
            m['O']--;m['N']--;m['E']--;
            ans[1]++;
        }
        while(m['N']){
            m['N']--;m['I']--;m['N']--;m['E']--;
            ans[9]++;
        }
        cout<<"Case #"<<x<<": ";
        for(int i=0;i<=9;i++){
            while(ans[i]--){
                cout<<i;
            }
        }
        cout<<"\n";
    }
	return 0;
}
