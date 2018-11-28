
#include<iostream>
using namespace std;
int main()
{
    int T,A,B,K,count,z,i,j;
    cin>>T;
    for(z=1;z<=T;z++)
    {
        count=0;
        cin>>A>>B>>K;
        for(i=0;i<A;i++)
        {
            for(j=0;j<B;j++)
            {
                if((i&j)<K)
                    count++;
            }
        }
        cout<<"Case #"<<z<<": "<<count<<"\n";
    }
    return 0;
}
