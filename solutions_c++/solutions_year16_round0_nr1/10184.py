#include <bits/stdc++.h>
using namespace std;

bool A[10];

void funcion(long long N)
{
    long long q,r;
    do
    {
        r = N%(10LL);
        q = N/(10LL);
        N = q;
        A[r] = true;
    }while(N!=(0LL));
}

bool check()
{
    for(int i=0;i<10;i++)
        if(A[i] == false)
            return false;
    return true;
}
int main()
{
    int T;
    long long cont;
    long long N;
    cin>>T;

    for(int i=1;i<=T;++i)
    {
        memset(A,0,sizeof(bool)*10);
        cin>>N;
        printf("Case #%d: ",i);

        cont = (0LL);
        
        if(N==(0LL))
            printf("INSOMNIA\n");
        else
        {

            while(!check())
            {
                cont = cont + 1LL;
                funcion(N*cont);
            }

            cout<<(N*cont)<<endl;
        }

    }
    return 0;
}
