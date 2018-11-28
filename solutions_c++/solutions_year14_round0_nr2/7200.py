#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

int main()
{
  int test_cases;
  double C,F,X,cookie_rate;
  double min_time, time, time_nobuy;

  ifstream readFile("B-large.in");
  ofstream writeFile("output.in");

  readFile>> test_cases;
  int i;

  for(i=0; i<test_cases; i++)
  {
      readFile>> C;
      readFile>> F;
      readFile>> X;
      cookie_rate = 2.0f;
      min_time = (X / cookie_rate);
      //cout<<min_time;
      time = 0.0f;

      while(true)
      {
          time += (C / cookie_rate);
          time_nobuy = (X / (cookie_rate+F));

          if(time + time_nobuy < min_time)
          {
              min_time = time + time_nobuy;
          }

          cookie_rate += F;

          if(time + time_nobuy > min_time)
          break;
      }

      writeFile <<"Case #"<< i+1 <<": "<<setprecision(7)<<fixed<<min_time<<endl;


  }

  readFile.close();
  writeFile.close();
  return 0;

}
