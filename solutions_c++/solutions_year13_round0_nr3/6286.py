#include<iostream.h>
#include<stdlib.h>
#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<string.h>
FILE *fp,*fw;
char*tokenize(char**);
palin(unsigned int);
unsigned int square(unsigned int);
palini(unsigned int);
digits(int);
int main(){
unsigned int a,no,b,ar[1000],d=0,n;
int flagmp,t,c=0,test,cnt=1,ac=0;
char *str,*token,ch;
int i=0;
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

	   n = atoi (token);
	  ar[d++]=n;

    }

c++;}




test=ar[ac++];
while(cnt<=test){
c=0;
a=ar[ac++];
b=ar[ac++];
while(a<=b){
flagmp=palin(a);
t=square(a);
if(flagmp==1 && t!=0){
if(palin(t)){
c++;
}
}
a++;
}
cout<<"Case #"<<cnt<<": "<<c<<"\n";
fprintf(fw,"Case #");
fprintf(fw,"%d",cnt);
fprintf(fw,": ");
fprintf(fw,"%d",c);
fprintf(fw,"\n");
cnt++;
}

fclose(fp);
fclose(fw);

getch();
return 0;
}

palin(unsigned int a){
int t,i=0;
unsigned int k,n=0;
k=a;
i=digits(a);
while(a>0){
i--;
t=a%10;
a=a/10;
n=n+((pow(10,i))*t);

}
if(n==k)
return 1;
else
return 0;
}

digits(int a){
int i=0;
while(a>0){
a=a/10;
i++;
}
return i;
}

unsigned int square(unsigned int a){
unsigned i;
i=sqrt(a);
if((sqrt(a)-i)==0)
return i;
i++;

return 0;
}

char * tokenize ( char ** str){

    // str = "     30 40 1234 456 -234"
      while (**str == ' ' && **str != NULL ) (*str)++ ;
    char *num = *str ;
    while ((**str) !=  ' '&& **str!=NULL ) (*str)++;
   if(**str == '\0' ) num=NULL;
    *str ++;
    return num;

}
