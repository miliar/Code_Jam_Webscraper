#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,t,flag,i;
    unsigned long long int temp,temp1;
    freopen("E:/A-large.in", "r", stdin);
	freopen("E:/output.txt", "w", stdout);
    cin>>t;
    set<int>Q;
    long long int ctr;
    for(i=1;i<=t;i++)
    {
        Q.clear();
        cin>>n;
        temp=temp1=n;
        while(temp1)
        {
            Q.insert(temp1%10);
            temp1/=10;
        }
        ctr=2;
        flag=0;
        while(Q.size()!=10)
        {
            temp=n*ctr;
            if(temp==n)
            {
                flag=1;
                break;
            }
            ctr++;
            temp1=temp;
            while(temp1)
            {
                Q.insert(temp1%10);
                temp1/=10;
            }
        }
        cout<<"Case #"<<i<<": ";
        if(flag==0)
            cout<<temp<<"\n";
        else
            cout<<"INSOMNIA\n";
    }
    return 0;
}
