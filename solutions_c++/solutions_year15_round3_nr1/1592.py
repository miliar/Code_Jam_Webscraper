#include <iostream>
#include <fstream>
using namespace std;

int main()
{
   int t, r, c, w;
   ifstream f("input.txt");
   ofstream g("output.txt");
   f>>t;
   int ans;
   for (int caz = 1; caz <= t; caz++)
   {
       f>>r>>c>>w;
       ans = c/w*(r-1) + (c-1)/w + w;
       g<<"Case #"<<caz<<": "<<ans<<'\n';
   }
}
