#include<bits/stdc++.h>
typedef long long int uli;
using namespace std;

const int mx=100+10;
char s[mx][mx];
bool ok[mx][mx];
int color[mx][mx];
bool cycle=false;
int n,m;
int lr,lc,ld;
vector<pair<int,int> >cls;
int dr,dc;
void getdir(char ch){
   dr=dc=0;
   if(ch=='>')dc=1;   
   else if(ch=='^') dr=-1;
   else if(ch=='<') dc=-1;   
   else if(ch=='v') dr=1;
}
bool valid(int r,int c){
   return 0<=r && r<n && 0<=c && c<m;
}
void dfs(int r,int c,char dir){
   cls.push_back(make_pair(r,c));
   if(color[r][c]>0 || ok[r][c]){
      cycle=true;
      return;
   }
   lr=r,lc=c,ld=dir;
   color[r][c]=1;
   char ndir=s[r][c];
   getdir(s[r][c]);   
   int nr=r+dr,nc=c+dc;
   while(valid(nr,nc) && s[nr][nc]=='.'){
      nr=nr+dr;
      nc=nc+dc;
   }   
   if(valid(nr,nc)){
      dfs(nr,nc,ndir);
   }
   color[r][c]=2;
}
int main(){
   freopen("al.in","r",stdin);   
   freopen("al.out","w",stdout);   
   int t;
   scanf("%d",&t);
   for(int tt=1;tt<=t;tt++){
      scanf("%d %d",&n,&m);
      for(int i=0;i<n;i++)
         scanf("%s",s[i]);      
      memset(ok,0,sizeof ok);
      int ans=0;
      for(int i=0;i<n;i++){
         for(int j=0;j<m;j++){
            if(s[i][j]=='.') ok[i][j]=true;            
            else{
               memset(color,0,sizeof color);  
               cycle=false;
               cls.clear();
               dfs(i,j,'.');
               if(!cycle){
                  if(ld=='.')continue;
                  ans++;                  
                  if(ld=='>') s[lr][lc]='<';
                  else if(ld=='^') s[lr][lc]='v';
                  else if(ld=='<') s[lr][lc]='>';
                  else if(ld=='v') s[lr][lc]='^';
               }
               for(int k=0;k<int(cls.size());k++){
                  ok[cls[k].first][cls[k].second]=true;
               }
            }
         }
      }
//      cout<<"___"<<endl;
//      for(int i=0;i<n;i++)cout<<s[i]<<endl;      
//      cout<<"ans="<<ans<<endl;
      bool possible=true;
      for(int i=0;i<n && possible;i++){
         for(int j=0;j<m &&possible;j++){
            if(!ok[i][j]){
               possible=false;
               int opr=-1,opc=-1;
               for(int r=0;r<n;r++) if(r!=i){
                  if(s[r][j]!='.'){
                     if(ok[r][j]) possible=true;
                     else opr=r,opc=j;
                  }
               }
               for(int c=0;c<m;c++) if(c!=j){
                  if(s[i][c]!='.'){
                     if(ok[i][c])possible=true;
                     else opr=i,opc=c;
                  }
               }
               if(possible) ok[i][j]=true,ans++;
               else{
                  if(opr==-1)possible=false;
                  else{
                     ok[i][j]=true;
                     ok[opr][opc]=true;
                     possible=true;
                     ans+=2;
                  }
               }
            }
         }
      }
      if(possible) printf("Case #%d: %d\n",tt,ans);
      else printf("Case #%d: IMPOSSIBLE\n",tt);
   }
   return 0;
}
