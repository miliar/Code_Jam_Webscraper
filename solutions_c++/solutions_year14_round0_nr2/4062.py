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
  ifstream fin("B-large.in");
  ofstream fout("large_out.txt");
  fout.precision(7);

  int T;
  fin>>T;

  double C, F, X;
  for (int i=0; i<T; ++i)
    {
      // C: price for farm; F: farm production rate; X: total cookies to save
      fin>>C>>F>>X;
//      qDebug()<<"C = "<<C;
//      qDebug()<<"F = "<<F;
//      qDebug()<<"X = "<<X;
      double t = 0.;  // time already consumed
      double f = 2; // current rate
      double tt = X/f;  // time consumed to save
      bool keep_buying = true;
      while(keep_buying)
        {
          // try to see how much time it takes to buy another farm and then start saving
          double t_temp = t + C/f;
//          qDebug()<<"t_temp = "<<t_temp;
          double f_temp = f + F;
//          qDebug()<<"f_temp = "<<f_temp;
          double tt_temp = t_temp + X/f_temp;
//          qDebug()<<"tt_temp = "<<tt_temp;
          if(tt_temp > tt) keep_buying = false;
          else
            {
              f = f_temp;
              t = t_temp;
              tt = tt_temp;
            }
        }
      fout<<"Case #"<<i+1<<": "<<fixed<<tt<<endl;
//      qDebug()<<"Case #"<<i+1<<": "<<fixed<<tt<<endl;
    }
  fout.close();
  return a.exec();
}
