#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

long long X[64];
long long sum[64];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int tc;
    cin >> tc;
    for(int nt = 1; nt <= tc; nt++)
    {
        long long B, N;
        cin >> B >> N;

        memset(X,0,sizeof(X));
        for(int i=0; i<N; i++)
        {
            cin >> X[i];
        }

        X[N+1] = 10000000000000LL;
        sort(X, X+(N+1));
    //    for(int i=0; i<64; i++)
  //      cout << X[i] << " ";
//        cout << endl;
        sum[0]=0;
        for(int i=1; i<=N+1; i++)
        {
            sum[i]=sum[i-1]+X[i];
        }

        double best = 0;
        long long cant = 37-N;
        for(int i=1; i<=N; i++)
        {
            for(int j=0; j<=N-i; j++)
            {

                long long k;
                if(cant+j > 0) k = min( X[i+j] -1, (sum[i+j-1]+B-j)/(cant+j));
                if(cant+j > 0 && k>=X[i+j-1])
                {
                    double p = k*cant-sum[i-1];
                    p /= cant;
                    p*=36;
                    p -= k*(cant+j)+j-sum[i+j-1];
                    best = max(best, p);
                }
            }
            //long long k;
            //if(cant > 0) k=min(X[i]-1,(sum+B)/cant);
            //if(cant > 0 && k>=X[i-1])
            //{
            //    double p = (k*cant-sum);
            //    p /= cant;
            //    p*=36;
            //    p -= k*cant-sum;
            //    best = max(best, p);
            //}
            //sum+=X[i];
            //cant++;
            cant++;
        }

        cout << "Case #" << nt << ": ";
        printf("%9.9Lf\n", best);
    }
}
