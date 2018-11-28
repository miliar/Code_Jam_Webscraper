#include <iostream>
#include <list>
using namespace std;

int more(list<int> & aud, int standing, int level)
{
  if (aud.empty())  {return 0;}

  int add = level - standing;
  if (add < 0)  {add = 0;}
  standing += aud.front();
  aud.pop_front();
  return add + more(aud, standing+add, level+1);
}

void tick(int cs)
{
  int n;
  cin >> n;
  list<int> aud;
  cin.get(); //skip space
  for (int i=0; i < n+1; i++)
  {
    char c = cin.get();
    int in = c - '0';
    aud.push_back(in);
  }
  cout << "Case #" << cs << ": " << more(aud, 0, 0) << endl;;
}

int main()
{
  int bign;
  cin >> bign;
  for (int i=0; i < bign; i++)
  {
    tick(i+1);
  }
}
