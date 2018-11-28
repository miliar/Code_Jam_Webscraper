#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#define sf scanf
#define pf printf
#define ll long long int
using namespace std;
int main(){
int t,flag,k;
float c,f,x,i,j,step;
float temp1,temp2,res;
sf("%d",&t);
for(k=1;k<=t;k++){
sf("%f %f %f",&c,&f,&x);
res=0;step=2;flag=0;
while(flag==0){temp1=(c/step)+(x/(step+f));
temp2=x/step;
if(temp1<temp2)
res+=c/step;
else {res+=x/step;
flag=1;
}
step+=f;
}
pf("Case #%d: %.7f\n",k,res);

}
return 0;
}
