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

  //freopen("C:\\Users\\jack\\Desktop\\in.txt","r",stdin);
 //freopen("C:\\Users\\jack\\Desktop\\out.txt","w",stdout);

    int test,ca;
    scanf("%d",&ca);
    test=1;
    
    while(test<=ca)
    {
            double cost,f,target,rate=2.0,cookie,prev,lest,estimated;
            scanf("%lf %lf %lf",&cost,&f,&target);
            
            prev=0;
            lest=target/2;
            
            while(1)
            {
                    
                    prev+=cost/rate;
                    
                    rate+=f;
                    estimated=prev+(target/rate);
                   // cout<<"es"<<prev<<" "<<estimated<<endl;
                    if(lest<=estimated)break;
                    lest=estimated; 
             }
 

         printf("Case #%d: %0.8lf\n",test,lest);
         test++;
                 }

    }
