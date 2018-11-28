#include <fstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("output.out");

long long t,n,j,k,i,a[100];
bool u[10];
string s1,s;

string convertint(int number)
{
    if (number == 0)
        return "0";
    string temp="";
    string returnvalue="";
    while (number>0)
    {
        temp+=number%10+48;
        number/=10;
    }
    for (int i=0;i<temp.length();i++)
        returnvalue+=temp[temp.length()-i-1];
    return returnvalue;
}

bool check(){
    for (int i=0;i<10;i++) if (u[i]==0){
        return 0;
    }
    return 1;

}

int main()
{
    fin >>t;
    for(i=1;i<=t;i++){

        fin >>n;
        if (n==0) fout <<"Case #"<<i<<": INSOMNIA"<<endl;
        else {
            for(j=1;j<=1000;j++){
                k=j*n;
                s="";
                s=convertint(k);
                int found;
                found=s.find('0');
                if (found!=string::npos) u[0]=1;
                found=s.find('1');
                if (found!=string::npos) u[1]=1;
                found=s.find('2');
                if (found!=string::npos) u[2]=1;
                found=s.find('3');
                if (found!=string::npos) u[3]=1;
                found=s.find('4');
                if (found!=string::npos) u[4]=1;
                found=s.find('5');
                if (found!=string::npos) u[5]=1;
                found=s.find('6');
                if (found!=string::npos) u[6]=1;
                found=s.find('7');
                if (found!=string::npos) u[7]=1;
                found=s.find('8');
                if (found!=string::npos) u[8]=1;
                found=s.find('9');
                if (found!=string::npos) u[9]=1;
                if (check()){
                  fout <<"Case #"<<i<<": "<<k<<endl;
                  for(int x=0;x<10;x++) u[x]=0;
                  break;
                }



            }

        }

    }

    return 0;
}
