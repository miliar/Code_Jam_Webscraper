#include<fstream>
#include<cstdio>
using namespace std;
int main()
{
    ifstream ifile;
    ifile.open("B-small-attempt0.in");
    FILE * pf = fopen("ans.txt","w");
    int t,i,j,a,b,k,c,x;
    ifile>>t;
    for(x=1;x<=t;++x)
    {
        c=0;
        ifile>>a>>b>>k;
        for(i=0;i<a;++i)
        {
            for(j=0;j<b;++j)
            {
                if((i&j)<k)
                {
                    //printf("%d %d\t",i,j);
                    ++c;
                }

                    //printf("%d %d %d\t",i,j,i&j);
            }
        }
        fprintf(pf,"Case #%d: %d\n",x,c);
    }
}
