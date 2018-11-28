#include<iostream>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    int t,n; cin>>t;
    for(int j=1;j<=t;j++)
    {
        bool arr[10]={0},flag=0;
        cin>>n;
        long long tmp,tmp1=n,tmp2,cnt=0,i=1;
        while(cnt<10)
        {
            while(n>0)
            {
                tmp=n%10;
                if(arr[tmp]==false)
                {
                    arr[tmp]=true;
                    cnt++;
                }
                n/=10;
            }
            if(cnt==10)
                break;
            i++;
            n=tmp1*i;
            tmp2=n;
            if(n==tmp1)
            {
                flag=true;
                break;
            }
        }
        if(flag)
            cout<<"Case #"<<j<<": INSOMNIA\n";
        else
        {
            cout<<"Case #"<<j<<": "<<tmp2<<endl;
        }

    }
}
