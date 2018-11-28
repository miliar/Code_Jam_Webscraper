#include <vector>
#include <list>
#include <map>
#include <fstream>
#include <iostream>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
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
#include <ctime>


using namespace std;


ifstream fin("A-small-attempt3.in");
ofstream fout("A.out");
int main(){
int t;
fin>>t;
for (int tests=0;tests<t;tests++){

int n;
fin>>n;
string vals[n];
for (int i=0;i<n;i++){
    fin>>vals[i];
   // fout<<vals[i]<<endl;
}
string sup[n];
vector <int> vecs[n];
for (int i=0;i<n;i++){
    sup[i]=vals[i][0];
    int val=1;
    
      if (vals[i].size()==1){
          // sup[i] = vals[i];
           vecs[i].push_back(1);
      }
      else
    for (int j=1;j<vals[i].size();j++){

      if (vals[i][j-1]!=vals[i][j]){
      sup[i]+=vals[i][j];  
      vecs[i].push_back(val);
      val=1;
      }
      else val++;

      if (j==vals[i].size()-1){
      vecs[i].push_back(val);
      }
    } 
    //for (int j=0;j<vecs[i].size();j++)fout<<vecs[i][j]<<",";
    //fout<<endl;
}

//fout<<endl;
bool isover = false;
for (int i=0;i<n-1;i++){
    if (sup[i]!=sup[i+1]){
           isover = true;               
    }
}
if (isover){
fout<<"Case #"<<tests+1<<": Fegla Won"<<endl;
continue;
            
}
vector <long double> vecdoub;
for (int i=0;i<vecs[0].size();i++){
    vecdoub.push_back(0);
    for (int j=0;j<n;j++){
        vecdoub[vecdoub.size()-1] += (long double)(vecs[j][i]);
        
        }
    vecdoub[vecdoub.size()-1] /= n;
    vecdoub[vecdoub.size()-1] = round(vecdoub[vecdoub.size()-1]);
    //fout<<vecdoub[vecdoub.size()-1]<<",";
}
long long ans = 0;
for (int i=0;i<n;i++)
    for (int j=0;j<vecdoub.size();j++)
        ans += (int)(abs(vecs[i][j]-vecdoub[j]));

fout<<"Case #"<<tests+1<<": "<<ans<<endl;

}

//system("pause");
return 0;
}
