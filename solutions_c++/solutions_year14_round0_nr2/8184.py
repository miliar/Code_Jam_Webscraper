#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>

#define R 2.0

using namespace std;

double t1(const double &f, const int &n)
{
  double sum = 0.0;

  for (int i = 0; i < n; ++i)
    sum += (1/(R + (i * f)));

  return sum;
}


int main()
{
  ifstream input("B-large.in");
  ofstream output("output.txt");

  //string teste;

  int i, n;

  int t = 0;
  double c, f, x, time, time2;
  //string ans_text;

  input >> t;
  for (i = 0; i < t; ++i)
  {
    input >> c >> f >> x;

    time = 10E30;
    time2 = 0.0;
    n = 0;
    while (true)
    {
      time2 = (c * t1(f, n)) + (x/(R + (n*f)));
      if (time2 < time)
        time = time2;
      else
        break;
      n++;
    }

    //cout << c << "\t" << f << "\t" << x;
    //cout << " tempo: " << fixed << std::setprecision(7) << time << endl;
    output << fixed << setprecision(7);
    output << "Case #" << i+1 << ": " << time << endl;


    /*for(j = 0; j < 4; ++j)
      cout << cards_1[j] << ' ';
    cout << endl;
    for(j = 0; j < 4; ++j)
      cout << cards_2[j] << ' ';
    cout << endl;

    cout << "hey yop" << endl;*/
    //cout << ans_text << endl;

  }

 // while (getline(input, teste))
  //  cout << teste << endl;




  input.close();
  output.close();

  //cout << "Hello world!" << endl;
  return 0;
}
