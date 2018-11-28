#include<iostream>

using namespace std;

int n,results[101],l;


void digit (int a, int k[])
{
    int c=a;
    while(c>0)
    {
        k[c%10]=1;
        c-=c%10;
        c/=10;
    }
}
int count (int k[])
{
    int wyn=0;
    for(int i=0; i<=9; i++)
    {
        if(k[i]) wyn+=1;
    }
    return wyn;
}

void clear(int k[])
{
    for(int i=0; i<=9; i++) k[i]=0;
}

long long base (int a)
{
    int x=a;
    int tab[10];
    clear(tab);
    digit (x, tab);
    while(count(tab)<10)
    {
        x+=a;
        digit (x, tab);
    }
    return x;
}


int main()
{
    cin>>n;
    for(int i=1; i<=n; i++)
    {
        cin>>l;
        if(l!=0)
        {
            results[i]=base(l);
        }
    }
    for(int i=1; i<=n; i++)
    {
        if(results[i]!=0)
        {
            cout<<"Case #"<<i<<": "<<results[i]<<endl;
        }
        else cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;

    }
    return 0;
}
