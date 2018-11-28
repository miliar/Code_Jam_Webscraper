//in the name of GOD
#include<fstream.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
void getpq(char string[50],char p[50],char q[50]);
int check(char p[50],char q[50]);
double stod(char q[50]);

void main()
{
clrscr();
int cases,done=0,possible;
char string[50],p[50],q[50];
long i,j,k,pl,ql;
long gen;
ifstream ifile("3ra.in",ios::in);
ofstream ofile("3ra.out",ios::out);
ifile>>cases;

while(done<cases)
{
ifile>>string;
getpq(string,p,q);
possible=check(p,q);
gen=0;
if(possible==1)
{
pl=atol(p);
ql=atol(q);
while((pl/ql)<1)
{
ql=ql/2;
gen=gen+1;
}
done=done+1;
ofile<<"Case #"<<done<<": "<<gen<<"\n";
}
else
{
done=done+1;
ofile<<"Case #"<<done<<": "<<"impossible"<<"\n";
}
}
getch();
}


void getpq(char string[50],char p[50],char q[50])
{
int i,j;
for(i=0;string[i]!='/';i++)
{
p[i]=string[i];
}
p[i]='\0';
i++;
j=0;
for(;string[i]!='\0';i++)
{
q[j]=string[i];
j++;
}
q[j]='\0';
}

int check(char p[50],char q[50])
{
float ql;
ql=stod(q);
while(ql>1)
{
ql=ql/2.0;
}
if(ql==1.0)
{
return 1;
}
else
{
return 0;
}
}

double stod(char q[50])
{
int i=0;
double qd=0;
for(i=0;q[i]!='\0';i++)
{
qd=qd*10+(q[i]-'0');
}
return qd;
}
