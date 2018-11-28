#include<cstdio>
#include<cstring>
using namespace std;

#define MOD 1000000007

long long fact[105];

int T,N;
int in_sets[30];
bool middle[30];
int edges[30][30];
int deg_in[30],deg_out[30];

bool first;
char firstchar,lastchar;
char last;
char str[105];
int len;
bool ok;
int alones,paths;
long long ans;

int next(int u){
  for(int i=0;i<26;i++) if(edges[u][i]) return i;
  return -1;
}

bool is_con(char S[105]){
  int cnt[30];
  for(int i=0;i<26;i++) cnt[i]=0;
  int L=strlen(S);
  for(int i=0;i<L;i++) if(i==0 || S[i]!=S[i-1]) cnt[S[i]-'a']++;
  for(int i=0;i<26;i++) if(cnt[i]>1) return false;
  return true;
}

int main(){
  fact[0]=1;
  for(int i=1;i<=100;i++) fact[i]=(fact[i-1]*i)%MOD;
  scanf("%d",&T);
  for(int t=1;t<=T;t++){
    ans=1;
    alones=paths=0;
    for(int i=0;i<26;i++){
      middle[i]=false;
      in_sets[i]=0;
      deg_in[i]=deg_out[i]=0;
      for(int j=0;j<26;j++) edges[i][j]=0;
    }
    scanf("%d",&N);
    ok=true;
    for(int i=0;i<N;i++){
      scanf("%s",str);
      if(!is_con(str)){ ok=false; break; }
      len=strlen(str);
      firstchar=str[0]; lastchar=str[len-1];
      edges[firstchar-'a'][lastchar-'a']++;
      int k=0;
      for(int j=0;j<len;j++){
        if(j==0 || str[j]!=str[j-1]) in_sets[str[j]-'a']++;
        if(str[j]!=firstchar && str[j]!=lastchar) middle[str[j]-'a']++;
      }
    }
    for(int i=0;i<26;i++){
      if(middle[i] && in_sets[i]>1) ok=false;
    }
    if(ok){
      for(int i=0;i<26;i++){
        for(int j=0;j<26;j++){
          if(edges[i][j]>0){
            deg_in[j]++;
            deg_out[i]++;
          }
        }
      }
      //for(int i=0;i<26;i++) for(int j=0;j<26;j++) if(edges[i][j]>0) printf("z %c do %c: %d\n",(char)(i+'a'),(char)(j+'a'),edges[i][j]);
      //for(int i=0;i<26;i++) if(deg_in[i] > 0 || deg_out[i]>0) printf("%c: %d %d\n",(char)(i+'a'), deg_in[i], deg_out[i]);
      for(int i=0;i<26;i++){
        ans = (ans*fact[edges[i][i]])%MOD;
        if(deg_in[i] == 1 && deg_out[i]==1 && edges[i][i]>0) alones++;
        if(edges[i][i]>0){
          edges[i][i]=0;
          deg_in[i]--; deg_out[i]--;
        }
        int sum_in=0,sum_out=0;
        for(int j=0;j<26;j++){ sum_out += edges[i][j]; sum_in += edges[j][i]; }
        if(sum_in>1 || sum_out>1){ ok=false; break; }
      }
      for(int i=0;i<26;i++){
        if(deg_in[i]==0 && deg_out[i]==1){
          paths++;
          int u=i;
          while(u!=-1){
            deg_in[u]=deg_out[u]=0;
            u = next(u);
          }
        }
      }
      for(int i=0;i<26;i++){
        if(deg_in[i] || deg_out[i]) ok=false;
      }
    }
    if(ok){
      ans = (ans*fact[paths+alones])%MOD;
      printf("Case #%d: %lld\n",t,ans);
    }
    if(!ok){
      printf("Case #%d: 0\n",t);
    }
  }

  return 0;
}
