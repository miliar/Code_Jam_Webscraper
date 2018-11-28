#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;

int main()
{
    /* uncomment the following two lines to fectch input from input.txt and write to output.txt (after you have completed rest of your code) */

    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t=1,T;
    cin>>T;
    while(T--)
    {
        int a[100]={0};
        int A,B,i=0,j=0;
        int C,temp;

              cin>>A; //Range Lower Limit
              cin>>B;  //Range Upper limit
              while(A<=B)
                {
                     C=0;
                     temp=A;
                     while(temp!=0)
                     {
                         C=C*10;
                         C=C+temp%10;
                         temp=temp/10;
                     }

                    if(A==C)
                        {   a[i]=A;
                            i++;
                        }

                A++;
                }

                int count=0,z;
                int D=0;
                for(j=0;j<i;j++)
                {
                     D=0;
                     z=sqrt(a[j]);
                     if((z*z)!=a[j])
                     continue;
                     temp=z;
                     while(temp!=0)
                     {
                         D=D*10;
                         D=D+temp%10;
                         temp=temp/10;
                     }

                    if(z==D)
                    count++;

                }

    cout<<"Case #"<<t++<<": "<<count<<endl;
    }

    return 0;
}

