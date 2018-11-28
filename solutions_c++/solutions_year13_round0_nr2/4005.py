#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<ctime>
#include<cctype>
#include<cassert>
#include<climits>
#include<cerrno>
#include<cfloat>
#include<ciso646>
#include<clocale>
#include<csetjmp>
#include<csignal>
#include<cstdarg>
#include<cstddef>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<cwchar>
#include<cwctype>

//containers
#include<vector>
#include<list>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<complex>
#include<string>
#include<stack>
#include<bitset>
#include<istream>
#include<valarray>

//IOs
#include<iostream>
#include<sstream>
#include<iomanip>
#include<fstream>
#include<exception>
#include<ios>
#include<iosfwd>
#include<ostream>
#include<iterator>
#include<stdexcept>
#include<streambuf>


//algorithm & miscellaneous
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<limits>
#include<locale>
#include<memory>
#include<new>
#define pb push_back
#define mp make_pair
#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int test,n,m;
    cin>>test;
    int ca=1;
    while(test--){
        int flag1=0,flag2=0;
        cin>>n>>m;
        int a[n][m];
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                cin>>a[i][j];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                flag1=0,flag2=0;
                for(int k=0;k<m;k++){
                    if(a[i][j]<a[i][k]){
                            flag1=1;
                            break;
                    }
                }
                for(int k=0;k<n;k++){
                    if(a[i][j]<a[k][j]){
                        flag2=1;
                        break;
                    }
                }
                if(flag1==1 and flag2==1)
                    break;
            }
             if(flag1==1 and flag2==1)
                    break;

        }
        if(flag1==1 and flag2==1)
            cout<<"Case #"<<ca<<": NO\n";
        else
            cout<<"Case #"<<ca<<": YES\n";
        ca++;
    }
    return 0;
}
