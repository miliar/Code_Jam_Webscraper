#include <QCoreApplication>
#include "vector"
#include "set"
#include "fstream"
#include "QDebug"
#include "QString"
#include "stdio.h"
using namespace std;

int main(int argc, char *argv[])
{
  QCoreApplication a(argc, argv);

  ifstream fin("in.txt");
  ofstream fout("out.txt");
  int T;
  fin>>T;

  int N;

  for(int i=0; i<T; ++i)
    {
      bool feglawon = false;
      vector<string> strings;
      vector< vector<int> > patterns;
      string min;
      fin>>N;
      for(int n=0; n<N; ++n)
        {
          string s;
          fin>>s;
          qDebug()<<s.size();
          strings.push_back(s);

          vector<int> pattern;
          string::iterator it = s.begin();
          string min_temp;
          min_temp += *it;
          pattern.push_back(1);
          for(; it!=s.end(); ++it)
            {
              if(*it != min_temp.back())
                {
                  pattern.push_back(1);
                  min_temp += *it;
                }
              else ++pattern.back();
            }
          if(n==0) min = min_temp;
          else if(min!=min_temp)
            {
              feglawon = true;
              break;
            }
          for(int i=0; i<pattern.size(); ++i)
          qDebug()<<"Pattern"<<pattern[i];
          patterns.push_back(pattern);
          qDebug()<<"MinSize"<<min.size();
        }


      fout<<"Case #"<<i+1<<": ";
      if(feglawon) fout<<"Fegla Won"<<endl;
      else
        {

          // now compute moves
          int minsize = min.size();
          int moves = 0;
          qDebug()<<"N"<<N;
          qDebug()<<"Pattern Size"<<patterns.size();
          for(int l=0; l<minsize; l++)
            {
              int mean=0;
              for (int k=0; k<N; ++k)
                {
                  mean += patterns[k][l];
                }
              mean /= N;
              for (int k=0; k<N; ++k)
                {
                  int temp = patterns[k][l] - mean;
                  temp = (temp>0)? temp : -temp;
                  moves += temp;
                }
            }
          fout<<moves<<endl;
        }
    }

  fout.close();
  fin.close();
  return a.exec();
}
