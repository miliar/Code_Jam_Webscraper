#include <bits/stdc++.h>

using namespace std;

void recursion(string total, deque < char > cola, int i, string &min)
{
  if(cola.size() == total.size())
  {
    string total = "";
    for(int i = 0 ; i < (int)cola.size() ; i++)
      total += cola[i];
    if(min < total)
    {
      min = total;
    }
  }
  else
  {
    cola.push_front(total[i]);
    recursion(total,cola,i+1,min);
    cola.pop_front();
    cola.push_back(total[i]);
    recursion(total,cola,i+1,min);
  }
}

int main()
{
  int t;
  scanf("%d",&t);
  for(int i = 0 ; i < t ; i++)
  {
    string linea;
    cin >> linea;
    int pos = 0;
    deque < char > cola;
    string min = linea;
    recursion(linea,cola,pos,min);
  /*  string min = linea;
    do{
      if(min < linea)
      {
        min = linea;
      }
    }while(next_permutation(linea.begin(),linea.end()));*/
    cout << "Case #" << i+1 << ": " << min << endl;
  }


  return 0;
}
