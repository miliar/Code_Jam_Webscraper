#include <fstream>
#include <iomanip>
std::ifstream fin("B-large.in");
std::ofstream fout("output.out");
int T;
double c, f, x, sum, update;
bool flag;
int main()
{
    fin>>T;
    for(int i =0; i< T; i++)
    {
          sum = 0;flag = 0;update = 2;
          fin>>c>>f>>x;
          while(!flag)
          {
                      if((c/update + x/(update+f)) < x/update)
                      {
                                   sum+=c/update;
                                   update+=f;
                      }
                      else
                      {
                          sum+=x/update;
                          flag = 1;
                      }
          }
          fout<<"Case #"<<i+1<<": "<<std::setprecision(15)<<sum<<"\n";
    }
    return 0;
}
