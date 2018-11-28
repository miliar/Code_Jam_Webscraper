#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.out","w",stdout);

    int T;
    scanf("%d",&T);

  //  long long dim[1000000000];

    for(int i=1; i<=T; i++)
    {
        long long r,t;
        scanf("%llu%llu",&r,&t);

        long long sum = 0;
        long long k = r;
        int counter = 0;
        while( sum <= t )
        {
            sum += (((k+1)*(k+1)) - (k*k));
            counter++;
            k+=2;
        }

        counter--;
        cout<<"Case #"<<i<<": "<<counter<<'\n';

    }

}
