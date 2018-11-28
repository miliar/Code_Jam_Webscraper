#include<stdio.h>
#include<string>
#include<algorithm>

using namespace std;

int T,TT,m,n;
char _s[8][20];
string s[8];
int go[8];
int worst,worstcnt;

void back(int i){
  if(i==m){
    int cnt=0;
    int j,k,l;

    for(k=0;k<n;k++){
      for(i=0,j=-1;i<m;i++)if(go[i]==k){
        if(j<0){
          cnt+=s[i].size()+1;
        }else{
          for(l=0;l<s[i].size() &&
                  l<s[j].size() &&
                  s[i][l]==s[j][l];l++);
          cnt+=s[i].size()-l;
        }
        j=i;
      }
    }

    if(cnt==worst)worstcnt++;
    else if(cnt>worst){
      worst=cnt;
      worstcnt=1;
    }
  }else{
    for(int j=0;j<n;j++){
      go[i]=j;
      back(i+1);
    }
  }
}

int main() {
  int i;
  scanf("%d",&T);
  for(TT=1;TT<=T;TT++){
    scanf("%d%d",&m,&n);
    for(i=0;i<m;i++){
      scanf("%s",_s[i]);
      s[i]=_s[i];
    }
    sort(s,s+m);
    worst=worstcnt=0;
    back(0);
    printf("Case #%d: %d %d\n",TT,worst,worstcnt);
  }
  return 0;
}
