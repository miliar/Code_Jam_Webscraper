#include <iostream>
#include <algorithm>
using namespace std;

double A[1000], B[1000];
int N;

int newplay()
{
    int Al, Bl = 0, S = 0;
    for (Al = 0; Al<N; Al++) 
    {
        if (A[Al] > B[Bl])
        {
            S++; Bl++;
        }
    }
    return S;
}

int oldplay()
{
    int Bl = 0, Br = N-1, S = 0;
    for (int Ar = N-1; Ar >=0; Ar --)
    {
        if (B[Br] < A[Ar])
            S++;
        else
            Br--;
    }
    return S;
}

void real_main()
{
    cin>>N;
    for (int i=0; i<N; i++)
        cin>>A[i];
    for (int i=0; i<N; i++)
        cin>>B[i];
    sort(A, A+N); sort(B, B+N);
    cout<<newplay()<<" "<<oldplay()<<endl;
}

int main()
{
    int t; cin>>t;
    for (int i=1; i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        real_main();
    }
    return 0;
}
