/*By Hitesh Kalwani (India)*/
#include<bits/stdc++.h>
using namespace std;
int main(){
  freopen("D-small-attempt3.in","r",stdin);
  freopen("output.out","w",stdout);
  long long x,r,c,a[4][4][4],t;

  for(int i=0;i<4;i++){
   for(int j=0;j<4;j++){
    for(int k=0;k<4;k++){
            a[i][j][k]=0; }}}

//diagonal
  for(int i=0;i<4;i++){
    for(int k=0;k<=i;k++){
            a[i][i][k]=1;}}

//vertical
    for(int k=0;k<4;k++){
            a[k][0][0]=1;
            a[0][k][0]=1;
           if(k%2!=0){
                a[k][0][1]=1;
                a[0][k][1]=1;}}

//remailning
for(int k=0;k<4;k++){
    a[3][2][k]=1;
    a[2][3][k]=1;
    if(k<2){
        a[3][1][k]=1;
        a[1][3][k]=1;}
    if(k<3){
    a[2][1][k]=1;
    a[1][2][k]=1;
    }}

a[3][3][2]=0;
a[2][2][1]=0;

  cin>>t;
  for(long long cas=1;cas<=t;cas++){
    cin>>x>>r>>c;
    string s="";
    s=(a[r-1][c-1][x-1])?"GABRIEL":"RICHARD";
    cout<<"Case #"<<cas<<": "<<s<<endl;}
return 0;}

