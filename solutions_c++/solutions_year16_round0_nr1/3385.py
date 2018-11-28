#include <iostream>
using namespace std;

int main() {
    long long int res,cnt,n,t,num,temp,dt,a[15],i,j,x;
    cin>>t;
    dt=t;
    while(t--)
    {
        for(i=0;i<15;i++)
        a[i]=0;
        cin>>n;
        num=n;
        if(n==0)
        res=0;
        else
        {
            cnt=0;
            j=1;
            while(cnt!=10)
            {
                temp=num;
                while(temp>0)
                {
                    x=temp%10;
                    if(a[x]==0)
                    {
                        cnt++;
                        a[x]=1;
                    }
                    temp=temp/10;
                }
                if(cnt==10)
                {
                    res=num;
                    //break;
                }
                j++;
                num=j*n;
            }
        }
        if(res==0)
        cout<<"Case #"<<dt-t<<": INSOMNIA"<<endl;
        else
        cout<<"Case #"<<dt-t<<": "<<res<<endl;
    }
	return 0;
}
