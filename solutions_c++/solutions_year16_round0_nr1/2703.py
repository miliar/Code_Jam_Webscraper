#include <bits/stdc++.h>
#define ull unsigned long long
using namespace std;

void check_digit(int* arr,ull n)
{
    int temp=0;
    while(n>0)
    {
         temp=n%10;
         if(arr[temp]==0)
         {
             arr[temp]=1;
         }
         n=n/10;
    }
}

bool go_to_sleep(int* arr)
{
    bool flag=true;
    for(int j=0;j<10;j++)
    {
        if(arr[j]==0)
        {
            flag=false;
            break;
        }
    }
    return flag;
}

int main()
{
    ios::sync_with_stdio(0);
    ifstream in;
    in.open("A-large.in");
    ofstream out;
    out.open("output.out");

    int t;in>>t;
    for(int i=1;i<t+1;i++)
    {
        ull n;in>>n;
        if(n==0)
        {
            out<<"Case #"<<i<<": INSOMNIA\n";
        }
        else
        {
            int arr[10]={0};
            bool flag=false;
            for(ull j=1;j<100000;j++)
            {
                ull x=n*j;
                check_digit(arr,x);
                if(go_to_sleep(arr))
                {
                    out<<"Case #"<<i<<": "<<x<<"\n";
                    flag=true;
                    break;
                }
            }
            if(flag==false)
            {
                out<<"Case #"<<i<<": INSOMNIA\n";
            }
        }
    }
}
