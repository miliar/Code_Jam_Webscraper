#include<iostream>
#include<cstdio>
#include<string>

using namespace std;
int fin(string str);
int main()
{
    freopen("bl.txt", "r", stdin);
    freopen("bsoll.txt", "w", stdout);
    int tst ,ctr,ind;
    string str;
    cin >> tst;
    for(int ii=1;ii<=tst;ii++)
    {
         ctr=0;
         cin >> str;
         while(fin(str)>=0)
         {
              ind=fin(str);
              for(int jj=0;jj<=ind;jj++)
              {
                  if(str[jj]=='+')
                      str[jj]='-';
                  else
                      str[jj]='+';
              }
              ctr++;
         }
         cout<<"Case #"<<ii<<": "<<ctr<<endl;
    }
    return 0;
}

int fin(string str)
{
     for(int ii=str.length()-1;ii>=0;ii--)
     {
         if(str[ii]=='-')
            return ii;
     }
     return -1;

}
