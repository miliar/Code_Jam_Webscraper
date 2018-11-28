#include<iostream.h>
#include<stdlib.h>
#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<string.h>
FILE *fp,*fw;

char*tokenize(char**);

int main(){

unsigned int ar[20000],d=0,v,ac=0;
int test,t1,cnt=1,c=0,l[10][10],n,m,i=0,j,large=-1,sec[10][10],l2[10][10],posi,posj,flag1,flag2,flag;
char *str,*token,ch;
fp=fopen("A.txt","r");
fw=fopen("OUT.txt","w");
clrscr();


str=(char*)malloc(4096);

while((ch=fgetc(fp))!=EOF){
if(ch=='\n')
i++;
}
i++;
fclose(fp);
fp=fopen("A.txt","r");
while(c<i){
fgets (str, 4096, fp);

    strcat(str," ");
   while ( (token = tokenize ( &str )) != NULL){

	   v = atoi (token);
	  ar[d++]=v;

    }

c++;
}


ac=0;
test=ar[ac++];
fflush(fp);
while(cnt<=test){
n=ar[ac++];
m=ar[ac++];

for(i=0;i<n;i++){
for(j=0;j<m;j++){
sec[i][j]=0;
}
 }


for(i=0;i<n;i++){
for(j=0;j<m;j++){
l[i][j]=ar[ac++];
}
 }



 for(i=0;i<n;i++){
for(j=0;j<m;j++){
l2[i][j]=l[i][j];
}
 }
  large=1;
//main logic
while(large!=0){
large=0;
posi=0;posj=0;
for(i=0;i<n;i++){
for(j=0;j<m;j++){
if(l[i][j]>large){
large=l[i][j];
posi=i;
posj=j;
}
}
 }

 l[posi][posj]=0;


flag1=0;
flag2=0;

for(t1=0;t1<m;t1++){
if(l2[posi][t1]>large)
flag1=1;
}
for(t1=0;t1<n;t1++){
if(l2[t1][posj]>large)
flag2=1;
}

if(flag1==0 || flag2==0)
sec[posi][posj]=l2[posi][posj];

}

flag=1;
for(i=0;i<n;i++){
for(j=0;j<m;j++){
if(sec[i][j]==0)
flag=0;
}
 }

cout<<"Case #"<<cnt<<": ";
fprintf(fw,"Case #");
fprintf(fw,"%d",cnt);
if(flag==1){
cout<<"YES"<<"\n";
fprintf(fw,": YES");
}
else{
cout<<"NO"<<"\n";
fprintf(fw,": NO");
}
fprintf(fw,"\n");

cnt++;
}

fclose(fp);
fclose(fw);

getch();
return 0;
}

char * tokenize ( char ** str){


      while (**str == ' ' && **str != NULL ) (*str)++ ;
    char *num = *str ;
    while ((**str) !=  ' '&& **str!=NULL ) (*str)++;
   if(**str == '\0' ) num=NULL;
    *str ++;
    return num;

}