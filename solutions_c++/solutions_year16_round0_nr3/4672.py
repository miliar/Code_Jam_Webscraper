#include<iostream>
#include<math.h>
#include<fstream>
using namespace std;
int main()
{
    unsigned long long int i,j,k,t,n;
    ifstream in("input.txt");
    ofstream out("outn.in");
    in>>t;
    for(i=1;i<=t;i++)
    {
        in>>n>>j;
        out<<"Case #"<<i<<": "<<endl;
        k=0;
       unsigned long long int d1=32769;
       unsigned  long long int d2=65535;
        if(n==32)
        {
        	d1=2147483649;
        	d2=4294967295;
		}
            for(int count =d1; count <=d2 ; count++)
                {
                   // cout<<"!";
                    // In the following loop we just basically print 'count' bit after bit.
                    int a[16];
                    unsigned long long int ans[9];
                    int ii=0;
                    for(int offset = 15; offset >= 0; offset--)
                        {
                                a[ii]=((count & (1 << offset)) >> offset);
                                ii++;
                        }
                     /* for(k=0;k<16;k++) 
                        	cout<<a[k];
                        	cout<<endl;*/
                        long int bs=2;
                        if(a[0]==1 && a[15]==1)
                     {  	
                        int flag=1;
                    while(flag==1 && bs<=10)
                    {
                        unsigned long long int  sum=0;
                        int indx=15;
                        for(k=0;k<16;k++)
                            {
                                sum+=(a[k]*pow(bs,indx));
                                indx--;
                            }
                         // cout<<sum<<endl;
                         unsigned long long int div=2;
                        int f2=1;
                        
                        while(f2==1 && div<=sqrt(sum))
                        {
                            if(sum%div==0 && sum>div)
                            {
                               f2=0;
                               ans[bs-2]=div;
                            }
                            div++;
                        }
                        if(f2==1)
                        {
                            flag=0;
                        }

                        bs++;
                    }
                   if(flag==1)
                   {
                       for(k=0;k<16;k++)
                        out<<a[k];
                       out<<" ";
                       for(k=0;k<9;k++)
                        out<<ans[k]<<" ";
                       out<<endl;
                       j--;
                   }
                   if(j==0)
                   	break;
			}
                }
    }
}

