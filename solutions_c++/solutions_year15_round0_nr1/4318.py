#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;

int main()
{
    ifstream f1;
    ofstream f2;
    f1.open("A-large.in");
    f2.open("output.out");
    int c=1,t,n,people,cnt;
    string str;
    f1>>t;
    while(c<=t)
    {
               f1>>n>>str;
               people = 0;
               cnt = 0;
               for(int i=0;i<=n;i++)
               {
                       if(people>=i)people = people + (str[i]-'0');
                       else 
                       {
                            cnt = cnt + i - people;
                            people = people + (str[i]-'0') + i - people;
                            }
                       }
               f2<<"Case #"<<c++<<": ";
               f2<<cnt<<endl;
               }
    f1.close();
    f2.close();
    //system("pause");
    return 0;
    }
