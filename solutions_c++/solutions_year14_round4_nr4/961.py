#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
char ent[15][15];
int ass[15];
int n,m;
int ret=0,qte=0;


int tem (vector<string> s){
  sort(s.begin(),s.end());
  int r =1;
  for(int i=0;i+1<(int)s.size();i++){
    int j=0;
    for(j=0;j<(int)min(s[i].size(),s[i+1].size());j++){
      if(s[i][j]!=s[i+1][j])break;
    }
    r += (int)s[i].size()-j;

  }
  // printf("%d\n",r);
  r += s[s.size()-1].size();
  /*for(int i=0;i<s.size();i++){
    printf("%s\n",s[i].c_str());
  }
  printf("%d \n",r);*/
  return r;
}
void calc(){
  int att =0;
  for(int i=0;i<m;i++){
    vector<string> at;
    for(int j=0;j<n;j++){
      if(ass[j]==i)at.push_back(string(ent[j]));
    }
    att += tem(at);
  } 
  if(att>ret){ret=att;qte=1;}
  else if(att==ret){qte++;}
}


int tt[15]={0};
void solve(int a){

  if(a==n){
    for(int i=0;i<m;i++){
      if(tt[i]==0)return;
    }
    calc();
    return;
  }
  for(int i=0;i<m;i++){
    ass[a]=i;
    tt[i]++;
    solve(a+1);
    tt[i]--;
  }

}

int main (){
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++){

    scanf("%d %d",&n,&m);
    for(int i=0;i<n;i++)
      scanf(" %s",ent[i]);
    
    ret=0,qte=0;
    solve(0);

    printf("Case #%d: %d %d\n",pp,ret,qte);
  }
  return 0;
}
