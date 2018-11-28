#include <iostream>
using namespace std;

int A[10];
long long unsigned int update(long long unsigned int N, int i)
{
    N *= i;
    int x = 10;
    long long unsigned int M = N;
//    cout<<M<<'\n';
    while(N)
    {
        A[N%x]++;
        N/=x;
    }
    for(int c=0; c<10; ++c)
    {
        if(A[c] == 0)
            return 0;
    }
    return M;
}

int main()
{
    long unsigned int T;
    cin>>T;
    for(int jj=1; jj<=T; ++jj)
    {
        long long unsigned int N;
        cin>>N;
        if(N == 0)
        {
            cout<<"\nCase #"<<jj<<": INSOMNIA";
            continue;
        }
        for(int i=0; i<10; ++i)
        {
            A[i] = 0;
        }
        long unsigned int succ = 0;
        for(int i=1; ; ++i)
        {
            succ = update(N,i);
            if(succ > 0)
            {
                cout<<"\nCase #"<<jj<<": "<<succ;
                break;
            }
        }
    }
    return 0;
}
