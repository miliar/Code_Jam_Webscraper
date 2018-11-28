//Tic Tac Toe solwer GCJ by Halfdreamer
#include<iostream>
using namespace std;
int main()
{
int i=0,j,n,flag=3,tmp,k,l,o=1,t;
char a[4][4];
cin>>n;
while(n-->0){
flag=3;
for(i=0;i<4;i++){
for(j=0;j<4;j++){
cin>>a[i][j];}}

for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(a[i][j]=='.'){flag=0;break;}
else if(a[i][j]=='T'){k=i;l=j;}
}}

for(i=0;i<4;i++){
tmp=1;t=6;
for(j=0;j<4;j++)if(a[i][j]!='T'&&a[i][j]!='.')t=j;
for(j=0;j<4;j++)if(a[i][j]!=a[i][t]&&a[i][j]!='T'||a[i][j]=='.'){tmp=0;break;}
if(tmp==1){
if(a[i][t]=='X')flag=1;else flag=2;
break;}}


for(j=0;j<4;j++){
tmp=1;t=6;
for(i=0;i<4;i++)if(a[i][j]!='T'&&a[i][j]!='.')t=i;
for(i=0;i<4;i++)if(a[i][j]!=a[t][j]&&a[i][j]!='T'||a[i][j]=='.'){tmp=0;break;}
if(tmp==1){
if(a[t][j]=='X')flag=1;else flag=2;

break;}
}

tmp=1;
for(i=0;i<4;i++)
if(a[i][i]!=a[0][0]&&a[i][i]!='T'||a[i][i]=='.')tmp=0;
if(tmp==1){if(k==0&&l==0){if(a[2][2]=='X')flag=1;else flag=2;}
else{if(a[0][0]=='X')flag=1;else flag=2;}
}

tmp=1;j=3;
for(i=0;i<4;i++){
if(a[i][j]!=a[0][3]&&a[i][j]!='T'||a[i][j--]=='.')tmp=0;}
if(tmp==1){if(k==0&&l==3){if(a[1][2]=='X')flag=1;else flag=2;}
else{if(a[0][3]=='X')flag=1;else flag=2;}
}

if(flag==0)cout<<"Case #"<<o++<<": "<<"Game has not completed"<<endl;
else if(flag==1)cout<<"Case #"<<o++<<": "<<"X won"<<endl;
else if(flag==2)cout<<"Case #"<<o++<<": "<<"O won"<<endl;
else cout<<"Case #"<<o++<<": "<<"Draw"<<endl;
}
return 0;
}
