#include <cstdio>
#include <cstring>
#include <algorithm>
#include <bitset>

#define DIM 100000


using namespace std;
bitset<1005>used;
char buff[DIM];
int pz = DIM-1,tstcase;

void scan(int &A)
{
    A = 0;
    int tims = -999;
    while('0' > buff[pz] || buff[pz] > '9')
        if(++pz == DIM)fread(buff,1,DIM,stdin),pz = 0;
    while('0' <= buff[pz] && buff[pz] <= '9' || buff[pz] == '.')
    {
        if(buff[pz] !='.')
        {
            A = A * 10 + buff[pz] - 48;
            ++tims;
        }
        else tims = 0;
        if(++pz == DIM)
            fread(buff,1,DIM,stdin),pz = 0;
    }
    if(tims > 0)
    while(tims < 5){
        tims ++;
        A *= 10;
    }
}

int nre,N[1005],K[1005];

void read()
{
    scan(nre);
    for(int i = 1; i <= nre; ++i)
        scan(N[i]);
    for(int i = 1; i <= nre; ++i)
        scan(K[i]);
    sort(N+1,N+nre+1);
    sort(K+1,K+nre+1);
}

void solve()
{
    int X = 0,Y = 0;
    int i1 = 1,i2 = nre,j1 = 1,j2 = nre;
    while(i1 <= i2 && j1 <= j2)
    {
        while(N[i1] < K[j1] && i1 <= i2 && j2 >= j1)
            ++i1, --j2;
        while(N[i1] > K[j1] && i1 <= i2 && j1 <= j2)
        {
            ++X;
            ++i1;
            ++j1;
        }
    }
    used = 0;
    int oki = 0;
    for(int i = 1; i <= nre; ++i)
    {
        oki  = 0;
        for(int j = 1; j <= nre; ++j)
            if(!used[j] && K[j] > N[i])
            {
                used[j] = 1;
                oki = 1;
                break;
            }
        if(!oki)
        {
            Y = nre - i + 1;
            break;
        }
    }
    printf("Case #%d: %d %d\n",tstcase,X,Y);
}

int main()
{
    freopen("war.in","r",stdin);
    freopen("war.txt","w",stdout);

    int T;
    scan(T);
    while(T--)
    {
        ++tstcase;
        read();
        solve();
    }

    return 0;
}
