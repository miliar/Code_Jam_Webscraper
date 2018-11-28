#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{freopen("1.txt","r",stdin);
freopen("2.txt","w",stdout);
int t,i,size,count,pro=0;
cin>>t;
 while(t--)
    {count=0;
    pro++;
    char arr[107];
    cin>>arr;
    for(i=0;arr[i]!='\0';i++)
       {
        /* if(arr[i]=='+')
            {
            arr[i]=1;
            }
            else
            {
            arr[i]=0;
            }*/

       }
size=i;
     for(i=0;i<size-1;i++)
        {
           if(arr[i]!=arr[i+1])
             {
               count++;
                // arr[i]=arr[i+1];

             }

        }
        if(arr[size-1]=='-')
           count++;
    cout<<"Case #"<<pro<<": "<<count<<endl;


    }
return 0;
}
