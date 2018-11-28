#include<fstream>
using namespace std;
ifstream fin ("temp.in");
ofstream fout ("temp.out");
int main ()
{
    freopen ("temp.out","w",stdout);
    int t;
    fin>>t;
    int i;
    for (i=1;i<=t;i++)
    {
        double c,f,x;
        fin>>c>>f>>x;
        int j=1;
        double time=x/2;
        double cost=0;
        while (cost<time)
        {
            cost+=c/(2+(j-1)*f);
            if (cost+x/(2+j*f)<time) time=cost+x/(2+j*f);
            j++;
        }
        printf("Case #%d: %.6lf\n",i,time);
    }
    return 0;
}
