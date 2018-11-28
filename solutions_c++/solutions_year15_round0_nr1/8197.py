#include<iostream>
using namespace std;

int standing, friends;
int n,maxLevel;
string seats;

bool init()
{
  standing = friends = 0;
  cin >> maxLevel >> seats;

  return true;
}

void calculate()
{
  standing = 0;
  friends = 0;

  for (int level = 0 ; level <= maxLevel ; level++)
  {
    int audiences = seats[level] - '0';
    if (level > standing)
    {
      int adding = level - standing;
      friends += adding;
      standing += adding;
    }
    standing += audiences;
  }
}

void output(int c)
{
  cout << "Case #" << c << ": " << friends << endl;
}

int main()
{
  cin >> n;

  for (int c = 0 ; c < n ; c++)
  {
    init();
    calculate();
    output(c+1);
  }

  return 0;
}
