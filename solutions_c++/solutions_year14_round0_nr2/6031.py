#include <iostream>
#include <fstream>
using namespace std;


int main()
{

 ofstream fout;
 fout.open("B-large.out");

 fout.setf(ios::fixed);
 fout.setf(ios::showpoint);
 fout.precision(7);

 ifstream fin;
 fin.open("B-large.in");
 double cost, farm, goal, ans, to_farm, to_goal1, to_goal2;
 int cases;
 double cookies;
 fin >> cases;

 for(int z = 0; z < cases; ++z)
 {
  bool done = false;
  cookies = 2;
  fin >> cost >> farm >> goal;
  while(!done)
  {
   to_farm = cost / cookies;
   to_goal1 = goal / cookies;
   to_goal2 = to_farm + (goal / (cookies + farm));
   if(to_goal1 < to_goal2)
   {
    done = true;
    ans += to_goal1;
   }
   else
   {
    ans += to_farm;
    cookies += farm;
   }

  }

  fout << "Case #" << z + 1 << ": " << ans << endl;

  ans = 0;
 }

 return(0);
}
