#include <bits/stdc++.h>

using namespace std;

#define fi first
#define se second
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef double dbl;
typedef vector<int> vi;
typedef pair<int, int> pi;

void flip(char *c, int bg, int en){
  while(bg<=en){
    swap(c[bg],c[en]);
    if(c[bg]=='+')c[bg]='-';
    else c[bg]='+';
    if(bg==en)break;
    if(c[en]=='+')c[en]='-';
    else c[en]='+';
    bg++,en--;
  }
}
bool doit2(char *c, const int &l){
  int ixm=l-1;
  while(ixm>=0 && c[ixm]=='+')ixm--;
  if(ixm<0)return true;
  if(c[0]=='-'){
    flip(c,0,ixm);
    return false;
  }
  int ixp=0;
  while(ixp<l && c[ixp]=='+')ixp++;
  flip(c,0,ixp-1);
  return false;
}

void doit(){
  char c[105];
  int l,res=0;
  scanf("%s", c);
  l=strlen(c);
  while(!doit2(c,l)){
    res++;
  }
  cout<<res<<endl;
}

int main() {
  int t;
  scanf("%d", &t);
  for(auto i=0;i<t;i++){
    printf("Case #%d: ",i+1);
    doit();
  }
  return 0;
}
