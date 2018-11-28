#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#define N 200
using namespace std;
int T,n;
vector<string>w;
string s;
int ptr[N];
int num[N];
int main(){
    freopen("A-small-attempt2.in","r",stdin);
   //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;++cas){
            scanf("%d",&n);
            w.clear();
            for(int i=0;i<n;++i){
                    cin>>s;//scanf("%s",s);
                    w.push_back(s);
            }
            int ans=0;
            bool ok=true;
            int len=w[0].size();
            int i=0;
            //int x=w[0][0]-'a';
            int x;
            memset(ptr,0,sizeof(ptr));
            memset(num,0,sizeof(num));
            while(i<len){
                 x = w[0][i]-'a';
                 int cnt=1;
                 while(i+1<len && (w[0][i+1]==w[0][i])){
                               cnt++;
                            i++; 
                 }
                 num[0]=cnt;
                 int j=1;
                 for(j=1;j<n;++j){
                      if(w[j][ptr[j]]-'a'!=x){
                          ok=false;
                          break;
                      }
                      cnt=0;
                      while(ptr[j]<w[j].size() && (w[j][ptr[j]]-'a'==x)){
                          cnt++;
                          ptr[j]++;
                      }
                      num[j]=cnt;
                 } 
                 if(j<n){
                         ok=false;
                         break;
                 }
                 int minv=101;
                 for(int k=1;k<=100;++k){
                         //int minv=101;
                         int tot=0;
                         for(int j=0;j<n;++j)
                                 tot += abs(k-num[j]);
                         minv=min(minv, tot);
                 }
                 ans+=minv;
                 i++;
            }
            for(int j=1;j<n;++j)
                    if(ptr[j]!=w[j].size()){
                       ok=false;
                       break;
                    }
            printf("Case #%d: ",cas);
           // printf("%d\n",ans);
            if(ok)printf("%d\n",ans);
            else printf("Fegla Won\n");
    }
    return 0;
}
