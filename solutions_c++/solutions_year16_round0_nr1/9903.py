#include<bits/stdc++.h>
using namespace std;

int number[10];

long long unsigned int calculate(int x)
{
    if(x==0)
        return -1;
    long long unsigned int r=x,cx=x;
    int cont = 0,rep=0,brk=0;
    for(int i=0;i<10;i++)
        number[i]=0;
    while(cont <10)
    {
        while(x)
        {
            if(number[x%10]==0)
            {
                cont++;
                number[x%10]=1;
                x=x/10;
            }
            else
                x=x/10;
        }
        rep++;
        x=r+cx;
        r=x;
        //brk++;
        //cout<<r<<"\t"<<cont<<"\t";
    }
    if(brk == 1000)
        r=-1;
    else
        r=r-cx;
    //cout<<endl;
    return r;
}

int main()
{
    int t,i=0;
    long long unsigned int a;
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    cin>>t;
    //t=10000;
    while(i<t)
    {

        cin>>a;
        long long unsigned int x=calculate(a);
        i++;
        if(x == -1)
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else
        {
            cout<<"Case #"<<i<<": "<<x<<endl;
        }
    }
}
