#include <bits/stdc++.h>
using namespace std;
int main()
{

    int t,i=1;
    cin>>t;
    while(i<=t)
    {
        int n,arr[10]= {0};;
        cin>>n;
        if(n<=0)cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else
        {   int new_val=1,sum;
            while(true)
            {
                int key=0,end_time=0;
                sum= n *new_val;
                int rem,j=sum;
                while(sum !=0)
                {
                    rem=sum%10;

                    if(arr[rem] ==0)
                    {
                        arr[rem]=1;

                    }

                    sum/=10;
                }

                for(int k=0; k<10; k++)
                    if(arr[k]==0)break; else  key++;                
                 
                if(key == 10)
                {  cout<<"Case #"<<i<<": "<<j<<endl;
                    end_time++; break;
                } 
                if(end_time>0 )break;
                new_val+=1;
            }

        }
        i++;
    }




    return 0;
}
