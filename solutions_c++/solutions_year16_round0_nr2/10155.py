#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <vector>
#include <sstream>
#include <map>

using namespace std;
int countSubStr(string str)
{
   int res = 0;
   for (int i=0; str[i] !='\0'; i++)
   {
        if (str[i] == '+')
        {
               if (str[i+1] == '-')
                  res++;
        }
   }
   return res;
}

int main()
{
 int T,R=1;
 cin>>T;
 while(T--)
 {
     string s;
     cin>>s;
     int cnt = countSubStr(s),k=0;
     if(s[0]=='-'){
        k+=1;
     }
     cnt = cnt*2;
     k +=cnt;
     cout<<"Case"<<" "<<"#"<<R<<":"<<" "<<k<<'\n';
     R++;
 }
}
