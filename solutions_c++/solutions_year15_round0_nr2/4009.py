#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
using namespace std;


map < vector<int> , int> M;
int sim(vector<int> v)
{
  int pos = v[v.size()-1];
  if(pos <= 3) return M[v] = pos;
  if(M[v]) return M[v];
  int min = pos;
  vector<int> temp = v;
  for (int i = 1; i <= v[v.size()-1]/2; i++)
  {
     
         v[v.size()-1] -= i;
         v.push_back(i);
         sort(v.begin(), v.end());
         min <?= 1 + sim(v);
          v = temp;
  }
  return  M[v] = pos <? min;
}
int main()
{
  ifstream in;
  in.open("in.txt");
  ofstream out;
  out.open("out.txt");
  int D,T; 
  string s;
  in >> T;

  for (int k = 1; k <= T; k++)
  {
    int time = 0;
    in >> D;
    vector<int> v(D);
    for (int i = 0; i < D; i++)
    {
        in >> v[i];
       // out << v[i] << " ";
    }
  //  out << endl;
    sort(v.begin(),v.end());
    out << "Case #" << k << ": " << sim(v) << endl;     
  }
  out.close();
  in.close();
   return 0;  
}
