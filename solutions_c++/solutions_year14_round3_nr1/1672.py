#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <functional>

using namespace std;

int main()
{
    int i,j,k,l,m,n;
    long long T,M,N,K,t1,t2,t3,t4,t5;
    long long ans,out;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A_output.txt","w",stdout);
    cin>>T;
    for(t1=1;t1<=T;++t1)
    {
    	scanf("%lld/%lld",&M,&N);

    	cout<<"Case #"<<t1<<": ";
            while(N%2==0&&M%2==0)
            {
                N/=2;
                M/=2;
            }

    	K=N;
    	while(K%2==0)
        {
            K/=2;
        }
            long long pox=2,gen=1;
            while(M*pox<N)
            {
                pox*=2;
                gen++;
            }
            if(K==1)
                cout<<gen<<endl;
            else
            {
                if(M*pox==N)
                    cout<<gen<<endl;
                else
                    cout<<"impossible"<<endl;
            }

    }

    return 0;
}
