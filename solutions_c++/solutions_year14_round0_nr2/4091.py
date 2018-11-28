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

bool myfunction (int i,int j) { return (i>j); }

int main(void)
{
    char buffer[100];
    int i;
    int T;
    bool temp;
    double C,F,X,t1,t2,t=0.0,n=2;
    FILE *fi,*fo;
    fi = fopen("B-small.in","r");
    fo = fopen("B-small.out","w");
    fscanf(fi,"%d",&T);
    fint(i,0,T)
    {
        fscanf(fi,"%lf",&C);
        fscanf(fi,"%lf",&F);
        fscanf(fi,"%lf",&X);
        if(X<C)
        {
            sprintf(buffer,"Case #%d: %.7f\n",i+1,(X/2.0));
            fputs(buffer,fo);
            cout<<buffer<<"\n";
        }
        else
        {
        t=C/2;
        n=2.0;
        temp=true;
        while(temp)
        {
            t1=(X-C)/n;
            t2=X/(n+F);
            if(t1<=t2)
            {
                t+=t1;
                temp=false;
            }
            else
            {
                t+=C/(n+F);
                n+=F;
            }
        }
        sprintf(buffer,"Case #%d: %.7f\n",i+1,t);
        fputs(buffer,fo);
        cout<<buffer<<"\n";        }
    }
}
