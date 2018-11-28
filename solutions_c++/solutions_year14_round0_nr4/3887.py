#include <QCoreApplication>
#include "vector"
#include "set"
#include "fstream"
#include "QDebug"
#include "QString"

using namespace std;


int main(int argc, char *argv[])
{
  QCoreApplication a(argc, argv);

  // read in a file
  ifstream fin("D-large.in");
  ofstream fout("large-out.txt");
  fout.precision(7);

  int T, N, dewar, war;
  fin>>T;

  for (int i=0; i<T; ++i)
    {
      fin>>N;
      vector<double> Ken(N), Naomi(N);
      for(int j=0; j<N; ++j) fin>>Naomi[j];
      for(int j=0; j<N; ++j) fin>>Ken[j];
      sort(Naomi.begin(),Naomi.end());
      sort(Ken.begin(),Ken.end());
      vector<double>::iterator itK = Ken.begin();
      vector<double>::iterator itN = Naomi.begin();
      dewar = 0;
      // compute dewar first
      while(itN!=Naomi.end())
        {
          if(*itN < *itK) ++itN; // Naomi need to choose a heavier block to beat Ken's lightest block
          else
            {
              ++dewar;
              ++itK;
              ++itN;
            }
        }
      // now compute war
      // just switch them, as now Ken has exactly the same advantage
      war = N;
      itK = Ken.begin();
      itN = Naomi.begin();
      while(itK!=Ken.end())
        {
          if(*itN > *itK) ++itK; // Ken need to choose a heavier block to beat Naomi's lightest block
          else
            {
              --war;
              ++itK;
              ++itN;
            }
        }
      fout<<"Case #"<<i+1<<": "<<dewar<<" "<<war<<endl;
      qDebug()<<"Case #"<<i+1<<": "<<dewar<<" "<<war;
    }
  fout.close();
  return a.exec();
}
