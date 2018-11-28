#include <bits/stdc++.h>
#define in cin>>
#define inn(a,b) cin>>a>>b
#define out cout<<
#define $$ >>
#define $_ <<
#define outt(k) cout<<(k)<<endl
#define outs(k) cout<<(k)<<" "
#define M 1002
#define FOR(i,k,l)   for(int i(k); i<l; i++)
#define Si set<int>
#define Mii map<int,int>
#define Mss map<string,string>
#define Mci map<char,int>
#define Msi map<string,int>
#define vi vector<int>
#define vpi vector<pair <int,int>>
#define vs vector<string>
#define pb push_back
#define dc deque<char>
#define di deque<int>





using namespace std;

int main(){
    ifstream cin("A-large.in");
    ofstream cout("A-large.out");

    int t;
    in(t);

    FOR(i,0,t){
        int k;
        in(k);
            int res(0),total=0;char temp;
            FOR(j,0,k+1){
                in(temp);
                if(temp!='0' && total<j){
                    res+=(j-total);
                    total=j;
                }
                total+=temp-'0';
            }
            cout<<"Case #"<<i+1<<": "<<res;
            if(i != (t-1))
                out(endl);

    }

    return 0;
}
