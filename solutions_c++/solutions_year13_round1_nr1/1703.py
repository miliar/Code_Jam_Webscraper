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
    //char a[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    long long r,t;
    cin>>n;
    for(int i=0;i<n;++i)
    {
        cin>>r>>t;
        long long  x=1,a=0,c=0,y=0;
        while(a<=t)
        {   if(a==0)
            x=x+r;
            else
            x=x+2;
            y=x-1;
            a=a+(pow(x,2)-pow(y,2));
            c++;
        }
    cout<<"Case #"<<i+1<<":"<<" "<<c-1<<endl;
    }


}
