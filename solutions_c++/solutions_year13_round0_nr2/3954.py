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

int main(){
    ifstream in("entrada.in", ios::in);
    ofstream out("salida1.out", ios::out);
    int t;
    in>>t;
    int r,c;
    int mat[200][200];
   
    for(int o=1; o<=t; o++){
       in>>r>>c;
       for(int i=0; i<r; i++)
          for(int j=0; j<c; j++){
             in>>mat[i][j];
          }
      bool posible = true;
      for(int i=0; i<r && posible; i++)
          for(int j=0; j<c && posible; j++){
             bool est = true;
             int tmp = mat[i][j];
             int pox;
             for(int k=0; k<c; k++)
                if(mat[i][k]>tmp){
                   est = false;
                   pox = k;
                }
                
             if(!est){
                est = true;
                for(int k=0; k<r; k++)
                   if(mat[k][j]>tmp)
                      est = false;
             }
             if(!est)
                posible = false;
          }
      
       out<<"Case #"<<o<<": "<<(posible ? "YES": "NO")<<endl;
    }
}
