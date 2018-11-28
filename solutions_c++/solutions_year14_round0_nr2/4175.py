#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cmath>
#include <stdio.h>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <limits.h>
#define ll long long int
#define mod 1000000009
using namespace std;


int main()
{

  //freopen("C:\\Users\\jack\\Desktop\\large.txt","r",stdin);
 //freopen("C:\\Users\\jack\\Desktop\\out201.txt","w",stdout);

    int test,test_case=1;
    scanf("%d",&test);
    while(test_case<=test)
    {
        
        double c,f,x;
        
        scanf("%lf%lf%lf",&c,&f,&x);
        
        double temp=x/2.0;
        double temp1=c/2.0;
        
        for(int i=1;;i++)
        {
                if(temp>(temp1+(x/(i*f+2.0))))
                {
                                            temp=(temp1+(x/(i*f+2.0)));
                                            temp1+=(c/(i*f+2.0));
                                            
                }
                else
                break;
        }
        printf("Case #%d: %.7lf\n",test_case,temp);              
        test_case++;           
        
    }
    
}  
