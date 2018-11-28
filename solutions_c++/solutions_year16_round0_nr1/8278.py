//============================================================================
// Name        : codejam.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;
#define ll long long int
int main() {

	ll t,dig,i;string k; bool x[10];bool r=false;
    cin>>t;
   // getline(cin,k);
    for( i=1;i<=t;i++)
    {  r=false;
    printf("Case #%d: ",i);
    	 for(ll j=0;j<=9;j++)
    	 {
    		 x[j]=false;
    	 }
            ll n,g,u,o,y;
            cin>>n;
            g=n;y=n;

             while(g!=0)
             {
            	 y=g%10;
            	 x[y]=true;
            	// cout<<g<<" ";
            	 g=g/10;
             }

        	 if(x[0] && x[1] && x[2] && x[3] && x[4] && x[5] && x[6] && x[7] && x[8] && x[9])
        		 printf("%lld",n);
            for(ll f=2;f<=15000;f++)
            {
              dig=f*n; u =dig;
               while(u)
               {
            	   o=u%10;
            	   x[o]=true;
            	   //cout<<o<<" ";
            	   u=u/10;
               }
         	 if(x[0] && x[1] && x[2] && x[3] && x[4] && x[5] && x[6] && x[7] && x[8] && x[9])
         	   {  printf("%lld",dig); r=true; break; }

            }
            if(r==false)
            	printf("INSOMNIA");
            printf("\n");
    }
	return 0;
}

