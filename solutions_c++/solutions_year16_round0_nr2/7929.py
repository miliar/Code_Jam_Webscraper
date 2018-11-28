#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
#include<conio.h>

int compute(vector<char> v);
int main()
{

            int test;
			cin>>test;
			for(int i=1;i<=test;i++)
			{
                  string s;
                  cin>>s;
                  vector<char> v(s.begin(), s.end());
                 /* for(int j=0;j<v.size();j++)
                  {
                      cout<<v[j]<<endl;
                  }*/
                  int answer=compute(v);
                  cout<<"Case #"<<i<<": "<<answer<<endl;

            }
}
bool allzeroes(vector<char> v)
{
    int h=0;
    for(int k=0;k<v.size();k++)
    {
        if(v[k]=='-')
            h++;
    }
    return h==v.size();
}

int compute(vector<char> v)
{
       int d=v.size();
       int flips=0;
       int c;

       for(int i=0;i<d-1;i++)
       {
           c=0;
           for(int j=0;j<=i;j++)
           {
               if(v[i+1]=='-')
               {
                   if(v[j]=='+')
                   {
                       v[j]='-';
                       c++;
                   }
               }
               else if(v[i+1]=='+')
               {
                   if(v[j]=='-')
                   {
                       v[j]='+';
                       c++;
                   }
               }
           }
           if(c>0)
           {
               flips++;
           }
       }

        if(allzeroes(v))
       {
           return flips+1;
       }
        return flips;
}
