#include <iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<map>
#include<vector>
#include<string>
#include<map>
#include<string>
#include<math.h>
using namespace std;
long long int a[1000002];

int main()
{
freopen("A.in","r", stdin);
freopen("output.in","w", stdout);
   int   test,tt;
   cin>>test;
   for(tt=1;tt<=test;tt++) {
     cout<<"Case #"<<tt<<':'<<' ';
     long long A,N,i,j;

     cin>>A>>N;
     for(i=0;i<N;i++) cin>>a[i];
     sort(a,a+N);
     i=0;
     long long cnt=0,f=0;
     long long max =100000000000000;
     while(i<N){
         if(A==1) {cout<<N-i<<endl;f=1;break;}
     while(a[i]<A&&i<N) {A+=a[i];i++;}

     if(i==N&&cnt<max) {max=cnt;}
     else if(cnt+N-i<max) {
     max= cnt+N-i;
     }
     while(A<=a[i]) {A+=A-1;
    cnt++;
     }

     }
         if(!f)
     cout<<max<<endl;}
     }



