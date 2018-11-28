#include<fstream.h>
#include<conio.h>
#include<stdio.h>
#include<string.h>
void main()
{
clrscr();
ifstream fin;
ofstream fout;
fin.open("in.in");
fout.open("out.txt");
int T,x,X,R,C;
char out[50],ch;
fin>>T;
fin.get(ch);
for(x=1;x<=T;x++)
{
fin>>X;
fin.get(ch);
fin>>R;
fin.get(ch);
fin>>C;
fin.get(ch);
if(((R*C)%X)!=0)
strcpy(out,"RICHARD");
else if((X==1||X==2))
strcpy(out,"GABRIEL");
else if((X==3)&&(((R==3)&&(C==1))||((R==1)&&(C==3))))
strcpy(out,"RICHARD");
else if(X==3)
strcpy(out,"GABRIEL");

else if((X==4)&&(((R==4)&&(C==4))||((R==3)&&(C==4))||((R==4)&&(C==3))))
strcpy(out,"GABRIEL");
else if(X==4)
strcpy(out,"RICHARD");
fout<<"Case #"<<x<<": "<<out<<"\n";
}
fin.close();
fout.close();
getch();
}
