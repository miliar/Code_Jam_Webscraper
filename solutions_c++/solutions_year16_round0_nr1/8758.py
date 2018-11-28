#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

#define len(x) ((int)(x.size()))
#define inf 1061109567


string tostr(long long  a){if(a==0) return "0";string ret;for(long long  i=a; i>0; i=i/10) ret.push_back((i%10)+48);reverse(ret.begin(),ret.end());return ret;}



int main(){
    ios_base::sync_with_stdio(0);
freopen("in.txt", "r", stdin);
freopen("out.txt", "w", stdout);

    int tst;
    cin>>tst;
    for(int i=1;i<=tst;i++){
        cout<<"Case #"<<i<<": ";
        long long num;
        cin>>num;
        map<char,int> m;
        for(int i=1;i<100000;i++){
            long long n=num*i;
            string s=tostr(n);
            for(int j=0;j<s.size();j++){
                m[s[j]]=1;
            }
            if(m.size()==10){
                cout<<n<<endl;
                goto hell;
            }
        }
        cout<<"INSOMNIA"<<endl;
hell:;
    }

}


