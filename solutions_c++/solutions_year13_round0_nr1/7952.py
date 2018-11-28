#include<iostream>
#include<string.h>
#include<fstream>
#include<sstream>
#include<stdlib.h>

using namespace std;
int  *a;
int decide()
{
    int f;
    int no,s[10]={0,0,0,0,0,0,0,0,0,0};
    for(int i=0;i<15;i++)
    {
       if(i%4==0)
            s[0]=s[0]+a[i];
       else if((i-1)%4==0)
            s[1]=s[1]+a[i];
       else if((i-2)%4==0)
            s[2]=s[2]+a[i];
       else if((i-3)%4==0)
            s[3]=s[3]+a[i];
        if(i<=3)
           s[4]=s[4]+a[i];
        else if((i>3)&&(i<=7))
           s[5]=s[5]+a[i];
        else if((i>7)&&(i<=11))
           s[6]=s[6]+a[i];
        else if((i>11)&&(i<=15))
           s[7]=s[7]+a[i];
    }
    s[8]=a[0]+a[5]+a[10]+a[15];
    s[9]=a[3]+a[6]+a[9]+a[12];
    for(int i=0;i<10;i++)
        {
            if((s[i]==20)||(s[i]==115))
               return 1;
            else if((s[i]==0)||(s[i]==100))
                    return 2;
            else if((s[i]%5!=0))
                        f=4;

        }
        if (f!=4)
            f=3;
        return f;

}
int main()
{

  char ch;
  char w[]={"X won"};
  char d[]={"O won"};
  char g[]={"Draw"};
  char l[]={"Game has not completed"};
  int n,i,c,f;
  string s;
  ifstream fin;
  ofstream fot,fct;
  fin.open("gg.in");
  fot.open("ans.out");
 // fct.open("wtf.out");
 getline(fin,s);
  stringstream(s) >> n;

for(int i=0;i<n;i++)
{
a=new int[15];
    c=0;
     while ((c<=15)&&(fin >> ch))
    {

        if(ch=='X')
            a[c]=5;
        else if (ch=='O')
        a[c]=0;
        else if (ch=='T')
        a[c]=100;
        else
        a[c]=1;

        c++;
    }

  /*  for (int j=0;j<16;j++)
    {
        if(j%4==0)
            cout<<endl;
        cout<<a[j];

    }*/
    f=decide();

switch(f)
{
case 1:
    fot<<"Case #"<<i+1<<": "<<w<<endl;
    break;
case 2:
     fot<<"Case #"<<i+1<<": "<<d<<endl;
    break;
case 3:
     fot<<"Case #"<<i+1<<": "<<g<<endl;
    break;
case 4:
     fot<<"Case #"<<i+1<<": "<<l<<endl;
    break;
}

delete[] a;
}

  fin.close();
  fot.close();

}
