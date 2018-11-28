#include<cstdio>
#include<string>
#include<vector>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<cctype>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<fstream>
#include<numeric>
#include<map>
#include<sstream>
#include<iterator>
#define M 100
using namespace std;
typedef long long  ll;

int main()
{
	freopen("D:\\in.txt","r",stdin);
	freopen("D:\\out.txt","w",stdout);
	ll i,j=1,k,t,r,l;
	cin >>t;
	while(t--)

    {
        k =0;
        cin >> r >> l;
        for(i=1;i;i++)
        {
            if(2*r+1<=l)
            {
                k++;

                l-= 2*r+1;
                r+=2;
            }
            else break;
        }
        printf("Case #%lld: %lld\n",j++,k);
    }
	return 0;
}
