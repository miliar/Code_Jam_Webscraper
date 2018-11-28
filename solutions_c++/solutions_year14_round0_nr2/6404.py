#include <fstream>
using namespace std;

int main()
{
  ifstream in ("B.in", ios::in);
  ofstream out("B.out", ios::out);
  int casen;
  in>>casen;

  for (int casei = 0 ; casei < casen; casei++)
  {
    double C, F, X;
    in>>C>>F>>X;

    double speed = 2;
    double totaltime = 0.0;

    while(C/speed + X/(speed+F) < X/speed)
    {
      totaltime += C / speed;
      speed +=F;
    }
    totaltime += X/speed;
    out.precision(7);
    out<<"Case #"<<(casei+1)<<": "<<fixed<<totaltime<<endl;
  }
}
