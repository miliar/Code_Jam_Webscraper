#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
string s;


void rev(int ind)
{
    int temp[200];
    char yup,tmp;
    int k,l=0;
    cout<<ind<<endl;
    for(k=0;k<=ind;k++)
    {

        if(s[k]=='+')
        {
            temp[k]=0;

        }
        else if(s[k]=='-')
        {
            temp[k]=1;
        }
        l++;
    }
    for(int i=0;i<k;i++)
    {
        cout<<temp[i]<<endl;
    }

    for(int i=0;i<=ind;i++)
    {
        if(temp[ind-i]==0)
            s[i]='-';
        else
            s[i]='+';

    }
}

bool check()
{
    bool flag=true;
    for(int i=0;i<s.length();i++)
    {
        if(s[i]=='+')
        {

        }
        else
        {
            flag=false;
            break;
        }
    }
    return flag;
}


int main()
{
int cnt=0;

string number,arr[110];
ifstream inp_file;
inp_file.open("question.txt");
ofstream out_file;
out_file.open("uv_ans.txt");
getline(inp_file,number);
int lim;
stringstream conver(number);
conver>>lim;

cout<<"\ntest: "<<lim<<endl;

for(int itr=0;itr<lim;itr++)
{
    cnt=0;
getline(inp_file,arr[itr]);
s.clear();
s=arr[itr];
int len=s.length()-1;

while(!check())
    {
     for(int i=len;i>-1;i--)
     {
         if(s[i]=='-' && s[0]!='+')
         {
             rev(i);
             cnt++;
             break;
         }
         else if(s[0]=='+')
         {
             int p;
             for(p=0;p<len;p++)
             {
                 if(s[p]=='-')
                    break;
                 }
             rev(p-1);
             cnt++;
             break;
         }
     }



    }


cout<<s<<endl;

cout<<cnt;
out_file<<"Case #"<<(itr+1)<<": "<<cnt<<"\n";
cout<<"\nCase #"<<(itr+1)<<": "<<cnt<<"\n";
}

return 0;
}
