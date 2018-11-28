#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{

  ifstream infile(argv[1]);
  int numCases;

  infile >> numCases;

  for (int i = 0; i < numCases; i++)
  {
    double c, f, x, totalTime = 0, rate = 2;
    infile >> c >> f >> x;

    while (1)
    {
      double newFarmTime = totalTime + c / rate + x / (rate + f);
      double cLeft = totalTime + x / rate;

      if (newFarmTime < cLeft)
      {
        totalTime += c / rate;
        rate += f;
      }
      else
      {
        totalTime += x / rate;
        break;
      }
    }
    cout << "Case #" << i + 1 << ": " << fixed << setprecision(7) << totalTime << endl;
  }

  return 0;

}
