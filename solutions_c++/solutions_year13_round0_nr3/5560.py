#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int is_palin(int n)
{
    int ret=0,m=n;
    while(n)
    {
        ret=ret*10 +(n%10);
        n/=10;
    }
    return ret==m;
}
int main()
{
    int T,len;
    cin>>T;
    vector<int> v;
    for(int i=1;i*i<=1000;i++)
    {
        if(is_palin(i) && is_palin(i*i))
        v.push_back(i*i);
    }
    len=v.size();
    for(int cases=1;cases<=T;cases++)
    {
        int A,B;
        cin>>A>>B;
        int count=0;
        for(int i=0;i<len;i++)
        {
            if(v[i]>=A && v[i]<=B)
            count++;
        }
        cout<<"Case #"<<cases<<": "<<count<<endl;

    }

    return 0;
}
