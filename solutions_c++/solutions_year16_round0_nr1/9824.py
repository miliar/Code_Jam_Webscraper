#include<stdio.h>
#include<sstream>
#include<string>

namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}
#include<iostream>
using namespace std;
int main()
{
    long int t,x,y,j=1,flag=0;
      int n;
    scanf("%ld",&t);

    for(int i=1;i<=t;i++)
    {       long int a[70]={0};
            scanf("%d",&n);
            if(n==0)
            {
            printf("Case #%d: INSOMNIA\n",i);
            }
            else
            {
                while(flag!=10)
                {
                    x=j*n;
                    string s= patch::to_string(x);
                    //cout<<s<<"\n";//y=strlen(s);
                    for(int k=0;k<=5;k++)
                    {
                        for(int l=48;l<=57;l++)
                        {
                            if((s[k]==l)&&(a[l]==0))
                            {   //cout<<l<<"\n";
                                a[l]++;
                                flag++;
                            }
                        }
                    }
                  //cout<<j<<"\n"  ;
                 j++;
                }


                printf("Case #%d: %ld\n",i,x);
                flag=0;
                j=1;

            }

    }

    return 0;
}
