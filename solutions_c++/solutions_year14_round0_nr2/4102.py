#include<iostream>
#include<cstdio>
using namespace std;
int main(){
int test,flag,count;
float c,f,x,i,j,incr;
float y1,y2,minm;
scanf("%d",&test);
for(count=1;count<=test;count++){
scanf("%f %f %f",&c,&f,&x);
minm=0;
incr=2;
flag=0;
while(flag==0){y1=(c/incr)+(x/(incr+f));
y2=x/incr;
if(y1<y2)
minm+=c/incr;
else {minm+=x/incr;
flag=1;
}incr+=f;
}printf("Case #%d: %.7f\n",count,minm);
}return 0;}
