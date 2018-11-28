// For Problem A Magic Tric

#include <QCoreApplication>
#include "vector"
#include "set"
#include "fstream"
#include "QDebug"

using namespace std;

int main(int argc, char *argv[])
{
  QCoreApplication a(argc, argv);

  // read in a file
  ifstream fin("A-small-attempt0.in");
  ofstream fout("out.txt");
  int T;
  fin>>T;
  int rid1, rid2, rows[16], first[4], second[4];
  for(int i=0; i<T; ++i)
    {
      // read in the first row index
      fin>>rid1;
      // read in and sort the selected row of the first time
      for(int j=0; j<16; ++j) fin>>rows[j];
      for(int j=0; j<4; ++j) first[j] = rows[4*(rid1-1)+j];
      sort(first, first+4);
//      qDebug()<<"all rows: ";
//      for(int j=0; j<16; ++j) qDebug()<<rows[j]<<" ";
//      qDebug()<<endl;
//      qDebug()<<"first selection: ";
//      for(int j=0; j<4; ++j) qDebug()<<first[j]<<" ";
//      qDebug()<<endl;

      fin>>rid2;
      // read are sort the selected row of the second time
      for(int j=0; j<16; ++j) fin>>rows[j];
      for(int j=0; j<4; ++j) second[j] = rows[4*(rid2-1)+j];
      sort(second, second+4);
      vector<int> v(4);
      vector<int>::iterator it;
      it=std::set_intersection (first, first+4, second, second+4, v.begin());
      v.resize(it-v.begin());
      fout<<"Case #"<<i+1<<": ";
      if(v.size()>1) fout<<"Bad magician!"<<endl;
      else if(v.size()==1) fout<<v[0]<<endl;
      else fout<<"Volunteer cheated!"<<endl;
    }
  fout.close();
  fin.close();
  return a.exec();
}
