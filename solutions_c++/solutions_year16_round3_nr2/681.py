#include <cstdio>
#include <vector>
using namespace std;


vector<int > a[50];

int main(){
int t;
scanf("%d", &t);
for(int c=1;c<=t;c++){
int b;
long long int m;
scanf("%d %lld",&b,&m);
printf("Case #%d: ",c);
if(m > (1LL << (b-2))){printf("IMPOSSIBLE\n");continue;}
printf("POSSIBLE\n");

for(int i=0;i<b;i++){a[i].clear();a[i].resize(b,0);}

for(int i=1;i<b-1;i++)for(int j=i+1;j<b;j++)a[i][j]=1;

if(m==(1LL << (b-2) ))for(int j=1;j<b;j++)a[0][j]=1;
else{

for(int i=0;i<=50;i++){
if(  ((1LL<<i) & m) )a[0][b-i-2]=1;
}

}

for(int i=0;i<b;i++){
for(int j=0;j<b;j++)printf("%d",a[i][j]);
printf("\n");
}


// 2^n = complete-next for n+2 



}
return 0;
}
