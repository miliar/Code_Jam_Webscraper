#include<bits/stdc++.h> 
using namespace std;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ul;
typedef unsigned int ui;
#define PB push_back
#define FOR(x,y) for(int x=0;x<(y);x++)
#define ROF(x,y) for(int x=(y);x>=0;x--)
#define FORR(x,y,z) for(int x=(z);x<(y);x++)
#define INT(x) int x;scanf("%d",&x)
deque<char> wyn;
string x;
int main(){
    int t,d=1;
    cin>>t;
    while(t--){
        cout << "Case #" << d << ": ";
        d++;
        cin >> x;
        wyn.clear();
        wyn.push_back(x[0]);
        FORR(i,x.size(),1){
            if(x[i]>=wyn.front())wyn.push_front(x[i]);
            else wyn.push_back(x[i]);
        }
        FOR(i,x.size()){
            cout<<wyn.front();
            wyn.pop_front();
        }
        cout << endl;
    }
}
        