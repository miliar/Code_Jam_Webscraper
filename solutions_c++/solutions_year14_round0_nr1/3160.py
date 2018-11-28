#include <iostream>
#include <algorithm>
using namespace std;

//#define MY_TEST

int main()
{
    #ifndef MY_TEST
    freopen("input.in","rt",stdin);
    freopen("output.txt","wt",stdout);
    #endif // MY_TEST

    int T,a,b,ar1[4],ar2[4],i,j,t,w,k;
    cin>>T;
    for(k=1;k<=T;++k)
    {
        cin>>a;
        for( i=1;i<=4;++i)
        {
            for(j=0;j<4;++j)
            {
                if(i!=a)
                {
                    cin>>t;
                }
                else
                {
                    cin>>ar1[j];
                }
            }
        }
        sort(ar1,ar1+4);
        cin>>b;
        for( i=1;i<=4;++i)
        {
            for(j=0;j<4;++j)
            {
                if(i!=b)
                {
                    cin>>t;
                }
                else
                {
                    cin>>ar2[j];
                }
            }
        }
        sort(ar2,ar2+4);
        w=0; //Common
        for(i=0;i<4;++i)
        {
            for(j=0;j<4;++j)
            {
                if(ar1[i]==ar2[j])
                {
                    ++w;
                    t=ar1[i];
                }
                else if(ar2[j]>ar1[i])
                    break;
            }
        }
        cout<<"case #"<<k<<": ";
        if(w==1)
        {
            cout<<t<<endl;
        }
        else if(w==0)
        {
            cout<<"Volunteer cheated!"<<endl;
        }
        else
        {
            cout<<"Bad magician!"<<endl;
        }
    }

    return 0;
}
