#include<bits/stdc++.h>
using namespace std;
int c=0;
int isprime(long long val)
{
    int i;
    for(i=3;i*i<=val;i+=2)
    {
        if(val%i==0)
            break;
    }
    if(i*i<=val)
        return i;
    return -1;
}
int eval(string s,int n,int arr[11])
{
    int i,k;
    for(k=2;k<=10;k++)
    {
        long long a=1,val=0;
    for(i=n-1;i>=0;i--)
    {
        val=val+(s[i]-'0')*a;
        a*=k;
    }

    int x=isprime(val);
    if(x==-1)
        return 0;
        else arr[k]=x;
    }

    return 1;
}
void solve(string s,int n,int i)
{
    if(i==0)
        {
            s+='1';
            solve(s,n,i+1);
        }
        else if(i==n-1)
        {
            int arr[11]={0};
            s+='1';
        //    cout<<s<<endl;
            if(c==50)
                return ;
            if(eval(s,n,arr))
                {
                    cout<<s<<" ";
                    int k;
                    for(k=2;k<=10;k++)
                    cout<<arr[k]<<" ";
                    cout<<endl;
                    c++;
                    if(c==50)
                        return ;
                }
        }
        else
        {
            if(c==50)
                return;
            solve(s+'0',n,i+1);
            solve(s+'1',n,i+1);
        }
}
int main()
{
    freopen("opc1.txt","w",stdout);
    int t=1,n=16,j=50,i=0;
    string s;
    cout<<"Case #1:\n";
    solve(s,n,i);
    return 0;
}
