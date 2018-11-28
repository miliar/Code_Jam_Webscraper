#include <iostream>
#include <fstream>
using namespace std;
ofstream debugfile("debug.txt");
char getmultiply(char c,bool &f,char d)
{
      string sign=((f)?"-":"+");
      debugfile<<sign<<c<<"*"<<d;
      if(c=='1'&&d=='i')
      {
        return 'i';
      }
      if(c=='1'&&d=='j')
      {
        return 'j';
      }
      if(c=='1'&&d=='k')
      {
        return 'k';
      }
      if(c=='i'&&d=='i')
      {
        f=!f;
        return '1';
      }
      if(c=='i'&&d=='j')
      {
        return 'k';
      }
      if(c=='i'&&d=='k')
      {
        f=!f;
        return 'j';
      }
      if(c=='j'&&d=='i')
      {
        f=!f;
        return 'k';
      }
      if(c=='j'&&d=='j')
      {
        f=!f;
        return '1';
      }
      if(c=='j'&&d=='k')
      {
        return 'i';
      }
      if(c=='k'&&d=='i')
      {
        return 'j';
      }
      if(c=='k'&&d=='j')
      {
        f=!f;
        return 'i';
      }
      if(c=='k'&&d=='k')
      {
        f=!f;
        return '1';
      }
}

int main()
{
  string line;
    ifstream infile ("example.txt");
    ofstream outfile ("output.txt");
    if ((infile.is_open())&&(outfile.is_open()))
    {
      int T;
      int casecurrent=1;
      infile>>T;
      while ( casecurrent<=T )
      {
        int L,X,flag=1;
        infile>>L>>X;
        getline(infile,line);
        getline(infile,line);
        string line1=line;
        char currentchar='1';
        bool minus=false;
        int ifound=0,jfound=0,kfound=0;
        for(int i=0;i<X;i++)
        {
            line1=line;
            for (int j = 0; j < L; j++)
            {
                currentchar=getmultiply(currentchar,minus,line1[j]);
                string sign=((minus)?"-":"+");
                debugfile<<"= "<<sign<<currentchar<<endl;
                if(currentchar=='i'&&(!minus)&&ifound==0)
                {
                  ifound=1;
                  currentchar='1';
                }
                if(currentchar=='j'&&(!minus)&&ifound==1&&jfound==0)
                {
                  jfound=1;
                  currentchar='1';
                }
                /*if(currentchar=='k'&&(!minus)&&ifound==1&&jfound==1&&kfound==0)
                {
                  kfound=1;
                  currentchar='1';
                }*/
            }
        }

        if(ifound==1&&jfound==1&&currentchar=='k'&&(!minus))
        {
          outfile<<"Case #"<<casecurrent++<<": YES"<<endl;
        }
        else
        {
          outfile<<"Case #"<<casecurrent++<<": NO"<<endl;
        }
        debugfile<<"Case #"<<casecurrent-1<<" is over."<<endl;
      }
    }
  }