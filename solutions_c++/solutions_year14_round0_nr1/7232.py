//Lasha Bukhnikashvili
#include<iostream>
#include<stdio.h>
#include<math.h>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<string>
#define Pi 3.14159265358
#define mod9 %1000000009
#define INF 1000000001
#define mod7 1000000009
#define LL  long long
#define time clock()/(double)CLOCKS_PER_SEC
using namespace std;
 int T,id,i,j,x,y,a[5][5],s,num,b[5][5],p[17];
int main(){
#ifndef ONLINE_JUDGE
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
 #endif
   cin>>T;
   while (T--){
         id++;
         cin>>x;
         for (i=1;i<=4;i++)
             for (j=1;j<=4;j++)
                 cin>>a[i][j];
         cin>>y;
         for (i=1;i<=4;i++)
             for (j=1;j<=4;j++)
                 cin>>b[i][j];
         p[a[x][1]]++;
         p[a[x][2]]++;
         p[a[x][3]]++;
         p[a[x][4]]++;
         p[b[y][1]]++;
         p[b[y][2]]++;
         p[b[y][3]]++;
         p[b[y][4]]++;
         num=0;
         for (i=1;i<=16;i++){
             if (p[i]==2) s=i,num++;
             p[i]=0;
         };
         if (num>1) {
            cout<<"Case #";
            cout<<id;
            cout<<": ";
            cout<<"Bad magician!"<<endl;
         };    
         if (num==0){
            cout<<"Case #";
            cout<<id;
            cout<<": ";
            cout<<"Volunteer cheated!"<<endl;
         };
         if (num==1){
            cout<<"Case #";
            cout<<id;
            cout<<": ";
            cout<<s<<endl;
         };
   };
 return 0;
}
 
