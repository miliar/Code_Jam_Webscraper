#include<iostream>
#include<math.h>
using namespace std;

int main()
{
    int i,j,t,s,b[6],clap[6];
    long int a;int p=1,k=0,count=0,temp=0;
    cin>>t;
    while(t>0)
    {
        cin>>s;
        cin>>a;
        for(i=0;i<=s;i++)
        {
            b[i]= a%10;
            a=a/10;
        }
        for(j=0;j<=s;j++)
        {
            clap[j]=b[i-1];i--;
        }
         temp=0;count=0;
        for(i=0;i<=s;i++)
        {
           if(count>=i && clap[i]>0)
           {
               while(clap[i]>0){count++;
               clap[i]--;}
           }
           
           if(count<i && clap[i]>0)
           {
               temp+= i-count;
               count+=temp;
                if(i==count)
                {
                    while(clap[i]>0)
                    {
                        clap[i]--;count++;
                    }
                }
                
           }
           
        }
        cout<<"Case #"<<p<<":"<<" "<<temp<<endl;
        p++;
       
        t--;
    }
    return 0;
}