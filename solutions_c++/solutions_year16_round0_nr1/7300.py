#include <iostream>
#include <math.h>

#define ll long long

using namespace std;

int ar[10]={1,1,1,1,1,1,1,1,1,1},sum=45;

void divide(ll num)
{
    int digit;
    while(num>0)
    {
        digit=num%10;
        if (digit==0&&ar[digit]==1)
            ar[0]=0;
        else if (ar[digit]==1)
        {
            ar[digit]=0;
            sum=sum-digit;
         //   cout<<endl<<sum;
        }
        num=num/10;
    }
}

int main()
{
    int cases;
    ll num,j=1;
    cin>>cases;
    
    for(int i=1;i<=cases;i++)
    {
        cin>>num;
        if(num==0)
        {
            cout <<"Case #"<<i<<": INSOMNIA"<<endl;
            goto y;
        }
        else
        {
            x:
            divide(num*j);
            if(ar[0]==0 && sum==0)
            {
                cout <<"Case #"<<i<<": "<<num*j<<endl;
                goto y;
            }
            j=j+1;
            goto x;
        }
        y:
        sum=45;
        j=1;
        ar[0]=1;
        ar[1]=1;
        ar[2]=1;
        ar[3]=1;
        ar[4]=1;
        ar[5]=1;
        ar[6]=1;
        ar[7]=1;
        ar[8]=1;
        ar[9]=1;
    }
    return 0;
}
