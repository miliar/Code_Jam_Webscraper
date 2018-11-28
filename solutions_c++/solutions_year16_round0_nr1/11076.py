#include<iostream>
#include<map>

using namespace std;
int main()
{

    long int T,N,counter;
    

    cin>>T;
    
    for(counter=1;counter<=T;counter++)
    {
        cin>>N;
        map<long int,long int> flag;
        long int count=0,i=1,ans;

        if(N==0)
            cout<<"Case #"<<counter<<": INSOMNIA"<<endl;
        
        else
        {
            long int temp;
        label:if(count<10)
        {
            temp=ans=N*i;

            while(temp!=0)
            {
                if(flag[temp%10]!=1)
                {
                flag[temp%10]=1;
                    count++;
                }
                    temp=temp/10;
            }
        }
            else
            {
                cout<<"Case #"<<counter<<": "<<ans<<endl;
                continue;

            }
           // cout<<"N is "<<ans<<" count is "<<count<<endl;
            i++;
            goto label;
                
        }
    }
    
}