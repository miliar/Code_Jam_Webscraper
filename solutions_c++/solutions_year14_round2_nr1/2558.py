#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
using namespace std;


char tab[101][101];
int main(){
  int t;
scanf("%d",&t);
for(int cas = 1; cas<=t;cas++){
int n;
scanf("%d",&n);
for(int i=0;i<n;i++){
  scanf("%s",&tab[i]);
}  
vector<char> x[100];
vector<char> y[100];


for(int i=0;i<n;i++){
char c=' ';
  for(int j=0;j<100;j++){
      if(tab[i][j]=='\0')break;
      if(tab[i][j]!=c){x[i].push_back(tab[i][j]);c=tab[i][j];y[i].push_back(0);}else{y[i][y[i].size()-1]++;}
  }
}
    int xxx=0;
bool b=true;
  for(int i=1;i<n;i++){if(x[i].size()!=x[0].size())b=false;for(int j=0;j<x[0].size();j++)if(x[i][j]!=x[0][j])b=false;}
  if(b){
    int tt[101];
    for(int j=0;j<x[0].size();j++)tt[j]=0;
    for(int i=0;i<n;i++){for(int j=0;j<x[i].size();j++){tt[j]+=y[i][j];}}
    int moy[101];
    for(int j=0;j<x[0].size();j++)moy[j]=int(round(float(tt[j])/float(n)));
    for(int i=0;i<n;i++){for(int j=0;j<x[i].size();j++){xxx+= abs(y[i][j]-moy[j]) ;}}
  }
  if(b)printf("Case #%d: %d\n",cas,xxx);else printf("Case #%d: Fegla Won\n",cas);
  
}
return 0;
}
