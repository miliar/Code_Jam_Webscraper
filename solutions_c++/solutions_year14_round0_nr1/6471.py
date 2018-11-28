
// By Akash Verma

#include<iostream>
#include<ostream>
#include<cstdlib>
#include<stdio.h>
#include<fstream>
#include<iomanip>
#include<limits.h>
#include<map>
#include<math.h>
#include<string.h>
#include<sstream>
#include<string>
#include<set>
#include<algorithm>
#include<stack>
#include<deque>
#include<assert.h>
#include<vector>
#include<queue>

typedef long long int  lli;
using namespace std;


int main(int argc, const char * argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    lli t,caseno;;
    scanf("%lld",&t);

    
    for(caseno=1;caseno<=t;caseno++)
    {
        
        cout<<"Case #"<<caseno<<": ";
        lli i,j,a[4][4],b[4][4],r1,r2;
        
        map<lli,lli>check;
        
        scanf("%lld",&r1); r1--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%lld",&a[i][j]);
        
        scanf("%lld",&r2);  r2--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%lld",&b[i][j]);
        
        lli count=0,N=-1;
        
        for(j=0;j<4;j++)
            check[a[r1][j]]++;
        
        for(j=0;j<4;j++)
        {
            if(check[b[r2][j]]==1)
            {
                count++;
                N=b[r2][j];
            }
        }
        
        if(count==1&&N!=-1)
            printf("%lld\n",N);
        else if(count>1)
            printf("Bad magician!\n");
        else if(count==0)
            printf("Volunteer cheated!\n");

            
    }
    return 0;
}
