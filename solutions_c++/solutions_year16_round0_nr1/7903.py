#include<iostream>
using namespace std;
void count(int num , int x[])
{
    while(num>0)
    {
        x[num%10]++;
        num/=10;
    }
    return;
}
bool check(int x[])
{
    bool ret = true;
    for(int i=0 ; i<10 ; i++)
    {
        if(x[i]==0)
        {
            ret = false;
        }
    }
    return ret;
}
int main()
{
    int t;
    cin>>t;
    for(int i=1 ; i<=t ; i++)
    {
        int n;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        }
        else
        {
            int x[10] = {0};
            int y = n;
            count(y,x);
            while(!check(x))
            {
                y += n;
                count(y,x);
            }
            cout<<"Case #"<<i<<": "<<y<<endl;
        }
    }
    return 0;
}
