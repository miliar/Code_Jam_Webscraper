/*
ID: Jack Avins
PROG: Counting Sheep
LANG: C++
*/

#include<iostream>
#include<fstream>

using namespace std;

int arr[10],k=0;

bool exist(int n)
{
    for(int i=0;i<k;i++)
      if(arr[i]==n)
        return true;

    return false;
}

bool extend(long val)
{
    while(val>0)
    {
        if(!exist(val%10))
        {
            arr[k++]=val%10;
            if(k==10)
                return true;
        }
        val/=10;
    }
    return false;
}

int file_num(ifstream &fin)
{
    char ch[5];
    int val=0,i;

    fin>>ch;

    for(i=0;ch[i]!='\n' && ch[i]!=' ' && ch[i]!='\0';i++)
        val = val*10 +(ch[i]-'0');

   return val;
}

int main()
{

  ifstream fin;
  ofstream fout,fout2;

  fin.open("A-small-attempt0.in");
  fout.open("A-small-attempt0.out");

  int n=file_num(fin),m,j=1;
  long val;
  bool flag=false;
  for(int i=0;i<n;i++)
   {
        j=1;
        m=file_num(fin);
        flag=false;
        for(int i=0;i<10;i++)
            arr[i]=0;
        k=0;

       if(m==0)
       {
           fout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<'\n';
       }
       else
       {
         while(1)
         {
           val=m*j;
           flag=extend(val);
           if(flag)
           {
               fout<<"Case #"<<i+1<<": "<<val<<'\n';
               break;
           }
           j++;
         }
       }
   }

  fin.close();
  fout.close();

  return 0;
}

