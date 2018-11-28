#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>

using namespace std;

double ken[1000];
double naomi[1000];

int main(){
  int nn;
  scanf("%d",&nn);
  for(int c=1;c<=nn;c++){
    set<double> ke;
    set<double> ke2;
    set<double> nao;
  int n;
  scanf("%d",&n);
  for(int i=0;i<n;i++){
    scanf("%lf",&naomi[i]);
    nao.insert(naomi[i]);
  }
  for(int i=0;i<n;i++){
    scanf("%lf",&ken[i]);
    ke.insert(ken[i]);
    ke2.insert(ken[i]);
  }

  
  int score_war=0;
    //play anything
    //other play immediately higher
  for(int i=0;i<n;i++){
    if(ke2.upper_bound(naomi[i])==ke2.end()){
      score_war++;
      ke2.erase(*ke2.begin());
  }else{
    ke2.erase(*ke2.upper_bound(naomi[i]));
  }
  }


  int score_d_war=0;
  for(int i=0;i<n;i++){
    if(nao.upper_bound(ken[i])==nao.end()){
      nao.erase(*nao.begin());
  }else{
      score_d_war++;
    nao.erase(*nao.upper_bound(ken[i]));
  }
  }
/*
  while(!ke.empty()){
    while(!ke.empty() && *ke.rbegin() > *nao.rbegin()){
    printf("war : play %lf ans %lf \n",*nao.begin(),*ke.rbegin());
      ke.erase(*ke.rbegin());
      nao.erase(*nao.begin());
    }
    if(!ke.empty()){
    printf("war : play %lf ans %lf ++\n",*nao.rbegin(),*ke.begin());
    score_d_war++;
    ke.erase(*ke.begin());
    nao.erase(*nao.rbegin());
    }
  }*/

  printf("Case #%d: %d %d\n",c,score_d_war,score_war);
    
  }
}
