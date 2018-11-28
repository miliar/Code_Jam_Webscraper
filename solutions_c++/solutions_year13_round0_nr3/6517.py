#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <cstdlib>
#include <fstream>
#include <vector>

using namespace std;

bool test_palindorme(const int &value)
{
  string temp, p1, p2;
  ostringstream conv;
  conv << value;
  temp = conv.str();

  if (temp.length() == 1)
    return true;

  if (temp.length() % 2 == 0)
  {
    p1 = string(temp, 0, temp.length() /2);
    p2 = string(temp, temp.length() /2, temp.length());
  }
  else
  {
    p1 = string(temp, 0, floor(temp.length() /2));
    p2 = string(temp, ceil(temp.length() /2)+1, temp.length());
  }
  //cout << temp << '\t' << p1 << '\t' << p2 << endl;

  if (p1 == p2)
    return true;
  else
    return false;

}

bool test_square(const int &value, const double &sq)
{
  if (sq == floor(sq))
    return true;
  else
    return false;
}

int main(int argc, char *argv[])
{
  //ifstream input("teste.txt");
  ifstream input("C-small-attempt0.in");
  ofstream output("output.txt");

  int t, i, j, qtt;
  int min, max;
  double sq;

  input >> t;
  for (i = 0; i < t; ++i)
  {
    input >> min >> max;
    qtt = 0;

    //test
    //max = floor(sqrt(max));

    for (j = min; j <= max; ++j)
    {
      sq = sqrt(j);
      if ((test_square(j, sq)) && (test_palindorme(sq)) &&(test_palindorme(j)))
        ++qtt;
    }
    output << "Case #" << i + 1 << ": " << qtt << endl;

  }


  //cout << "Case #" << i + 1 << ": " << matrix[0][0] << ".0000"<< endl;
  //getchar();
  //output << "Case #" << i + 1 << ": " << hits << ".000000" << endl;



  output.close();
  input.close();
}
