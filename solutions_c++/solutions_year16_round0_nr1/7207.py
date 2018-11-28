#include<iostream>


using namespace std;

int check(bool a[],long long n)
{
    int updated=0;
    while(n>0)
    {
        long long temp=n%10;
        if(a[temp]==0)
        {
            a[temp]=1;
            updated+=1;
        }
        n/=10;
    }

    return updated;
}

int main()
{
    int t;
    cin>>t;

    for(int j=0;j<t;j++)
    {
        long long n;
        cin>>n;

        cout<<"Case #"<<(j+1)<<": ";
        if(n==0)
        {
            cout<<"INSOMNIA"<<endl;
        }
        else
        {
        bool a[10]={0};
        long long i=1;
        int done=0;

        while(true)
        {
            done+=check(a,i*n);
            if(done==10)
            {
                break;
            }
            i++;
        }

        cout<<(i*n)<<endl;
        }
    }
}
