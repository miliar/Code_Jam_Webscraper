#include <bits/stdc++.h>

using namespace std;

int N;
map<string, int> mp;
bitset<5000> A, B, C, D;
bitset<5000> X[200];

void _main()
{
    cin>>N;
    cin.ignore();
    mp.clear();
    int n=0;
    A.reset();
    B.reset();
    for(int i=0; i<N; i++)
    {
        X[i].reset();
        string S;
        getline(cin, S);
        stringstream ss(S);
        while(ss>>S)
        {
            if(!mp.count(S))
                mp[S]=n++;
            int x=mp[S];
            if(i==0)
                A[x]=1;
            else if(i==1)
                B[x]=1;
            else
                X[i-2][x]=1;
        }
    }
    C=A, D=B;
    int ans=0x3f3f3f3f;
    for(int i=0; i<(1<<(N-2)); i++)
    {
        A=C;
        B=D;
        for(int j=0; j<N-2; j++)
        {
            if((i>>j)&1)
                A|=X[j];
            else
                B|=X[j];
        }
        ans=min(ans, (int)((A&B).count()));
    }
    printf("%d\n", ans);
    fflush(stdout);
}

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    int TEST;
    cin>>TEST;
    for(int i=1; i<=TEST; i++)
    {
        printf("Case #%d: ", i);
        _main();
    }
    return 0;
}
