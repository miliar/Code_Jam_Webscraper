#include <fstream>
#include <cmath>

using namespace std;

bool palindrom(int nr)
{
    int a[101],cf=0,m;
    if(nr<10)
        return true;
    while(nr)
    {
        a[cf++]=nr%10;
        nr/=10;
    }
    m=cf/2;
    for(int i=0;i<m;i++)
        if(a[i]!=a[cf-1-i])
            return false;
    return true;
}

int main()
{
    int n,a,b,j,nr,root;
    ifstream f1("C-small-attempt0.in");
    f1>>n;
    ofstream f2("C-small-attempt0.out");
    for(int i=0;i<n;i++)
    {
        if(i)
            f2<<'\n';
        f2<<"Case #"<<i+1<<": ";
        nr=0;
        f1>>a>>b;
        for(j=a;j<=b;j++)
            if(palindrom(j))
            {
                root=sqrt(j);
                if(pow(root,2)==j)
                    if(palindrom(root))
                        nr++;
            }
        f2<<nr;
    }
    return 0;
}
