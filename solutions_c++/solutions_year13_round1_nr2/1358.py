#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int maxx;

void trace(vector<int> values,int L,int R,int N,int j,int gain,int E)
{int i;int y=L;
      if(j==N){return;}
      for(i=0;i<=L;i++)
      {
          gain+=values[j]*i;
          L-=i;
          L+=R;
          if(L>E){L=E;}
          if(gain>maxx){maxx=gain;}
          trace(values,L,R,N,j+1,gain,E);
          L=y;
          gain-=values[j]*i;    
      }
      return;
}
int main(int argc, char *argv[])
{
    ofstream fout ("output.out");
    ifstream fin ("B-small-attempt4.in");
    bool y;
    
    vector<int> value,results;
    int E,R,N,i,j,T,t,x;
    fin>>T;
    maxx=0;
    for(t=0;t<T;t++)
    {
        fin>>E;
        fin>>R;
        fin>>N;
        if(R>E){R=E;}
    value.clear();
        for(i=0;i<N;i++)
        {
            fin>>x;
            value.push_back(x);
        }
        
        trace(value,E,R,N,0,0,E);
        results.push_back(maxx);
        maxx=0;
    }
    for(t=0;t<T;t++)
    {
    fout<<"Case #"<<t+1<<": "<<results[t]<<endl;
    }
    
    
    
    
    
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
