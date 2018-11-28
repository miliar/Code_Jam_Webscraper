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
#include<fstream>

using namespace std;

typedef long long int ll;
ll power(ll a)
{
    return(a*a);
}

int main()
{
    ofstream fout ("test.out");
    ifstream fin ("A-small-attempt1.in");
    ll r,t,i,index;
    int cases,cno;
    fin>>cases;
    for(cno=1;cno<=cases;cno++)
    {
        fin>>r>>t;
        ll sum= 0;
        for(index=1,i=0;;i+=2,index++)
        {
//            cout<< pow(r+i,2)<<"  ";
//            cout<<pow(r+i+1,2)<<"\n";

            sum+= power(r+i+1)-power(r+i);
            //cout<<"sum "<<sum<<" i= "<<i<<" index= "<<index<<"\n";
            if(sum>t)
            {
                break;
            }

        }
        fout<<"Case #"<<cno<<": "<<index-1<<"\n";


    }

    return 0;
}
