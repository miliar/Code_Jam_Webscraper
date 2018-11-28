#include <fstream>
#include <vector>
#include <iomanip>
using namespace std;
ifstream fin("B-large.in");
ofstream fout("Blarge.out");

int main()
{
    int t;
    fin>>t;
    for(int z=1;z<=t;z++)
    {
            fout<<setprecision(7);
            double c,f,x;
            double ans=0.0;
            fin>>c>>f>>x;
            ans=x/2.0;
            double p1,p2,ptotal,n1,n2,ntotal;
            n1=c/2.0;
            n2=x/(2.0+f);
            ntotal=n1+n2;
            if(ans<ntotal)
                  fout<<"Case #"<<z<<": "<<ans<<endl;
            else
            {
                  ptotal=ans;
                  int i=1;
                  while(ntotal<ptotal)
                  {
                        ptotal=ntotal;
                        p1=n1;
                        p2=n2;              
                        n1=p1+c/(2.0+i*f);
                        n2=x/(2.0+(i+1)*f);
                        ntotal=n1+n2;
                        i++;                                 
                  }  
                  fout<<"Case #"<<z<<": "<<ptotal<<endl;  
            }                  
    }                
    return 0;
}
            
