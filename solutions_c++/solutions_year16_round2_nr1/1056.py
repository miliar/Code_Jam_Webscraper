#include<bits/stdc++.h>
using namespace std;
string arr[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int ans[12];
string inp;
int cnt[150];
int L;

int Find()
{
     if(cnt['Z'] > 0){
          return 0;
     }

     if(cnt['W'] > 0){
          return 2;
     }

     if(cnt['U'] > 0){
          return 4;
     }

     if(cnt['X'] > 0){
          return 6;
     }

     if(cnt['G'] > 0){
          return 8;
     }

     if(cnt['O'] > 0){
          return 1;
     }

     if(cnt['R'] > 0){
          return 3;
     }

     if(cnt['F'] > 0){
          return 5;
     }

     if(cnt['S'] > 0){
         return 7;
     }

     return 9;
}

int main()
{
       freopen("A-large.in","r",stdin);
       freopen("0.out","w",stdout);
       int T,it,n,i,j;
       scanf("%d",&T);
       for(it=1; it<=T; it++){
             cin>>inp;
             L= inp.size();
             for(i=0; i<=9; i++)  ans[i]=0;
             for(i=0; i<140; i++)  cnt[i]=0;

             for(i=0; i<L; i++){
                  cnt[inp[i]]++;
             }

             while(L > 0){
                   int x = Find();
                 //  printf("x:%d\n",x);
                   ans[x]++;
                   L -= (int)(arr[x].size());
                   for(i=0; i<arr[x].size(); i++){
                        cnt[arr[x][i]]--;
                   }
             }

             printf("Case #%d: ",it);
             for(i=0; i<=9; i++){
                  while(ans[i]>0){
                      printf("%d",i);
                      ans[i]--;
                  }
             }
             puts("");
             //cout<<"Case #"<<it<<": "<<out<<endl;
       }


       return 0;
}
