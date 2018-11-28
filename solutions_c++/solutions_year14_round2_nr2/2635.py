#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    int num1;
    int a,b,c,ans;
ifstream myfile ("B-small-attempt0.in");
  ofstream myfile2 ("output.txt");
myfile >> num1;
       for(int i=1;i<=num1;i++)
       {
               int count = 0;
               int x,y;
               myfile >> a >> b >> c;
               for(int j=0;j<b;j++)
               {
               for(int i=0;i<a;i++)
               {
               x = i;
               y = j;
               ans = x&y;
               if(ans < c)
               count++;
               }
               }
               myfile2 << "Case #" << i << ": "<< count << endl;
       }
    return EXIT_SUCCESS;
}
