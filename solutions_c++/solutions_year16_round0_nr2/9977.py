/*
ID: Jack Avins
PROG: Revenge of the Pancakes
LANG: C++
*/

#include<iostream>
#include<fstream>

using namespace std;

void flip(string &m,int n)
{
    for(int i=n;i>=0;i--)
        if(m[i]=='+')
           m[i]='-';
        else
           m[i]='+';
  //cout<<m;
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

  fin.open("B-large.in");
  fout.open("B-large.out");

  int n=file_num(fin),c=0;
  string m;
  fin.get();

  for(int i=0;i<n;i++)
   {
        c=0;
        getline(fin,m);

        for(int i=m.length();i>=0;i--)
            if(m[i]=='-')
            {
                flip(m,i);
                c++;
            }
       fout<<"Case #"<<i+1<<": "<<c<<'\n';
   }

  fin.close();
  fout.close();

  return 0;
}

