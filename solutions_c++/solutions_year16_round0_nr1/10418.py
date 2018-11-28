#include<iostream>
#include<cstdio>

using namespace std;

long func(long n,int i,int a[]){
if(n==0)
return 0;
long temp=n*i,g;

while(temp>0){
g=temp%10;
a[g]=1;
temp/=10;
}

int x=0,c=0;
for(int j=0;j<10;j++){
if(a[j]==0){
x=0;
break;
}
c++;
}
if(c==10)
x=1;
i++;
if(x==0)
func(n,i,a);
if(x==1)
return n*(i-1);
}


int main(){
int t,count=1;
long n;
scanf("%d",&t);
while(t--){
scanf("%ld",&n);
int a[10]={0};
long b=func(n,1,a);
if(b==0)
printf("Case #%d: INSOMNIA\n",count);
else
printf("Case #%d: %ld\n",count,b);
count++;
}
return 0;
}
