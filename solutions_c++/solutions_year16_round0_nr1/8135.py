#include <iostream>
using namespace std;
int chk(bool a[]);
int main()
{
    int n,j,i,num,d,count=1,flag;
    unsigned long temp,ans;
    bool digit[10];
    cin>>n;
    while(n--)
    {   for (i=0;i<10;i++)
         digit[i]=0;
         j=0;
         flag=0;
        cin>>num;
        if (num==0)
        {

           cout<<"Case #"<<count<<": INSOMNIA\n";
           count++;
           continue;
        }

        while(flag==0)
        { j++;
         temp=j*num;

        do
        {
            d=temp%10;
            temp=temp/10;
            digit[d]=1;
        }while(temp);
        flag=chk(digit);
        }
        ans=j*num;
        cout<<"Case #"<<count<<": "<<ans<<"\n";
        count++;
    }
    return 0;
}
int chk(bool a[])
{

    for(int i=0;i<10;i++)
    {
        if(a[i]==0)
        return 0;

    }
    return 1;
}

