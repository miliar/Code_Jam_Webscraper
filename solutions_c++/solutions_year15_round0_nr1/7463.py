/*************************************************************************
	> File Name: gcja.cpp
	> Author: WeeiCv  
	> Mail: cheneiweei@gamil.com
	> Created Time: 六  4/11 12:39:08 2015
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<cstring>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>

using namespace std;
const int maxn = 100000;
char a[maxn];
int cur[maxn];

int main()
{
   FILE *fin=fopen("input.txt","r");
   FILE *fout=fopen("output.txt","w");
   
   int T,n;
   fscanf(fin,"%d",&T);
   for(int i=0;i<T;i++){
       fscanf(fin,"%d",&n);
       fscanf(fin,"%s",a);
       for(int kk=0;kk<n;kk++)
           cur[kk]=a[kk]-'0';
       int tem=cur[0];
       int ans=0;
       for(int k=1;k<=n;k++){
           if(tem<k){
               ans+=k-tem;
               tem+=cur[k]+k-tem;
           }
           else{
               tem+=cur[k];
           }
       }
       fprintf(fout,"Case #%d: %d\n",i+1,ans);
   }
   return 0;
}
