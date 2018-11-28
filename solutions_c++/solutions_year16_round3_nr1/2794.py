#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vI;
typedef vector<double> vD;
typedef vector<pair<int, int> > vpI;
typedef vector<string> vS;
typedef pair<int, int> pI;
typedef pair<double, double> pD;
typedef map<int, int> mI;
typedef map<string, int> mSI;
typedef map<int, pair<int, int> > mIP;
typedef map<pair<int, int>, int> mPI;
typedef set<int> sI;
typedef set<pI> sPI;
typedef set<string> sS;
typedef priority_queue<int> Qmax;
typedef priority_queue<int, vector<int>, greater<int> >Qmin;

#define TWO(k)  (1<<(k))
#define LTWO(k) (((LL)(1)<<(k)))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define For(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define Ford(i,a,b) for(int (i)=(a);(i)>=(b);(i)--)
#define F0(n) for(int (i)=0;(i)<(n);(i)++)
#define F1(n) for(int (i)=1;(i)<=(n);(i)++)
#define Zero(i) memset((i),0,sizeof((i)))
#define Fu1(i) memset((i),0xff,sizeof((i)))
#define Bit(s,i) (( (s) &(1<<(i)))>0)
#define NP next_permutation

//const double PI = acos(-1.0);
//const double EPS = 1e-9;
//const int ioo = (~0)-(1<<31);
//const LL loo = (~(LL)0)-((LL)1<<63);
//const int MOD = 1000000007;
//const LL MODL = 1000000007LL;
//const LL LL1 = (LL)1;

priority_queue<pI> pq;
int n;

void print_char(int x){
    cout<<(char)(x+'A');
}

int main()
{
     freopen("out.txt","w",stdout);
     freopen("A-large.in","r",stdin);
    //freopen("in.txt","r",stdin);
    int TTT, test = 0;
    cin>>TTT;
    while(TTT--){
        cout<<"Case #"<<++test<<": ";
        cin>>n;
        for(int i = 0; i < n; i++){
            int j, k; cin>>j;
            pq.push(MP(j, i));
        }
        while(!pq.empty()){
            pI u = pq.top(); pq.pop();
            pI v = pq.top(); pq.pop();
            if(pq.empty() && u.first == 1 && v.first == 1){
                print_char(u.second);
                print_char(v.second);
            }
            else if(pq.size() == 1 && u.first == 1 && v.first == 1){
                print_char(u.second);
                pq.push(v);
            }
            else if(u.first - v.first >= 1){
                print_char(u.second);
                u.first -= 1;
                if(u.first > 0) pq.push(u);
                pq.push(v);
            }
            else{
                print_char(u.second);
                print_char(v.second);
                u.first--;
                v.first--;
                if(u.first > 0) pq.push(u);
                if(v.first > 0) pq.push(v);
            }
            if(!pq.empty()) cout<<' ';
        }
        cout<<endl;
    }
    return(0);
}
