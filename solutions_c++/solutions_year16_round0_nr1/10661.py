#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    long int n,n1,rem;
    long int a[500],b[500],count,num,x,y,i,j;
    bool check[10];
    long int c;
    x=0;
    bool flag;
    while(t--)
    {
    	
    flag=false;
    x++;
    for(i=0;i<10;i++)
    check[i]=false;
        count=0;
        cin>>n;
        n1=n;
        i=0;
        while(n>0)
        {
            a[count]=n%10;
            n/=10;
            count++;
        }
        for(i=0;i<count;i++)
        check[a[i]]=true;
        i=0;
        while(i<10)
        {
            if(check[i]==false)
            break;
            i++;
        }
        if(i==10)
        {
            flag=true;
            break;
        }
        for(j=0;j<100;j++)
        {
        rem=n1;
  //      cout<<"1";
        for(i=0;i<count&&rem>0;i++)
        {
            a[i]+=rem;
            if(a[i]>9)
            {
                rem=a[i]/10;
                a[i]%=10;
            }
            else 
            rem=0;
        }
        while(rem>0)
        {
            a[count++]=rem%10;
            rem/=10;
        }
        for(i=0;i<count;i++)
        check[a[i]]=true;
        i=0;
        while(i<10)
        {
            if(check[i]==false)
            break;
            i++;
        }
        if(i==10)
        {
            flag=true;
            break;
        }
        }
        if(flag==true)
        {
        cout<<"Case #"<<x<<": ";
        for(i=count-1;i>=0;i--)
        cout<<a[i];
        cout<<"\n";
        }
        else
        {
            cout<<"Case #"<<x<<": INSOMNIA\n";
        }



    }

    return 0;
}




