#include<iostream>
using namespace std;
main()
{
    int T,i=2,j,res=0,k=1;
    long long no,temp1,temp2,temp;
    int arr[10];
    cin>>T;
   
    while(T--)
    {
        cin>>no;
        temp1=no;
        temp=temp1;
        i=2;
         for(j=0;j<10;j++)
        {
       arr[j]=0;
                
    }
        if(no==0)
        {
            cout<<"Case #"<<k<<": INSOMNIA\n";
        }
        else
        {   res=0;
        
            while(res<10)
            {   
                temp1=temp;
               while(temp1)
               {
                    temp2=temp1%10;
                    temp1=temp1/10;
                    if(arr[temp2]==0)
                     {  
                            arr[temp2]+=1;
                            ++res;
                      }
                      if(temp1==0 && res<10)
                      {   
                         temp=no*i;
                          i++;
                       }
                 
                }
                
            }
            cout<<"Case #"<<k<<": "<< temp<<"\n";
        }
        k++;
    }
}
