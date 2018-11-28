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

#include<iomanip>
#include<fstream>
#include<numeric>
#include<map>
#include<sstream>
#include<iterator>
#define M 100
using namespace std;
typedef double  ll;
int main()
{
	freopen("D:\\a.in","r",stdin);
	freopen("D:\\o0.txt","w",stdout);
	 cout << setprecision(7) <<fixed;

	ll n,j,k,l  ,x,c,f,cs=1;
	int i,cd=1;
	cin >> n;
	while( n--)
    {
        printf("Case #%d: ",cd++);
        vector<ll> de;
        ll ma = 43545454545;
        cin >> c >> f >> x;
        if(x<= c)
            cout << x/2.0 <<endl;
        else
        {
            k = l =0;
            l = x/2.0;
            if(l<ma) ma =l;
            de.push_back(l);
            l =0;
            for( i = 0  ;i+1 ; i++)
            {
                k= 2+i*f;
                l+=c/k;
                j = l+ x/(2+(i+1)*f);
                if(j<ma) ma = j;
                else break;
               // de.push_back(j);
              //  cout << de.at(i) <<" ";
                if(x/(2+(i+1)*f)<.001) break;
            }
           // cout <<endl;
           // sort(de.begin(),de.end());
            cout << ma <<endl;
        }
    }
}
