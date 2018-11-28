#include<iostream>
#include<bits/stdc++.h>
#include<algorithm>
#include<vector>
#include<map>

#define llong long long
#define f1(i,n) for(i=1;i<=n;i++)
#define f0(i,n) for(i=0;i< n;i++)
using namespace std;


int main()
{
        int T,N;
        cin>>T;
        char S1[1001][21];
        char S2[1001][21];
        
        char first[21],second[21];
        int t;
        int f;
        f1(t,T)
        {       cin>>N;
                int i;
                int tot=0;
                int one=0,two=0;
                int j;
                f0(i,N)
                      cin>>S1[i]>>S2[i];
                
        
                f0(i,N)
                {       f=0;
                        f0(j,N)
                        if(j!=i)
                        {      if(!strcmp(S1[i],S1[j]))
                               {         f=1; 
                                         break;
                               }
                        }
                        if(f==1)
                        f0(j,N)
                        if(j!=i)
                        {      if(!strcmp(S2[i],S2[j]))
                               {         f=2; 
                                         break;
                               }
                        }
                        if(f==2)tot++;               
                }
                cout<<"Case #"<<t<<": "<<tot<<endl;
        }
        return 0;
}
