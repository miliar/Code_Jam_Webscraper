#include<iostream>
#include<cstdio>
#define X 1100000
using namespace std;

int all[10];
int mat[X];
void check(int number)
{
    int newn=number;
    int mod;
    while(number>0)
    {
        mod=number%10;
        number/=10;
        all[mod]=1;
    }
}

int main()
{
    freopen("ain.txt","r",stdin);
    freopen("aout.txt","w",stdout);
    int test,n,i,j,k;
    bool breaking;
    for(k=1; k<X; k++)
    {
        for(i=0; i<10; i++)
        {
            all[i]=false;
        }
        n=k;

        for(i=1;; i++)
        {
            check(n*i);
            breaking=true;
            for(j=0; j<10; j++)
            {
                if(all[j]==0)
                {
                    breaking=false;
                }
            }
            if(breaking==true)
            {
                break;
            }
        }
        mat[n]=n*i;
    }
    cin>>test;
    for(i=0; i<test; i++)
    {
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        }
        else
        {
            cout<<"Case #"<<i+1<<": "<<mat[n]<<endl;
        }
    }
    fclose(stdout);
    return 0;
}
