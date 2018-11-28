#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime>
#include <climits>  
#include <fstream>  

using namespace std;

int main()
{
    ifstream in("entrada.txt", ios::in);
    ofstream out("salida.out", ios::out);
    
    int t;
    long long r, pint;
    long long ini=0;
    long long des=0;
    int cont =0;
    
    in>>t;
    
    for(int i=1; i<=t; i++){
       in>>r>>pint;
       cont =0;
       ini = r+1;
       while(1){
          des = ini*ini - (ini-1)*(ini-1);
          if(pint>=des){
             pint-=des;
             cont++;
          }
          else
             break;
          ini = ini +2;
       }
       out<<"Case #"<<i<<": "<<cont<<endl;
    }
}
