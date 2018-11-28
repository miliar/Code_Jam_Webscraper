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

    long long T,Sm,k,i,ans,j;
    char inp[1005];
    cin>>T;
    for(k=1;k<=T;++k)
    {
        cin>>Sm;
        cin>>inp;
        ans=0;
        j=0;
        for(i=0;i<=Sm;++i)
        {
            if(j<i)
            {
                ans += (i-j);
                j =i;
            }
            j+= inp[i]-'0';
        }
        cout<<"case #"<<k<<": "<<ans<<endl;
    }

    return 0;
}
