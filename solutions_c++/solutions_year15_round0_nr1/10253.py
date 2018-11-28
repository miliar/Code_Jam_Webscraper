#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int maxs;
        cin>>maxs;
        int s;
        cin>>s;
        int a[maxs+1];
        for(int j=0;j<=maxs;j++)
        {
            a[maxs-j]=s%10;
            s=s/10;
        }
        int counter=0;
        int sum=0;
        for(int j=0;j<=maxs;j++)
        {
            if(sum<j)
            {
                counter+=j-sum;
                sum+=j-sum;
            }
            sum+=a[j];
        }
        cout<<"Case #"<<i+1<<": "<<counter<<"\n";
    }
    return 0;
}
