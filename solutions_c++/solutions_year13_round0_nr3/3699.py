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
bool isPalin(ll a){
    stringstream ss;
    ss<<a;
    int zero=0;
    string z;
    string y=ss.str();
    string x=y;
    reverse(x.begin(),x.end());
    for(int i=0;i<x.size();i++){
        if(x[i]!='0')
            break;
        else
            zero++;
    }
    z=x.substr(zero,x.size());
    if(z==y)
        return true;
    return false;
}
int main(){
    ifstream cin("input3.txt");
    ofstream cout("output3.txt");
    int test;
    ll a,b;
    cin>>test;
    int ca=1;
    while(test--){
        int count=0;
        cin>>a>>b;
        for(ll i=sqrt(a);i<=sqrt(b);i++){
            if(isPalin(i)){
                if(i*i>=a and i*i<=b)
                    if(isPalin(i*i))
                        count++;
            }
        }
        cout<<"Case #"<<ca<<": "<<count<<"\n";
        ca++;
    }
    return 0;
}
