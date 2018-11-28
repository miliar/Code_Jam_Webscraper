#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

char arr[4][4],count;
int chk2(int f1,int f2,int f3);

int divide(string line,int x)
{
char *a=new char[line.size()+1];
a[line.size()]=0;
memcpy(a,line.c_str(),line.size());
arr[x][0]=a[0];
arr[x][1]=a[1];
arr[x][2]=a[2];
arr[x][3]=a[3];
return 0;
}

int chk()
{int result=0,z=0,flag_t=0,flag_o=0,flag_x=0,flag_dot=0;
for(int z=0;z<=3;z++)
{for(int j=0;j<=3;j++)
{
        if(arr[j][z]=='T') flag_t++;
        if(arr[j][z]=='O') flag_o++;
        if(arr[j][z]=='X') flag_x++;
        if(arr[j][z]=='.') flag_dot++;
        
}
result=chk2(flag_t,flag_o,flag_x);
if(result!=0) return result;
flag_t=0,flag_o=0,flag_x=0;
}


for(int z=0;z<=3;z++)
{for(int j=0;j<=3;j++)
{
        if(arr[z][j]=='T') flag_t++;
        if(arr[z][j]=='O') flag_o++;
        if(arr[z][j]=='X') flag_x++;
        if(arr[z][j]=='.') flag_dot++;
}
result=chk2(flag_t,flag_o,flag_x);
if(result!=0) return result;
flag_t=0,flag_o=0,flag_x=0;
}

for(int j=0;j<=3;j++)
{       if(arr[j][j]=='T') flag_t++;
        if(arr[j][j]=='O') flag_o++;
        if(arr[j][j]=='X') flag_x++;
        if(arr[j][j]=='.') flag_dot++;
}
result=chk2(flag_t,flag_o,flag_x);
if(result!=0) return result;
flag_t=0,flag_o=0,flag_x=0;
int b=3;
for(int j=0;j<=3;j++)
{       if(arr[j][b]=='T') flag_t++;
        if(arr[j][b]=='O') flag_o++;
        if(arr[j][b]=='X') flag_x++;
        if(arr[j][b]=='.') flag_dot++;
        b--;
}
result=chk2(flag_t,flag_o,flag_x);
if(result!=0) return result;

if(flag_dot!=0) return 4;
else return 3;

return 0;
}


int chk2(int f1,int f2,int f3)
{
    int result=0;
    if(f1+f2==4) result=2;
    if(f1+f3==4) result=1;
    return result;
}

int main(int argc, char *argv[])
{
    ifstream myfile ("CJ1.txt");
    ofstream myfile1;
     myfile1.open ("example.txt");
    string line;
  int number,x=0,result;
  int diff;
  if (myfile.is_open())
  {myfile>>number;
  }
  
  for(int i=1;i<=number;i++)
  {while(x!=4) { myfile>>line; divide(line,x); x++;}
  result=chk();
  myfile1<<"Case #"<<i<<": ";
               switch(result)
               {case 1:myfile1<<"X won"<<endl; break;
               case 2 :myfile1<<"O won"<<endl; break;
               case 3 :myfile1<<"Draw"<<endl; break;
               case 4 :myfile1<<"Game has not completed"<<endl; break;
               }
  
  x=0;
  }
    
  myfile1.close();
    
    myfile.close();
  
    system("PAUSE");
    return EXIT_SUCCESS;
}
