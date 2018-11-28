#include <fstream>
#include <cstdio>
#include <cstring>
#define NMAX 5005

using namespace std;

char s[NMAX];
int v[NMAX];
int n,i,nrflip,k,T,j;

void rastoarna(int st,int dr)
{
    while(st<dr)
    {
        v[st]=v[st]^1;
        v[dr]=v[dr]^1;
        swap(v[st],v[dr]);
        ++st;
        --dr;
    }
    if(st == dr) v[st]=v[st]^1;
}

int main()
{
    ifstream f("test.in");
    freopen("test.out","w",stdout);
    f>>T;f.get();
    k=0;
    int ok=0;
    while(T)
    {
        ++k;--T;
        printf("Case #%d: ",k);
        f.getline(s,NMAX);
        n=strlen(s);
        for(i=0;i<n;++i)
            if(s[i] == '+') v[i+1]=1;
                else v[i+1]=0;
        i=n;nrflip=0;
        while(i > 0)
        {
            if(v[i] == 0)
            {
                //trebuie sa aducem un 1 pe prima pozitie
                j=1;ok=0;
                while(v[j] > 0 && j<n)
                {
                    v[j]=0;++j; ok=1;
                }
                if(ok == 1) ++nrflip;
                     ++nrflip;
                    rastoarna(1,i);
            }
            --i;
        }
        printf("%d\n",nrflip);
    }

}
