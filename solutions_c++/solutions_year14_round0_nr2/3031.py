#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <limits>
#include <iomanip>

using namespace std;

int main()
{
    int i,j,k,l,m,n;
    int T,M,N,K,t1,t2,t3,t4,t5;
    long long ans,out;
    freopen("B-large.in","r",stdin);
    freopen("B_output.txt","w",stdout);
    long double F,C,X,minv,tv,rate,z;
    cin>>T;
    for(t1=1;t1<=T;++t1)
    {
        cin>>C>>F>>X;
        rate=2;
        minv = X;
        tv = X/rate;
        z = 0;
    	//cout<<tv<<" "<<z<<" "<<minv<<" "<<rate<<endl;
    	while(tv<=minv)
        {
            minv = tv;
            z += C/rate;
            rate += F;
            tv = z + X/rate;
        }
        printf("Case #%d: ",t1);
        cout << fixed << setprecision(7) <<minv<<endl;
    }

    return 0;
}
