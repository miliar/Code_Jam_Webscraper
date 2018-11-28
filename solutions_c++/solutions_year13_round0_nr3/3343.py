
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>        //max heap implementation
#include <limits.h>




#define pub push_back
#define pob pop_back
#define puf push_front
#define pof pop_front
#define mkp make_pair
#define fi first
#define se second
#define debug(a) { for( typeof(a.begin()) it = a.begin() ; it != a.end() ; it++ ) cout << *it << " "; cout << endl; }

using namespace std;

//class comparators for queue and others
class classcomp{
    public:
        bool operator() (const int& l, const int& r)const{
            return l<r;
        }
};

#define ll long long

int main()
{
    freopen("input1.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    long int a[]={0,1,2,3,11,22,101,111,121,202,212,
 1001,1111,2002,10001,10101,10201,11011,
 11111,11211,20002,20102,100001,
 101101,110011,111111,200002,1000001,
 1001001,1002001,1010101,1011101,
 1012101,
 1100011,
 1101011,
 1102011,
 1109111,
 1110111,
 1111111,
 2000002,
 2001002,
};

    long long b[100];
    for(int i=0;i<41;++i)
    b[i]=pow(a[i],2);

    /*for(int i=0;i<41;++i)
    //cout<<b[i]<<endl;*/

    long long n,c=0,p,q;
    cin>>n;
    for(int i=0;i<n;++i)
    {   c=0;
        cin>>p>>q;
        for(int j=0;j<41;++j)
        {
            if(b[j]>=p && b[j]<=q)
            c++;
        }
        cout<<"Case #"<<i+1<<":"<<" "<<c<<endl;
    }



}
