#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <ctime>
#include <climits>
#include <cctype>
#include <iomanip>
#include <algorithm>
#include <list>
#include <map>
//#include<unordered_map>
#include <set>
using namespace std;


#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rev(j,n) for(int (i)=j;(i)>=(int)(n);--(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#define rerm(i,l,u,m) for(int (i)=(int)(l);(i)<=(int)(u);(i)+=(m))
typedef long long int lli;
typedef long long ll;
typedef unsigned long long int ulli;
#define vec vector
#define pii pair<int,int>
#define pis pair<int, string>
#define psi pair<string,int>
#define pli pair<lli,lli>
typedef vec<int> vi;
typedef vec<vi > vii;
typedef vec<pii > vpii;
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define modu 1000000007
#define endl "\n"
#define fir first
#define sec second


int main(){

    ofstream fout ("B-large.out");
    ifstream fin ("B-large.in");
    ulli l,r,n,t,m,k;
    string s;
    fin>>t;
    rep(i,t){
        fin>>s;
        fout<<"Case #"<<i+1<<": ";
        n = s.length();
        int counter=0;
        rep(i,n-1){
            if(s[i]!=s[i+1]){
                counter++;
                //cout<<i;
            }


        }
        if(s[n-1]=='-')
            counter++;
        fout<<counter<<endl;
    }

    fin.close();
    fout.close();


    return 0;
}
