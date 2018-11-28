#include<iostream>
#include<fstream>
using namespace std;
long long int a[16],ans[9];
bool ispossible()
{

    long long int val=0,pow,i;
    int j,k;
    for(j=2;j<=10;j++)
    {
        pow=1;val=0;
        for(i=15;i>=0;i--)
    {
        val=val+a[i]*pow;
        pow*=j;
    }
    for(i=2;i<val;i++)
    {
        if(val%i==0)
        {
            ans[j-2]=i;
            break;
        }
    }
    if(i==val)
        return 0;
    }
    if(j==11)
    {
        //cout<<"yes";

        return 1;}
}
int main()
{
    int t,n,i,j,k,p,q,c=1,count;
    //ofstream out;
    //out.open("jamsmall.out");
    cin>>t;
    while(t--)
    {
        cin>>n>>j;
        count=0;
        cout<<"Case #"<<c<<":\n";
        c++;
        for(i=n-3;i>0&&j>count;i--)
        {//cout<<i<<endl;
            for(k=0;k<n;k++)
            {
                if(k!=i)
                    a[k]=1;
                else
                    a[k]=0;
            }
            if(ispossible()) {count++;k=j;
            for(j=0;j<16;j++)
            cout<<a[j];
        for(j=0;j<9;j++)
            cout<<" "<<ans[j];
        cout<<endl;
        j=k;}
        }
        //ccout<<count<<endl;
        for(i=n-3;i>0&&j>count;i--)
        {//ccout<<i<<endl;;


            for(p=i-1;p>0&&j>count;p--)
            {
               for(k=0;k<n;k++)
            {
                if(k!=i&&k!=p)
                    a[k]=1;
                else
                    a[k]=0;
            }
            //ccout<<"func"<<endl;
            if(ispossible()) {count++;k=j;
            for(j=0;j<16;j++)
            cout<<a[j];
        for(j=0;j<9;j++)
            cout<<" "<<ans[j];
        cout<<endl;
        j=k;}
            }

        }

        for(i=n-3;i>0&&j>count;i--)
        {


            for(p=i-1;p>0&&j>count;p--)
            {
                for(q=p-1;q>0&&j>count;q--)
                {
                    for(k=0;k<n;k++)
            {
                if(k!=i&&k!=p&&k!=q)
                    a[k]=1;
                else
                    a[k]=0;
            }
            //ccout<<"func"<<endl;
            if(ispossible()) {count++;k=j;
            for(j=0;j<16;j++)
            cout<<a[j];
        for(j=0;j<9;j++)
            cout<<" "<<ans[j];
        cout<<endl;
        j=k;}
                }

            }

        }

    }
    return 0;
}
