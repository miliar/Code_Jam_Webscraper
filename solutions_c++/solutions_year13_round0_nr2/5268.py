//#includes {{{
#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <numeric>
#include <complex>
#include <list>
#include <stack>
#include <queue>
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <cassert>
using namespace std;
// }}}
// #defines {{{
#define sz(a) int((a).size())
#define pb push_back

#define all(c) (c).begin(),(c).end()
#define FOR(i,a,b) for (int i=a; i<(int(b)); i++)
#define tr(it, container) \
    for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define trb(it, container) \
    for(typeof(container.rbegin()) it = container.rbegin(); it != container.rend(); it++)

#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef long long ll;
typedef complex<double> pnt;

template<class T>
void splitline(const string &s, vector<T> &dest) {
    istringstream in(s);
    dest.clear();
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(dest));
}
template<class T>
inline void PRINT_ELEMENTS(const T& coll, const char* optcstr=""){
    typename T::const_iterator pos;
    std::cout<< optcstr;
    for(pos=coll.begin();pos!=coll.end();++pos){
        cout << *pos << ' ';
    }
    cout << endl;
}
template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
int s2i(string str){
    stringstream ss; int n;
    ss << str; ss >> n; return n; }
string i2s(int n){
stringstream ss; string str;
ss << n; ss >> str; return str; }
// }}}

int main(int argc, char*argv[]){
    //codejam
    int t;
    scanf("%d\n",&t);
    for(int z=0;z<t;z++) {
        int n,m;
         scanf("%d %d",&m,&n);
        int a[m][n];
        memset(a, 100, sizeof a);
        int cc;
        set<int> p;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++) {
                scanf("%d",&cc);
                a[i][j] =cc;
                p.insert(cc);
            }
        }
        int res=0;
        int f1=0,f2=0;
        for(typeof(p.rbegin()) it = p.rbegin(); it != p.rend(); it++){
            int max1=*it;
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++) {
                    if(a[i][j]==max1){
                        f1=0,f2=0;
                        //row wise
                        for(int z1=0;z1<n;z1++)
                            if(a[i][z1]>max1){ f1=1; break; }
                        //column wise
                        for(int z1=0;z1<m;z1++)
                            if(a[z1][j]>max1){ f2=1; break; }
                        if(f1==0 || f2==0) res=0;
                        if(f2==1 && f1==1){ res=1; break;}
                    }
                        if(f2==1 && f1==1){ res=1; break;}
                }
                        if(f2==1 && f1==1){ res=1; break;}
            }
                        if(f2==1 && f1==1){ res=1; break;}
        }
        printf("Case #%d: ",z+1);
        switch(res){
            case 0: printf("YES");
                    break;

            case 1: printf("NO");
                    break;
        }
        printf("\n");
    }
}

// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread


