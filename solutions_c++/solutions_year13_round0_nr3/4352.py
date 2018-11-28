#include <iostream>
#include<set>
#include <cstring>
#include <stdio.h>
#include <algorithm>

using namespace std;
int64_t s[1000000];
int num;
int find(int64_t x){
  int head=0;int tail=num;
  if (x<s[0]) return 0;
  if (x>s[tail-1]) return num;
  while (head<=tail){
     int mid=(head+tail)/2;
     if (s[mid]==x) return mid+1;
     if (s[mid]>x) tail=mid-1;
     else head=mid+1;
  }
  return tail+1;
}
int main()
{
   freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
   s[0]=1;s[1]=4;s[2]=9;num=3;
    for (int i=1;i<1000;i++){
        if (i%10==0) continue;
        int64_t temp=0,temp1=0;
        int64_t tt=i;
        int64_t bei=1;
        while (tt){
          temp=temp*10+tt%10;
          tt=tt/10;
          bei=bei*10;
        }
        temp1=temp*bei+i;
        int64_t sq=temp1*temp1;
        string str="";
        while(sq){
           str=char(sq%10+48)+str;
           sq=sq/10;
        }bool ok=true;
        for (int j=0;j<str.length()/2;j++){
           if (str[j]!=str[str.length()-j-1]) {
             ok=false;
             break;
           }
        }
        if(ok){s[num]=temp1*temp1;num++;}
        for (int j=0;j<10;j++){
          temp1=temp*bei*10+j*bei+i;
          while(sq){
           str=char(sq%10+48)+str;
           sq=sq/10;
        }bool ok=true;
        for (int j=0;j<str.length()/2;j++){
           if (str[j]!=str[str.length()-j-1]) {
             ok=false;
             break;
           }
        }
        if(ok){s[num]=temp1*temp1;num++;}
        }
        //cout <<temp<<endl;
    }
    sort(s,s+num);
    int T,ca=1;
    scanf("%d",&T);
    int64_t n,m;
 //  for (int i=0;i<num;i++) cout <<s[i]<<' ';cout<<endl;
    while(T--){
      scanf("%I64d%I64d",&n,&m);
     // cout <<m<<' '<<n<<' '<<find(m)<<' '<<find(n-1)<<endl;
      int t=find(m)-find(n-1);
      printf("Case #%d: %d\n",ca++,t);
    }
    return 0;
}
