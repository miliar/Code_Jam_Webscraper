#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
 int t,r,n,m,k,x;
 scanf("%d",&t);
 scanf("%d %d %d %d",&r,&n,&m,&k);
printf("Case #1:\n");
 for(int i=0;i<r;i++){
  vector<int> v;
  vector<int> p(8);
  vector<int> pm(8);
  for(int j=0;j<k;j++){
  vector<int> pmtemp(8);
scanf("%d",&x);v.push_back(x);
while(!(x%2)){x/=2;pmtemp[2]++;}
while(!(x%3)){x/=3;pmtemp[3]++;}
while(!(x%5)){x/=5;pmtemp[5]++;}
while(!(x%7)){x/=7;pmtemp[7]++;}
pm[2]=max(pm[2],pmtemp[2]);
p[2]+=pmtemp[2];
pm[3]=max(pm[3],pmtemp[3]);
p[3]+=pmtemp[3];
pm[5]=max(pm[5],pmtemp[5]);
p[5]+=pmtemp[5];
pm[7]=max(pm[7],pmtemp[7]);
p[7]+=pmtemp[7];
}

p[2]-=(k*pm[2])/n;
p[3]-=(k*pm[3])/n;
p[5]-=(k*pm[5])/n;
p[7]-=(k*pm[7])/n;

//pm = max multiple num of
// p = #times it appears (compare to k/n)
int nn = n;
vector<int> ans(8);
while(nn){
if(pm[7]){printf("7");nn--;pm[7]--;continue;}
if(pm[5]){printf("5");nn--;pm[5]--;continue;}
if(pm[3]){printf("3");nn--;pm[3]--;continue;}//ATTENTION
if(nn==1 & pm[2]==1){printf("2");nn--;}
if(nn==1 & pm[2]==2){printf("4");nn--;}
if(nn==2 & pm[2]==1){printf("22");nn-=2;}
if(nn==2 & pm[2]==2){printf("22");nn-=2;}
if(nn==2 & pm[2]==3){printf("24");nn-=2;}
if(nn==2 & pm[2]==4){printf("44");nn-=2;}
if(nn==3 & pm[2]>=3){printf("4");pm[2]-=2;nn-=1;}
if(nn==3 & pm[2]<3){printf("2");pm[2]-=1;nn-=1;}
if(!pm[2]){printf("2");nn--;}
//printf("nn=%d %d \n",nn,pm[2]);
}
printf("\n");
}//end for
}


