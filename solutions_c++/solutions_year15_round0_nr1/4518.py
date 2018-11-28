#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
  ifstream in;
  in.open("in.txt");
  ofstream out;
  out.open("out.txt");
  int T, smax;
  string s;
  in >> T;
  cout << T << endl;
  for (int k = 1; k <= T; k++)
  {
    in >> smax >> s;
    if(smax == 0)
    {
        out << "Case #" << k << ": " << 0 << endl;
        continue; 
    }
    int cur = s[0] - '0';
    int need = 0;
    for (int i = 1; i <= smax; i++)
    {
        if(s[i] > '0')
        {
            if(i > cur)
            {
                need += i - cur;
                cur += i - cur;
            }
            cur += s[i] - '0';
        }
    }
    out << "Case #" << k << ": " << need << endl;     
  }
  out.close();
  in.close();
   return 0;  
}
