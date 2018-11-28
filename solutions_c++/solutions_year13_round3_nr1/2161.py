#include <fstream>
#include<iostream>
#include<string.h>
using namespace std;
int isValid(char name[1000],int x,int y,int cunso)
{
int i,count=0,flag=1;
for(i=x;i<=y;i++)
  {
       if(name[i]!='a'&& name[i]!='e'&&name[i]!='i'&& name[i]!='o'&& name[i]!='u')
       {
           count++;
       }
       else {if(count>=cunso)
               break;
                else 
                count=0;
            }
  }
if(count>=cunso)
return 1;
else 
return 0;
}
int check(char name[1000],int cunso)
{
int i,count=0;
i=0;
while(name[i]!='\0')
{
if(name[i]!='a'&& name[i]!='e'&&name[i]!='i'&& name[i]!='o'&& name[i]!='u')
    {
count++;
    }

i++;
}
if(count>=cunso)
return 1;
else 
return 0;
}
int main () {
   fstream fin,fout;
   char name[1000];
   int n,cunso,index,lenght,status,x,y;
   fout.open("fout.txt",ios::out);
   fin.open ("A-small-attempt2.in",ios::in);
   fin>>n;
    for(index=0;index<n;index++)
    {
         status=0;
         fin>>name;
         fin>>cunso;
         lenght=strlen(name);
         for(x=0;x<lenght;x++)
         {
             for(y=lenght-1;y>=x;y--)
             {
		if(isValid(name,x,y,cunso)==1)
                {status++;}
             }
         }
      fout<<"Case #"<<index+1<<": "<<status<<"\n";
    }  

   fin.close();
   fout.close();
  return 0;
}
