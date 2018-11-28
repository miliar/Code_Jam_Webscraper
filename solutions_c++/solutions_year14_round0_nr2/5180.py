# include<stdio.h>
# include<iostream.h>
# include<conio.h>
void main()
{
double c,f,x ,temp1,temp2,time=0.0,base,rate;
int no;
FILE *f1,*f2;
clrscr();

f1=fopen("ques.txt","r");
f2=fopen("ans.txt","w");

fscanf(f1,"%d",&no);
printf(" the no is : %d\n",no);

fscanf(f1,"%lf",&c);
printf(" the no is : %lf\n",c);
//f1>>c;
fscanf(f1,"%lf",&f);
printf(" the no is : %lf\n",f);

fscanf(f1,"%lf",&x);
printf(" the no is : %lf\n",x);

beg:
rate=num;
base=(c/rate);
time=time+base;
temp1=(x/(rate+f));
temp2=((x-c)/rate);

if(temp1<temp2)
{ num=num+f;goto beg; }
else time=time+temp2;

printf(" time is : %lf\n",time);

getch();

}
