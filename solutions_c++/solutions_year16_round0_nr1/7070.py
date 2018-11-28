#include <iostream>

using namespace std;
int check(int a[])
{
  for(int i=0;i<=9;i++)
  {
      if(a[i]==1)
        continue;
      else
        return 0;
  }
  return 1;
}
int main()
{
    int t,a[10],x,k=1,c=1,y;
    long long int n,temp;
    cin>>t;
    while(t--)
    {
        cin>>n;
        if(n==0)
        {
            cout<<"CASE #"<<k++<<": INSOMNIA"<<endl;
            continue;
        }
        c=1;
        for(int i=0;i<=9;i++)
            a[i]=0;

        while(1)
        {
            temp=n*c;
            y=temp;
            c++;
        while(temp!=0)
        {
            x=temp%10;
            a[x]=1;
            temp=temp/10;
        }

        if(check(a)==1)
            {
                cout<<"CASE #"<<k++<<": "<<y<<endl;


                break;
            }

        }
    }


    return 0;
}
