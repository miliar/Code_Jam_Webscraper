#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;


int T,cc=1;
char num[1000];
bool value[1000];


int main(){

   //freopen("init.in","r",stdin);
   //freopen("A-large.in","r",stdin);
   //freopen("solve.out","w",stdout);

   scanf("%d",&T);
   while(T--){
     int sum=0,total,s,aux;
     memset(value,false,sizeof value);
     scanf("%d",&s);
     scanf("%s",&num);
     total=num[0]-'0';


     for(int i=1;i<=s;i++){
       if(i<=total){
         if(value[i]) continue;
         value[i]=1;
         total+=num[i]-'0';
       }
       else{
         aux=i-total;
         if(aux>s) aux=s;
         total-=num[i-1]-'0';
         num[i-1]=char(num[i-1]+aux);
         sum+=aux;
         value[i-1]=0;
         i=i-2;
       }
     }
     printf("Case #%d: %d\n",cc++,sum);
   }

   return 0;
}
