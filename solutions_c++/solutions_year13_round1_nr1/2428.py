#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    int T;
    long long r,t;
    long long parea;
    long long ans;
    long long  pans;
    long long beg,end,mid;
    int i;
    cin>>T;
    for(int k=1;k<=T;k++)
    {
        cin>>r>>t;
        cout<<"Case #"<<k<<": ";
        parea=(2*r)+1;
        if(t==parea)
        {
            cout<<1<<endl;
        }
        else
        {
            /*ans=parea;
            if(r<=1000000000)
            ans=(sqrt(4*r*r+8*t)-(2*r))/4;
            cout<<ans<<endl;*/
            /*beg=2;//1414213562
            end=1414213562;
            mid=(beg+end)/2;
            while(beg<end)
            {
                pans=ans;
                ans=(parea+(mid-1)*2)*mid;
                if(ans==t)
                {
                    break;
                }
                else if(ans<t)
                {
                    beg=mid+1;
                    if(beg<=end)
                    mid=(beg+end)/2;
                }
                else
                {
                    end=mid-1;
                    if(beg<=end)
                    mid=(beg+end)/2;
                }
            }
            if(ans==t)
            {
                cout<<mid<<"ashfgk"<<endl;
            }
            else
            {
                cout<<mid-1<<endl;
            }*/
            for(i=2;i<=707106780;i++)
            {
                pans=ans;
                ans=(((parea)+(i-1)*2)*i);
                if(ans==t)
                {
                    cout<<i<<endl;
                    break;
                }
                if(ans>t)
                {
                    cout<<i-1<<endl;
                    break;
                }
            }
        }
    }
    return 0;
}
