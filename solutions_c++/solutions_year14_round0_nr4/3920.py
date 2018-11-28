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

int search(vd vec,double val)
{
    int low=0,high=vec.size()-1,mid;
    if(vec[0]>val)
        return 0;
    while(high>low+1)
    {
        mid=(low+high)/2;
        if(vec[mid]<=val)
            low=mid;
        else
            high=mid;
    }
    return high;
}

int count_war(vd vec1,vd vec2)
{
    int c=0,i;
    double a,b;
    int n=vec1.size();
    while(n)
    {
        a=vec1[n-1];
        if(a>=vec2[n-1])
        {
            ++c;
            vec1.erase(vec1.begin()+n-1);
            vec2.erase(vec2.begin()+0);
        }
        else
        {
            i = search(vec2,a);
            vec1.erase(vec1.begin()+n-1);
            vec2.erase(vec2.begin()+i);
        }
        --n;
    }
    return c;
}

int count_dec(vd vec1,vd vec2)
{
    int c=0,n=vec1.size();
    while(n)
    {
        if(vec1[0]>vec2[0])
        {
            ++c;
            vec1.erase(vec1.begin()+0);
            vec2.erase(vec2.begin()+0);
        }
        else
        {
            vec1.erase(vec1.begin()+0);
            vec2.erase(vec2.begin()+n-1);
        }
        --n;
    }
    return c;
}

int main(void)
{
    char buffer[100];
    int i,j;
    int T,N;
    FILE *fi,*fo;
    vd v1(1000,0.0);
    vd v2(1000,0.0);
    fi = fopen("D-small.in","r");
    fo = fopen("D-small.out","w");
    fscanf(fi,"%d",&T);
    fint(i,0,T)
    {
        fscanf(fi,"%d",&N);
        v1.resize(N,0.0);
        v2.resize(N,0.0);
        fint(j,0,N)
            fscanf(fi,"%lf",&v1[j]);
        fint(j,0,N)
            fscanf(fi,"%lf",&v2[j]);
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        sprintf(buffer,"Case #%d: %d %d\n",i+1,count_dec(v1,v2),count_war(v1,v2));
        fputs(buffer,fo);
        cout<<buffer<<"\n";
    }
    return 0;
}
