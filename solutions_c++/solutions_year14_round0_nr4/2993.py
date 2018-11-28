#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

//#define MY_TEST

int main()
{
    #ifndef MY_TEST
    freopen("input.in","rt",stdin);
    freopen("output.txt","wt",stdout);
    #endif // MY_TEST.

    int T,N,k,i,j,w,dw;
    double p1[1000],p2[1000];

    cin>>T;
    for(k=1;k<=T;++k)
    {
        cin>>N;
        for(i=0;i<N;++i)
            cin>>p1[i];
        for(i=0;i<N;++i)
            cin>>p2[i];
        sort(p1,p1+N);
        sort(p2,p2+N);
        // Play War optimally
        w=0;
        j=N-1;
        for(i=N-1;i>=0;--i)
        {
            if(p1[i]<p2[j])
            {
                --j;
            }
            else
            {
                ++w;
            }
        }
        //Play Deceitful war optimally
        dw=0;
        j=0;
        for(i=0;i<N;++i)
        {
            if(p1[i]>p2[j])
            {
                ++dw;
                ++j;
            }
        }
        cout<<"case #"<<k<<": "<<dw<<" "<<w<<endl;
    }

    return 0;
}
