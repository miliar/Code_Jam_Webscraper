#include<iostream>
using namespace std;
int main()
{
    int t,t1;
    cin>>t;
    t1=t;
    while(t--)
    {
        int n;
        cin>>n;
        int a[10];
        if (n==0) cout<<"Case #"<<t1-t<<": INSOMNIA"<<endl;
        else{
        for (int j=0;j<10;j++) a[j]=0;
        int i=1,k;
        while(1)
        {
            k=n*i;
            while(k!=0)
            {
                int rem=k%10;
                a[rem]=1;
                k=k/10;
            }
            i++;
            if ((a[0]==1)&&(a[1]==1)&&(a[2]==1)&&(a[3]==1)&&(a[4]==1)&&(a[5]==1)&&(a[6]==1)&&(a[7]==1)&&(a[8]==1)&&(a[9]==1)) break;
        }
        cout<<"Case #"<<t1-t<<": "<<n*(i-1)<<endl;
    }
    }
}
