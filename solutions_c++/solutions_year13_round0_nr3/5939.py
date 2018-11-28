#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<vector>
#include<string>
#include<string.h>
#include<algorithm>
#include<cassert>
#include<map>
#include<set>
#include<sstream>
#include<cmath>

using namespace std;

typedef unsigned long long ull;
typedef unsigned long ul;
typedef long long ll;
typedef long il;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<unsigned int> vui;

#define fint(i,a,b) for(i=a;i<b;++i)
#define f_int(i,a,b,c) for(i=a;i<b;i+=c)
#define fstr(i,str) for(i=0;str[i]!='\0';++i)
#define fvec(i,vec) for(i=vec.begin();i!=vec.end();++i)

string convertInt(int number)
{
   std::stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

string convertInt(char number[10])
{
   std::stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

bool check_palindrom(int num)
{
    string s = convertInt(num);
    int i;
    int n=s.size();
    fint(i,0,n/2)
    {
        if(s[i]!=s[n-1-i])
            return false;
    }
    cout<<"\n"<<num<<"is seleected\n";
    return true;
}

double FnS_R[]={1.0,2.0,3.0,11.0,22.0,101.0,111.0,121.0};
int size=8;
int main()
{
char buffer[50];
string temp;

int i,j,k;
int T;
FILE *fi,*fo;
fi = fopen("C-small.in","r");
fo = fopen("C-small.out","w");
fscanf(fi,"%d",&T);
int A,B;
double rA,rB;
fint(i,0,T)
{
    fscanf(fi,"%d%d",&A,&B);
    rA = sqrt(A);
    rB = sqrt(B);
 //   cout<<"\n"<<rA<<" "<<rB<<"\n";
    for(j=0;((j<size)&&(FnS_R[j]<rA));++j);
    for(k=7;((k>=0)&&(FnS_R[k]>rB));--k);
    sprintf(buffer,"Case #%d: %d\n",i+1,k-j+1);
    fputs(buffer,fo);
   // cout<<"\n"<<k<<" "<<j<<"\n";
}
return 0;
}
//fscanf(fp,"%s",&str);//reads upto space
/*fgets(temp,10,fi); //reads whole line
T=atoi(temp);*/

