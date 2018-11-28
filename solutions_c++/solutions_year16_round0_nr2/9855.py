#include <iostream>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<list>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<fstream>
#include<map>
#include<iomanip>
using namespace std;
#define whiel while
#define null NULL
#define eps 1e-8
#define INF 0x3f3f3f
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define read(x) scanf("%d",&x)
#define ll long long
using namespace std;


int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
	 int t;
	 cin>>t;

    for(int case_i=1;case_i<=t;++case_i)
    {

        string a ;
        cin>>a ;
        int times = 0 ;
         cout<<"Case #"<<case_i<<": ";
        for(int i=a.size()-1 ;i>= 0 ;i--)
        {
            if(a[i]=='-')
            {
                times++;
                for(int j=i-1 ;j>=0 ;j--)
                {
                    a[j]=a[j]=='+'?'-':'+';
                }


            }




        }
        cout<<times<<endl;


    }

    return 0;
}
