#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<math.h>

int A[10][10],fg[10][10]={0};

int pal(int x)
{int s,d,r;
 s=x;
 r=0;
 while(x)
   {d=x%10;
    r=r*10+d;
    x=x/10;}
 if(s==r)
   return 1;
 else
   return 0;
}

int main()
{int flag,flag1,flag2,flag3,i,j,a,b,t,l,s;
 ifstream fin;
 fin.open("input.txt");
 ofstream fout;
 fout.open("output.txt");
 fin>>t;
 for(i=0;i<t;i++)
   {fin>>a>>b;
    s=0;
    for(j=a;j<=b;j++)
       {flag1=flag2=flag3=0;
        flag1=pal(j);
        l=(int)sqrt(j);
        if((l*l)==j)
          flag2=1;
        flag3=pal(l);
        if(flag1&&flag2&&flag3)
           s++;      
       }
    fout<<"Case #"<<i+1<<": "<<s<<"\n";
   }
 fin.close();
 fout.close();
}
