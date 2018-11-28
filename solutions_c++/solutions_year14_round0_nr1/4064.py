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
    char temp[10],buffer[100];
    int i,j,k,t;
    int T,r;
    vb b1(16,false);
    vb b2(16,false);
    FILE *fi,*fo;
    fi = fopen("A-small.in","r");
    fo = fopen("A-small.out","w");
    fscanf(fi,"%d",&T);
    fint(k,0,T)
    {
        fint(i,0,16)
        {
            b1[i]=false;
            b2[i]=false;
        }
        fscanf(fi,"%d",&r);
        fint(i,0,4)
        {
            --r;
            fint(j,0,4)
            {
                fscanf(fi,"%d",&t);
                if(!r)
                b1[t-1]=true;
            }
        }

        fscanf(fi,"%d",&r);
        fint(i,0,4)
        {
            --r;
            fint(j,0,4)
            {
                fscanf(fi,"%d",&t);
                if(!r)
                b2[t-1]=true;
            }
        }

        t=0;
        fint(i,0,16)
        {
            if(b1[i]&&b2[i])
            {
                if(!t)
                    t=i+1;
                else
                    t=-1;
            }
        }

        if(t>0)
        {
            sprintf(buffer,"Case #%d: %d\n",k+1,t);
            fputs(buffer,fo);
            cout<<buffer<<"\n";
        }
        else if(t==-1)
        {
            sprintf(buffer,"Case #%d: Bad magician!\n",k+1);
            fputs(buffer,fo);
            cout<<buffer<<"\n";
        }
        else if(!t)
        {
            sprintf(buffer,"Case #%d: Volunteer cheated!\n",k+1);
            fputs(buffer,fo);
            cout<<buffer<<"\n";
        }
    }
}
