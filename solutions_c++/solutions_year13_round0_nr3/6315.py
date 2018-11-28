#include<iostream>
#include<sstream>
#include<fstream>
#include<cmath>
const int limit=50;
int d,e;
using namespace std;
class stack
{
      private:
              
              char contents[limit];
              int topposition;
      public:
             stack()
             {
                    topposition=0;
             }
             void push(char x)
             {
                  if(!isfull())
                  {
                               contents[topposition]=x;
                               topposition++;
                  }
             }
             char pop()
             {
                 if(!isempty())
                 {
                               topposition--;
                               return contents[topposition];
                 }
             }
             bool isfull()
             {
                  if(topposition>=limit)
                                        return true;
                  return false;
             }
             bool isempty()
             {
                  if(topposition==0)
                                        return true;
                  return false;
             }
};
bool fair(string b);
bool square(string b);
bool squarerootisinrange(int a);
int main()
{
    int m;
    ifstream fin;
    ofstream fout;
    fout.open("output");
    fin.open("C-small-attempt0.in");
    fin>>m;
    for(int g=1;g<=m;g++)
    {
    fin>>d>>e;
    int count=0;
    //cout<<d<<" "<<e<<endl;
    for(int l=d;l<=e;l++)
    {
            string b;
            ostringstream convert;
            convert <<l;
            b=convert.str();
            string f;
            ostringstream sq;
            sq <<sqrt(l);
            f=sq.str();
            if((fair(b))&& (square(f)))//&&(squarerootisinrange(sqrt(l)))
            {
                                count++;
            }
    }
    fout<<"Case #"<<g<<": "<<count<<endl;
    }
    system("pause");
    return 0;
}
bool fair(string b)
{
     bool palindrome=true;
     stack s1,s2,s3;
     for(int i=0;i<b.length();i++)
     {
            s1.push(b[i]);
     }
    for(int i=0;i<b.length();i++)
    {
            s2.push(s1.pop());
            s3.push(b[i]);
    }
    for(int i=0;i<b.length();i++)
    {
            if((s2.pop())!= (s3.pop()))
            {
                                  palindrome=false;;
            }
    }
    return palindrome;
}
bool square(string b)
{
     bool palindrome=true;
     stack s1,s2,s3;
     for(int i=0;i<b.length();i++)
     {
            s1.push(b[i]);
     }
    for(int i=0;i<b.length();i++)
    {
            s2.push(s1.pop());
            s3.push(b[i]);
    }
    for(int i=0;i<b.length();i++)
    {
            if((s2.pop())!= (s3.pop()))
            {
                                  palindrome=false;;
            }
    }
    return palindrome;
}
bool squarerootisinrange(int a)
{
     if(a>=d)
     return true;
     else
     return false;
}     
