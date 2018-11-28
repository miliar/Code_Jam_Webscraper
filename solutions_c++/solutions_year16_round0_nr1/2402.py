
#include <iostream>

using namespace std;


int main()
{
    int n,num,count,curr,countt;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        count=0;
        countt=0;
        int a[10]={0};
        cin>>num;
        if(num==0)
        {
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        do
        {
            countt+=num;
            curr=countt;
            while(curr>0)
            {
                if(a[curr%10]==0)
                {
                    count++;
                    a[curr%10]=1;
                }
                curr=curr/10;
            }
        }
        while(count<10);
        cout<<"Case #"<<i<<": "<<countt<<endl;
    }
    
    return 0;
}