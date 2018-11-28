#include<iostream>
#include<fstream>
#include<cmath>
#include<vector>
#include <algorithm>    // std::sort
using namespace std;
ifstream fin("A.in");
ofstream fout("Aout.txt");
int N;
int m_arr[150];
class Node
{
      public:
      int t;
      int s,e;
};
vector<Node> v;

bool x()
{
     vector<Node> temp;
     for(int i=0;i<v.size();i++)
     {
             //add mode
             Node buff = v[i];
             while(buff.t>m_arr[buff.s]&&buff.s<=buff.e)
             {
                                                        buff.t += m_arr[buff.s];
                                                        buff.s++;
                                                        }
             //cout << buff.t << " " << buff.s << " " <<buff.e <<endl;
             if(buff.s>buff.e)return true;
             Node buff_2 = buff;
             buff.t = buff.t*2-1;
             temp.push_back(buff);
             buff_2.e--;
             temp.push_back(buff_2);
     }
     v = temp;
     return false;
}


int main()
{
    fin >> N;
    for(int i=0;i<N;i++)
    {
      v.clear();
      int T, n;
      fin >> T >> n;
      for(int j=0;j<n;j++)
              fin >>  m_arr[j];
      sort(m_arr, m_arr+n);
      Node buff;
      buff.t=T;
      buff.s=0;
      buff.e=n-1;
      v.push_back(buff);
      int j;
      for(j=0;j<100;j++)
      {
              if(x())break;
      }
      fout << "Case #"<<i+1 <<": " <<  j << endl;
    }

    system("pause");
}
