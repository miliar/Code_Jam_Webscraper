#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <ctime>
#include <cctype>
#include <iomanip>
#include <algorithm>
#include <list>
using namespace std;


#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#define rerm(i,l,u,m) for(int (i)=(int)(l);(i)<=(int)(u);(i)+=(m))
typedef long long int lli;
typedef long long ll;
typedef unsigned long long int ulli;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
#define pb(x) push_back(x)
#define modu 1000000007


int main(){
    int t;
    ofstream fout ("A-large.out");
    ifstream fin ("A-large.in");
    fin>>t;
    rep(j,t){
        int n;
        string ch;
        fin>>n>>ch;
        int shy=0,friends=0;
        rep(i,n+1){
            if(shy<i){
                friends++;
                shy+=(i-shy);
            }
            //cout<<(int)'1';
            shy+=((int)ch[i]-48);
            //cout<<"shy-"<<shy<<endl;
        }
        fout<<"Case #"<<j+1<<": "<<friends<<endl;

    }

    return 0;
}
