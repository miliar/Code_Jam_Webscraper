#include<iostream>
#include<stdio.h>
#include<iomanip>
#include<fstream>
using namespace std;
int t;
double c, f, x;
void inmake()
{ ifstream fin;
  fin.open("in.txt");
  
  ofstream fout;
  fout.open("out.txt");
  
  fin >> t;
  for (int i = 0; i < t; i++)
  { fin >> c >> f >> x;
    double ans = 0, step = 2, current = 0;
    ans = x / step;
    
    int ok = 0;
    while (1)
    { current += (c / step);
      step += f;
      
      if (current + (x / step) - ans > 0.000000001)
      { fout << "Case #" << i + 1 << ": " << fixed << setprecision(7) << ans << endl; ok++; break; }
      
      else ans = current + (x / step);
     }
    
    if (ok == 0) fout << "Case #" << i + 1 << ": " << fixed << setprecision(7) << ans << endl;
   }
  
  fin.close();
  fout.close();
}

int main()
{ 
  inmake();
  
  cin >> t;
  return 0;
}
