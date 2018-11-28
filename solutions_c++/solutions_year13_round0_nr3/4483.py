#include <iostream>

using namespace std;

int palind(int i)
{
    if(i>=1000)
        return 0;
    if(i/100 != 0)
        return i/100 == i%10;
    if(i/10 != 0)
        return i/10 == i%10;
    return 1;
}

int main()
{
    int t,n;
    int ans[1001]={0};
    int i,j;
    for(i=1; i<=1000; i++)
    {
        if( i*i > 1000)
            break;
        if( palind(i) && palind(i*i))
            ans[i*i]=1;
    }
    cin>>n;
    t=1;
    while(t<=n)
    {
        cin>>i>>j;
        int cnt=0;
        for(; i<=j; i++)
            if(ans[i]==1)
                cnt++;
        cout<<"Case #"<<t<<": "<<cnt<<endl;
        t++;
    }
    return 0;
}
