#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <vector>

namespace std
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

using namespace std;

int main()
{
    //freopen("test", "r", stdin);
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int testCases;
    cin>>testCases;
    for(int testcase=0;testcase<testCases;testcase++)
    {
        int s;
        string a;
        cin>>s>>a;
        //cout<<s<<" "<<a<<endl;
        int sum=0,diff=0;
        for(int i=0;i<=s;i++)
        {
            //cout<<"sum="<<sum<<" a[i]="<<a[i]<<" diff="<<diff<<endl;
            if(sum<i && a[i]!='0') {
                diff+=i-sum;
                sum+=diff;
            }
            sum+=a[i]-'0';
        }
        cout<<"Case #"<<testcase+1<<": "<<diff<<endl;
    }
    return 0;

}
