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

int et,r,n;
int v[12];

int solve(int e, int ind, int gan){
    if(ind>=n)
       return gan;
    int sol =0;
    for(int i=0; i<=e; i++){
       sol = max(solve(min(e+r-i,et),ind+1,gan+v[ind]*i),sol);
    }
    return sol;
}

int main(){
    ifstream in("entrada.txt", ios::in);
    ofstream out("salida.out", ios::out);
    
    int t;
    
    in>>t;
    for(int i=1; i<=t; i++){
       in>>et>>r>>n;
       for(int j=0; j<n; j++){
           in>>v[j];
       }
       
       out<<"Case #"<<i<<": "<<solve(et,0,0)<<endl;
    }
}
