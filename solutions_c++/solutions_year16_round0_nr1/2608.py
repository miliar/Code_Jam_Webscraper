#include <iostream>
using namespace std;

int main()
{
    int t,it=1;
    long long int n,c;
    cin>>t;
    while(it<=t)
    {
        int hash[10]={0};
        cin>>n;

        int flag=0;
        if(n==0)
        {
            flag=1;
            cout<<"Case #"<<it<<": "<<"INSOMNIA"<<endl;
        }
        for(int i=1;flag==0;i++)
        {
            c=i*n;
            //cout<<c<<endl;
            while(c>0)
            {
                int digit=c%10;
                hash[digit]++;
                c=c/10;
            }
            int count=0;
            for(int j=0;j<10;j++)
            {
                //cout<<hash[j]<<" ";
                if(hash[j]!=0)
                count++;
            }
            //cout<<endl;
            if(count==10)
            flag=1;

            if(flag==1)
            {
                cout<<"Case #"<<it<<": "<<i*n<<endl;
                break;
            }
        }
        it++;
    }
}
