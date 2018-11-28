#include<iostream>
#include<stdio.h>
#include<string.h>
#include<string>
#include<algorithm>
#include<set>
#define fi first
#define se second
using namespace std;
typedef pair<int, int> pii;
int main(){
    freopen("inputA.in", "r", stdin);
    freopen("outputA.in", "w", stdout);
    int T;
    cin>>T;
    for(int t = 1; t <= T; t++){
        int n;
        cin>>n;
        set<pii> s;
        for(int i = 0; i < n; i++){
            int x;
            cin>>x;
            if(x)
                s.insert(pii(x, i));
        }
        cout<<"Case #"<<t<<": ";
        while(s.size() > 1){
            pii p1 = *s.rbegin();
            s.erase(prev(s.end()));
            pii p2 = *s.rbegin();
            pii beg = *s.begin();
            s.erase(prev(s.end()));
            if(p1.fi - beg.fi > 0){
                cout<<(char)(p1.se + 'A')<<' ';
                p1.fi--;
            }
            else if(((int)s.size()) & 1){
                while(p1.fi){
                    p1.fi--;
                    cout<<(char)(p1.se + 'A')<<' ';
                }
            }
            else{
                cout<<(char)(p1.se + 'A')<<(char)(p2.se + 'A')<<' ';
                p1.fi--, p2.fi--;
            }
            if(p1.fi) s.insert(p1);
            if(p2.fi) s.insert(p2);
        }
        cout<<'\n';
    }
    return 0;
}
