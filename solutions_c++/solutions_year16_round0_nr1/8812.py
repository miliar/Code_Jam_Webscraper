#include <bits/stdc++.h>
//ifstream fin("A-small-attempt0.in")
//ofstream fout("out.txt");
using namespace std;
bool marker[10];
bool flag;
void func(long long n)
{
    while(n!=0)
    {
        int x= n%10;
        marker[x] = true;
        n=n/10;
    }
    for(int i=0;i<10;++i)
        if(marker[i]==false)
        {
            flag = false;
            return;
        }
        flag = true;

}

int main()
{
    int test;
    cin>>test;
    for(int i=1;i<=test;++i)
    {
        long long n;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
        fill(marker,marker+10,false);
        long long mult=0;
        flag = false;
        while(flag==false)
        {
            mult++;
            func(n*mult);
        }
        cout<<"Case #"<<i<<": "<<n*mult<<endl;
    }
}

