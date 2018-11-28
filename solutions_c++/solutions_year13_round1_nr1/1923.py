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


string convertInt(long long number)
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


int main()
{
char temp[10],buffer[100];
int i,j,k;
int T;
FILE *fi,*fo;
fi = fopen("A-small.in","r");
fo = fopen("A-small.out","w");
fscanf(fi,"%d",&T);
ll r,t,a;
ll res=0;
fint(i,0,T)
{
    fscanf(fi,"%lld%lld",&r,&t);
    a=2*r-1;
/*    res=-1;
    while(t>=0)
    {
        t-=a;
        a+=4;
        ++res;
    }
*/    res = (sqrt(a*a+8*t)-a)/4;
//    res = (2*t)/(a+sqrt(a*a+8*t));
    sprintf(buffer,"Case #%d: %s\n",i+1,convertInt(res).c_str());
    fputs(buffer,fo);
    cout<<res<<"\n";
}
return 0;
}
//fscanf(fp,"%s",&str);//reads upto space
/*fgets(temp,10,fi); //reads whole line
T=atoi(temp);*/

