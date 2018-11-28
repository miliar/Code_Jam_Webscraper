#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<cmath>
#include<string>
#include<string.h>
#include<strings.h>
#include<iomanip>
#include<cstdio>
#include<bitset>
#include<fstream>
using namespace std;
int main(){
  ofstream fout ("B-largeout.txt");
  ifstream fin ("B-large.in");
  int x, flagy, t, T, i, flag, j, count;
  string s;
  fin>>T;
  for(t=1;t<=T;++t){
    flag=0;
    flagy=0;
    count=0;
    fin>>s;
    x=s.length();
    for(i=0;i<x;++i){
        if(s[i]=='-')
        {
            flag=1;
            break;
        }
    }
    if(flag==0)
    {
        fout<<"Case #"<<t<<": "<<0<<endl;
        continue;
    }
    count=0;
    if(s[x-1]=='-'){
        flag=0;
        flagy=0;
        count++;
        for(i=0;i<x;i++){
            if(s[i]=='-')
                s[i]='+';
            else
                s[i]='-';
        }
     while(1){
        //fout<<s<<endl;
        i=0;
        flag=0;
        flagy=0;
        for(i=0;i<x;i++)
        {

            if(s[i]=='-')
                {
                    flag=1;
                    break;
                }
        }
        if(flag==0)
        {
            fout<<"Case #"<<t<<": "<<count<<endl;
            break;
        }
        flag=0;
        //for(i=0;i<x-1;i++){
        //    if(s[i]=='+')
        //        flagy=1;
        //}
        i=0;
        while(s[i]=='-'){
            i++;
        }
        while(s[i]=='+'){
            i++;
        }
        if(i==x)
            flagy=1;
        if(flagy==1&&s[x-1]=='+')
        {
                count++;
                fout<<"Case #"<<t<<": "<<count<<endl;
                break;
        }
        while(s[i]!='-'&&i!=x-1)
            i++;

        for(j=0;j<i;j++){
            if(s[j]=='+')
                s[j]='-';
            else
                s[j]='+';
        }
        count++;

     }

    }
    else{
        i=0;
        flag=0;
        flagy=0;
     while(1){
        i=0;
        flag=0;
        flagy=0;
        for(i=0;i<x;i++)
        {

            if(s[i]=='-')
                {
                    flag=1;
                    break;
                }
        }
        if(flag==0)
        {
            fout<<"Case #"<<t<<": "<<count<<endl;
            break;
        }
        flag=0;

        //for(i=0;i<x-1;i++){
        //    if(s[i]=='+')
        //        flagy=1;
        //}
        i=0;
        //fout<<"HI"<<endl;
        while(s[i]=='-'){
            i++;
        }
        while(s[i]=='+'){
            i++;
        }
        //fout<<i<<" "<<x-1<<endl;
        if(i==x)
            flagy=1;
        //fout<<"Bye"<<flagy<<endl;
        if(flagy==1&&s[x-1]=='+')
        {
                count++;
                fout<<"Case #"<<t<<": "<<count<<endl;
                break;
        }

        while(s[i]!='-'&&i!=x-1)
            i++;


        for(j=0;j<i;j++){
            if(s[j]=='+')
                s[j]='-';
            else
                s[j]='+';
        }
        count++;

      }
    }


  }

 return 0;
}
