#include <bits/stdc++.h>
using namespace std;
long long int prime( long long int k)
    {
    long long int i;
    if(k==2||k==3||k==5)
        return(1);
    else if(k%2==0||k%3==0||k%5==0||k==1)
        {
        return(0);
    }
    else
        {
        for(i=6;i*i<=k;i=i+6)
            {
            if(k%(i+1)==0)
               {return(0);}
               else if((k%(i+5))==0)
               {return(0);}
        }
    }
    return(1);
}

int main()
    {
long long int i,t,n,j,z,f,k,ki,m,r,c,x=0,y,a[100000],g;
    cin>>t;
    for(i=0;i<t;i++)
        {
       cin>>n>>j;cout<<"Case "<<"#"<<i+1<<":\n";
        x=0;f=1;g=32769;
        for(z=0;z<j;)
            {
              std::bitset<16> si (g);
            std::string s =si.to_string<char,std::string::traits_type,std::string::allocator_type>();
                            
              f=1;x=0;g+=2;             
             for(r=2;r<=10;r++)
                {
                 c=0;
               for(k=n-1,m=0;k>=0;k--,m++)
                   {
                   if(s[k]!='0')
                       {c=c+pow(r,m);}
                   }              
                  if(prime(c)==1)
                  {f=0;r=11;}
                  else
                      {
                     // cout<<c<<endl;
                     if(c%2==0)
                      {a[x]=c/2;x++;}
                     else
                         {
                          y=3;
                         while(c%y!=0)
                             {
                              y++;
                             }
                            a[x]=y;x++;
                         }
                     }
                }
               if(f==1)
                   {
                     cout<<s<<" ";z++;
                     for(ki=0;ki<9;ki++)
                      cout<<a[ki]<<" ";
                    cout<<endl;
                   }                    
        }          
      }
    return 0;
}