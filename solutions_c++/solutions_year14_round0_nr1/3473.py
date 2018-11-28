#include<algorithm>
#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>
#include<stdlib.h>
#include<vector>
#include<stack>
#include<queue>
#include<list>
#include<bitset>
#include<map>
//Template V1
#define nl printf("\n")
#define in(x) scanf("%d",&x)
#define out(x) printf("%d",x)
#define inll(x) scanf("%lld",&x)
#define outll(x) printf("%lld",x)
#define inc(x) scanf("%c",&x)
#define outc(x) printf(x)
#define ins(x) scanf("%s",&x)
#define outs(x) printf("%s",x)
#define loop(var,x,y) for(int var=x;var<y;var++)
#define rloop(var,x,y) for(int var=x-1;var>=y;var--)
#define cins(x) cin>>x
#define couts(x) cout<<x
#define reset(x,y) memset(x,y,sizeof(x));
#define stop fflush(stdin);getchar()
#define push_back PB
#define GOD using
#define BLESS namespace
#define YOU std;

GOD BLESS YOU

typedef long long ll;
typedef vector<int> vi;

int main(){
int T;in(T);
int kasus=1;

while(T--){
int val1[20]={0};
int val2[20]={0};

int x;in(x);
for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
                int temp;in(temp);
                val1[temp]=i+1;
        }
}
int y;in(y);
for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
                int temp;in(temp);
                val2[temp]=i+1;
        }        
}
int count=0;
int last=0;
for(int i=1;i<=16;i++){
        if(val1[i]==x){
          for(int j=1;j<=16;j++){
           if(val2[j]==y&&j==i){count++;last=j;}
          }
        }
}

printf("Case #%d: ",kasus++);
if(count==0){
printf("Volunteer cheated!\n");
}
else if(count==1){
printf("%d\n",last);
}
else if(count>1){
printf("Bad magician!\n");

}

}

}
