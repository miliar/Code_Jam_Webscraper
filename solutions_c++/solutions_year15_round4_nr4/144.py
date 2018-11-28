#include <cstdio>

int t,r,c;
long long prime=1000000007;

long long tabf3[101];
long long tabfn3[101];

long long tabf3_3[101];
long long tabfn3_3[101];

long long tabf3_4[101];
long long tabfn3_4[101];

long long tabf3_6[101];
long long tabfn3_6[101];

long long tabf3_12[101];
long long tabfn3_12[101];



int main(){
scanf("%d",&t);
tabf3[0]=1;
tabfn3[0]=1;
tabf3_3[0]=1;
tabfn3_3[0]=1;
tabf3_6[0]=1;
tabfn3_6[0]=1;
tabf3_4[0]=1;
tabfn3_4[0]=1;
tabf3_12[0]=1;
tabfn3_12[0]=1;

tabf3[1]=0;
tabfn3[1]=1;

tabf3_4[1]=0;
tabfn3_4[1]=1;

tabf3_6[1]=0;
tabfn3_6[1]=1;

tabf3_3[1]=0;
tabfn3_3[1]=1;

tabf3_12[1]=0;
tabfn3_12[1]=1;



tabf3[2]=1;
tabfn3[2]=0;

tabf3_4[2]=1;
tabfn3_4[2]=0;

tabf3_6[2]=1;
tabfn3_6[2]=2;

tabf3_3[2]=1;
tabfn3_3[2]=1;

tabf3_12[2]=1;
tabfn3_12[2]=2;



for(int i=3;i<=100;i++){
tabf3[i]=tabfn3[i-2];
tabfn3[i]=tabf3[i-1];

tabf3_3[i]=tabfn3_3[i-2];
tabfn3_3[i]=(tabf3_3[i-1]+3*tabf3_3[i-2]-2*tabf3[i-2])%prime;

tabf3_4[i]=tabfn3_4[i-2];
tabfn3_4[i]=(tabf3_4[i-1]+4*tabf3_4[i-3]-3*tabf3[i-3])%prime;

tabf3_6[i]=tabfn3_6[i-2];
tabfn3_6[i]=(tabf3_6[i-1]+9*tabf3_6[i-2]-3*tabf3_3[i-2]-4*tabf3[i-2])%prime;

tabf3_12[i]=tabfn3_12[i-2];
tabfn3_12[i]=(tabf3_12[i-1]
+3*tabf3_12[i-2]-2*tabf3[i-2]
+6*tabf3_12[i-2]-3*tabf3_3[i-2]-2*tabf3[i-2]
+4*tabf3_12[i-3]-3*tabf3_6[i-2])%prime;

}


for(int i=1;i<=t;i++){
scanf("%d %d",&r,&c);
if(!(c%12))
printf("Case #%d: %lld\n",i,(tabf3_12[r]+tabfn3_12[r])%prime);
else if(!(c%6))
printf("Case #%d: %lld\n",i,(tabf3_6[r]+tabfn3_6[r])%prime);
else if(!(c%3))
printf("Case #%d: %lld\n",i,(tabf3_3[r]+tabfn3_3[r])%prime);
else if(!(c%4))
printf("Case #%d: %lld\n",i,(tabf3_4[r]+tabfn3_4[r])%prime);
else 
printf("Case #%d: %lld\n",i,(tabf3[r]+tabfn3[r])%prime);
}



return 0;
}
