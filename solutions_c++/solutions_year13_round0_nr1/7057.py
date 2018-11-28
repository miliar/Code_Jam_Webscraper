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
#include<fstream>

using namespace std;

typedef unsigned long long ull;
typedef unsigned long ul;
typedef long long ll;
typedef long il;
typedef vector<long> vl;
typedef vector<long long> vll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<bool> vb;
typedef vector<unsigned int> input_type;

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



int main()
{
char temp[50],buffer[100];
int i,j,k;
int T;
FILE *fi,*fo;
fi = fopen("A-small.in","r");
fo = fopen("A-small.out","w");
fscanf(fi,"%d",&T);
vi countX,countO;
vb check;
bool check_complete;
bool check_change=false;
char c;
//int _i,_j;
fint(k,1,T+1)
{
    countX.resize(10,0);
    fint(j,0,10)
        countX[j]=0;
    countO.resize(10,0);
    fint(j,0,10)
        countO[j]=0;
    check.resize(10,true);
    fint(j,0,10)
        check[j]=true;
    check_complete=true;
    check_change=false;
    sprintf(temp,"Draw");
        fscanf(fi,"%c",&c);
    fint(i,0,4)
    {
        fint(j,0,4)
        {
            fscanf(fi,"%c",&c);
            if(c=='.')
            {
                check_complete=false;
                check[i]=false;
                check[4+j]=false;
                if(i==j)
                    check[8]=false;
                else if((i+j)==3)
                    check[9]=false;
            }
            else if(c=='O')
            {
                ++countO[i];
                ++countO[4+j];
                if(i==j)
                    ++countO[8];
                else if((i+j)==3)
                    ++countO[9];
            }
            else if(c=='X')
            {
                ++countX[i];
                ++countX[4+j];
                if(i==j)
                    ++countX[8];
                else if((i+j)==3)
                    ++countX[9];
            }
            else
            {
                if(c!='T')
                    cout<<"error";
            }
            cout<<c;
        }
        fscanf(fi,"%c",&c);
        cout<<"\n";
    }
    cout<<"\ncase "<<k<<"\n";
    fint(i,0,10)
    {
        if((!countO[i])&&(check[i]))
            {
                sprintf(temp,"X won");
                check_change=true;
            }
        else if((!countX[i])&&(check[i]))
            {
                sprintf(temp,"O won");
                check_change=true;
            }
            cout<<"O = "<<countO[i]<<"  "<<"X ="<<countX[i]<<"\n";
    }
    cout<<"\n\n";
    if((!check_change)&&(!check_complete))
        sprintf(temp,"Game has not completed");
    sprintf(buffer,"Case #%d: %s\n",k,temp);
    fputs(buffer,fo);
}
return 0;
}
//fscanf(fp,"%s",&str);//reads upto space
/*fgets(temp,10,fi); //reads whole line
T=atoi(temp);*/


