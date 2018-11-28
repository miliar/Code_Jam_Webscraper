#include<iostream.h>
#include<stdio.h>
#include<conio.h>
FILE *fr,*fw;
int main(){

int i=0,j=0,x=0,y=0,flag=-1,c=1,t=0,k=0;
char arr[4][4],ch,in[10000];
fr=fopen("A.txt","r");
fw=fopen("OUT.txt","w");
clrscr();
// test case input
fscanf(fr,"%d",&t);

while((ch=getc(fr))!=EOF){
if(ch!='\n')
in[k++]=ch;
}
in[k++]='\0';
k=0;
while(c<=t){
x=0;
y=0;
flag=-1;
//board input
for(i=0;i<4;i++){
for(j=0;j<4;j++){
arr[i][j]=in[k++];
}
}



//for X
for(i=0;i<4;i++){
x=0;
for(j=0;j<4;j++){
if(arr[i][j]=='X'||arr[i][j]=='T'){
x++;}
if(x==4){
flag=0;
goto E;
}
}
}


for(i=0;i<4;i++){
x=0;
for(j=0;j<4;j++){
if(arr[j][i]=='X'||arr[i][j]=='T'){
x++;}
if(x==4){
flag=0;
goto E;
}
}
}

x=0;
for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(i==j) {
if(arr[i][j]=='X'||arr[i][j]=='T'){
x++;}     }
if(x==4){
flag=0;
goto E;
}
}
}
    x=0;
for(i=0;i<4;i++){
for(j=3;j>=0;j--){
if((i+j)==3) {
if(arr[i][j]=='X'||arr[i][j]=='T'){
x++;}     }
if(x==4){
flag=0;
goto E;
}
}
}


//for O
for(i=0;i<4;i++){
y=0;
for(j=0;j<4;j++){
if(arr[i][j]=='O'||arr[i][j]=='T'){
y++;}
if(y==4){
flag=1;
goto E;
}
}
}

for(i=0;i<4;i++){
y=0;
for(j=0;j<4;j++){
if(arr[j][i]=='O'||arr[i][j]=='T'){
y++;}
if(y==4){
flag=1;
goto E;
}
}
}
y=0;
for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(i==j) {
if(arr[i][j]=='O'||arr[i][j]=='T'){
y++;}     }
if(y==4){
flag=1;
goto E;
}
}
}
y=0;
for(i=0;i<4;i++){
for(j=3;j>=0;j--){
if((i+j)==3) {
if(arr[i][j]=='O'||arr[i][j]=='T'){
y++;}     }
if(y==4){
flag=1;
goto E;
}
}
}


//not completed case
for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(arr[i][j]=='.'){
flag=2;
goto E;
}
}
}

E:

cout<<"Case#"<<c;
fprintf(fw,"Case #");
fprintf(fw,"%d",c);
switch(flag){
case -1: cout<<": Draw";
fprintf(fw,": Draw");
break;
case 0: cout<<": X won";
fprintf(fw,": X won");
break;
case 1: cout<<": O won";
fprintf(fw,": O won");
break;
case 2: cout<<": Game has not completed";
fprintf(fw,": Game has not completed");
break;
}
cout<<"\n";
fprintf(fw,"\n");
c++;
}
fclose(fr);
fclose(fw);
getch();
return 0;
}
#include<iostream.h>
#include<stdio.h>
#include<conio.h>
FILE *fr,*fw;
int main(){

int i=0,j=0,x=0,y=0,flag=-1,c=1,t=0,k=0;
char arr[4][4],ch,in[10000];
fr=fopen("A.txt","r");
fw=fopen("OUT.txt","w");
clrscr();
// test case input
fscanf(fr,"%d",&t);

while((ch=getc(fr))!=EOF){
if(ch!='\n')
in[k++]=ch;
}
in[k++]='\0';
k=0;
while(c<=t){
x=0;
y=0;
flag=-1;
//board input
for(i=0;i<4;i++){
for(j=0;j<4;j++){
arr[i][j]=in[k++];
}
}



//for X
for(i=0;i<4;i++){
x=0;
for(j=0;j<4;j++){
if(arr[i][j]=='X'||arr[i][j]=='T'){
x++;}
if(x==4){
flag=0;
goto E;
}
}
}


for(i=0;i<4;i++){
x=0;
for(j=0;j<4;j++){
if(arr[j][i]=='X'||arr[i][j]=='T'){
x++;}
if(x==4){
flag=0;
goto E;
}
}
}

x=0;
for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(i==j) {
if(arr[i][j]=='X'||arr[i][j]=='T'){
x++;}     }
if(x==4){
flag=0;
goto E;
}
}
}
    x=0;
for(i=0;i<4;i++){
for(j=3;j>=0;j--){
if((i+j)==3) {
if(arr[i][j]=='X'||arr[i][j]=='T'){
x++;}     }
if(x==4){
flag=0;
goto E;
}
}
}


//for O
for(i=0;i<4;i++){
y=0;
for(j=0;j<4;j++){
if(arr[i][j]=='O'||arr[i][j]=='T'){
y++;}
if(y==4){
flag=1;
goto E;
}
}
}

for(i=0;i<4;i++){
y=0;
for(j=0;j<4;j++){
if(arr[j][i]=='O'||arr[i][j]=='T'){
y++;}
if(y==4){
flag=1;
goto E;
}
}
}
y=0;
for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(i==j) {
if(arr[i][j]=='O'||arr[i][j]=='T'){
y++;}     }
if(y==4){
flag=1;
goto E;
}
}
}
y=0;
for(i=0;i<4;i++){
for(j=3;j>=0;j--){
if((i+j)==3) {
if(arr[i][j]=='O'||arr[i][j]=='T'){
y++;}     }
if(y==4){
flag=1;
goto E;
}
}
}


//not completed case
for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(arr[i][j]=='.'){
flag=2;
goto E;
}
}
}

E:

cout<<"Case#"<<c;
fprintf(fw,"Case #");
fprintf(fw,"%d",c);
switch(flag){
case -1: cout<<": Draw";
fprintf(fw,": Draw");
break;
case 0: cout<<": X won";
fprintf(fw,": X won");
break;
case 1: cout<<": O won";
fprintf(fw,": O won");
break;
case 2: cout<<": Game has not completed";
fprintf(fw,": Game has not completed");
break;
}
cout<<"\n";
fprintf(fw,"\n");
c++;
}
fclose(fr);
fclose(fw);
getch();
return 0;
}
#include<iostream.h>
#include<stdio.h>
#include<conio.h>
FILE *fr,*fw;
int main(){

int i=0,j=0,x=0,y=0,flag=-1,c=1,t=0,k=0;
char arr[4][4],ch,in[10000];
fr=fopen("A.txt","r");
fw=fopen("OUT.txt","w");
clrscr();
// test case input
fscanf(fr,"%d",&t);

while((ch=getc(fr))!=EOF){
if(ch!='\n')
in[k++]=ch;
}
in[k++]='\0';
k=0;
while(c<=t){
x=0;
y=0;
flag=-1;
//board input
for(i=0;i<4;i++){
for(j=0;j<4;j++){
arr[i][j]=in[k++];
}
}



//for X
for(i=0;i<4;i++){
x=0;
for(j=0;j<4;j++){
if(arr[i][j]=='X'||arr[i][j]=='T'){
x++;}
if(x==4){
flag=0;
goto E;
}
}
}


for(i=0;i<4;i++){
x=0;
for(j=0;j<4;j++){
if(arr[j][i]=='X'||arr[i][j]=='T'){
x++;}
if(x==4){
flag=0;
goto E;
}
}
}

x=0;
for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(i==j) {
if(arr[i][j]=='X'||arr[i][j]=='T'){
x++;}     }
if(x==4){
flag=0;
goto E;
}
}
}
    x=0;
for(i=0;i<4;i++){
for(j=3;j>=0;j--){
if((i+j)==3) {
if(arr[i][j]=='X'||arr[i][j]=='T'){
x++;}     }
if(x==4){
flag=0;
goto E;
}
}
}


//for O
for(i=0;i<4;i++){
y=0;
for(j=0;j<4;j++){
if(arr[i][j]=='O'||arr[i][j]=='T'){
y++;}
if(y==4){
flag=1;
goto E;
}
}
}

for(i=0;i<4;i++){
y=0;
for(j=0;j<4;j++){
if(arr[j][i]=='O'||arr[i][j]=='T'){
y++;}
if(y==4){
flag=1;
goto E;
}
}
}
y=0;
for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(i==j) {
if(arr[i][j]=='O'||arr[i][j]=='T'){
y++;}     }
if(y==4){
flag=1;
goto E;
}
}
}
y=0;
for(i=0;i<4;i++){
for(j=3;j>=0;j--){
if((i+j)==3) {
if(arr[i][j]=='O'||arr[i][j]=='T'){
y++;}     }
if(y==4){
flag=1;
goto E;
}
}
}


//not completed case
for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(arr[i][j]=='.'){
flag=2;
goto E;
}
}
}

E:

cout<<"Case#"<<c;
fprintf(fw,"Case #");
fprintf(fw,"%d",c);
switch(flag){
case -1: cout<<": Draw";
fprintf(fw,": Draw");
break;
case 0: cout<<": X won";
fprintf(fw,": X won");
break;
case 1: cout<<": O won";
fprintf(fw,": O won");
break;
case 2: cout<<": Game has not completed";
fprintf(fw,": Game has not completed");
break;
}
cout<<"\n";
fprintf(fw,"\n");
c++;
}
fclose(fr);
fclose(fw);
getch();
return 0;
}
#include<iostream.h>
#include<stdio.h>
#include<conio.h>
FILE *fr,*fw;
int main(){

int i=0,j=0,x=0,y=0,flag=-1,c=1,t=0,k=0;
char arr[4][4],ch,in[10000];
fr=fopen("A.txt","r");
fw=fopen("OUT.txt","w");
clrscr();
// test case input
fscanf(fr,"%d",&t);

while((ch=getc(fr))!=EOF){
if(ch!='\n')
in[k++]=ch;
}
in[k++]='\0';
k=0;
while(c<=t){
x=0;
y=0;
flag=-1;
//board input
for(i=0;i<4;i++){
for(j=0;j<4;j++){
arr[i][j]=in[k++];
}
}



//for X
for(i=0;i<4;i++){
x=0;
for(j=0;j<4;j++){
if(arr[i][j]=='X'||arr[i][j]=='T'){
x++;}
if(x==4){
flag=0;
goto E;
}
}
}


for(i=0;i<4;i++){
x=0;
for(j=0;j<4;j++){
if(arr[j][i]=='X'||arr[i][j]=='T'){
x++;}
if(x==4){
flag=0;
goto E;
}
}
}

x=0;
for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(i==j) {
if(arr[i][j]=='X'||arr[i][j]=='T'){
x++;}     }
if(x==4){
flag=0;
goto E;
}
}
}
    x=0;
for(i=0;i<4;i++){
for(j=3;j>=0;j--){
if((i+j)==3) {
if(arr[i][j]=='X'||arr[i][j]=='T'){
x++;}     }
if(x==4){
flag=0;
goto E;
}
}
}


//for O
for(i=0;i<4;i++){
y=0;
for(j=0;j<4;j++){
if(arr[i][j]=='O'||arr[i][j]=='T'){
y++;}
if(y==4){
flag=1;
goto E;
}
}
}

for(i=0;i<4;i++){
y=0;
for(j=0;j<4;j++){
if(arr[j][i]=='O'||arr[i][j]=='T'){
y++;}
if(y==4){
flag=1;
goto E;
}
}
}
y=0;
for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(i==j) {
if(arr[i][j]=='O'||arr[i][j]=='T'){
y++;}     }
if(y==4){
flag=1;
goto E;
}
}
}
y=0;
for(i=0;i<4;i++){
for(j=3;j>=0;j--){
if((i+j)==3) {
if(arr[i][j]=='O'||arr[i][j]=='T'){
y++;}     }
if(y==4){
flag=1;
goto E;
}
}
}


//not completed case
for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(arr[i][j]=='.'){
flag=2;
goto E;
}
}
}

E:

cout<<"Case#"<<c;
fprintf(fw,"Case #");
fprintf(fw,"%d",c);
switch(flag){
case -1: cout<<": Draw";
fprintf(fw,": Draw");
break;
case 0: cout<<": X won";
fprintf(fw,": X won");
break;
case 1: cout<<": O won";
fprintf(fw,": O won");
break;
case 2: cout<<": Game has not completed";
fprintf(fw,": Game has not completed");
break;
}
cout<<"\n";
fprintf(fw,"\n");
c++;
}
fclose(fr);
fclose(fw);
getch();
return 0;
}
