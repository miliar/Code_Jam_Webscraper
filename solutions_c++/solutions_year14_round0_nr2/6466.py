
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
        
        double c,f,x,speed=2.0,now,then,buyC,time=0.0000;
        cin>>c>>f>>x;
    
        if(x<=c)
        {
            time=x/speed;
             printf("%.9f\n",time);
            continue;
        }
        
        while(1)
        {
            now=x/speed;
            buyC=c/speed;
            if(buyC+(x/(speed+f))<now)
            {
                time+=buyC;
                speed+=f;
                
            }
            else
            {
                time+=x/speed;
                break;
                
            }
            
            
        }
        
        printf("%.9f\n",time);
        
    }
    return 0;
}










