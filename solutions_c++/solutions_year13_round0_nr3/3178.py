/*
| Problem Status : UNSOLVED
|
|
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<iterator>
#include<vector>
#include<string>
#include<sstream>
#include<set>
#include<deque>
#include<cstring>
#include<cstdlib>


#define FOR(i,v,n) for(int i=v;i<n;++i)
#define PVector(arr,type) copy(arr.begin(),arr.end(),ostream_iterator<type>(cout," "));
#define swap(a,b) { a=a^b; b=a^b; a=a^b; }

using namespace std;
typedef long long ll;

ll sqrt(ll n)
{
    ll i=1;
    for(;i*i<=n;++i);
    return i-1;
}

bool ispalin(string s)
{
    for(int i=0,j=s.size()-1; i<j ; ++i,--j)
    if(s[i]!=s[j]) return false;

    return true;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);

    int t;cin>>t;

    ll a,b;
    for(int ii=1;ii<=t;++ii)
    {
        cin>>a>>b;

        ll s=sqrt(a),c=0;
        if(s*s<a) ++s;
        for(ll i=s;i*i<=b;++i)
        {
            ostringstream str1,str2;
            str2<<i;
            str1<<(i*i);
            if( ispalin(str1.str()) && ispalin(str2.str()) ) ++c;
        }
        cout<<"Case #"<<ii<<": "<<c<<endl;
    }



    return 0;
}
