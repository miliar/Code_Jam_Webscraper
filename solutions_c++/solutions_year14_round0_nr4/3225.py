#include<iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);

    int T,N,n,war,deceitfull,j;
    double A[1001], B[1001];

    cin >> T;
    n=1;
    while(n<=T)
    {
        deceitfull = 0;
        war = 0;
        cin >> N;

        for(int i=0; i<N; i++)
        {
            cin >> A[i];
        }

        for(int i=0; i<N; i++)
        {
            cin >> B[i];
        }

        sort(A, A+N);
        sort(B, B+N);
        j=0;
        for(int i=0; i<N; )
        {
            if(A[i] > B[j])
            {
                deceitfull++;
                i++;
                j++;
            }
            else
            {
                i++;
            }
        }

        j=0;
        for(int i=0; i<N; )
        {
            if(B[i] > A[j])
            {
                war++;
                i++;
                j++;
            }
            else
            {
                i++;
            }
        }

        cout << "Case #" << n << ": " << deceitfull << " " << (N-war) << endl;

        n++;
    }

}
