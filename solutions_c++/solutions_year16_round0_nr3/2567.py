#include <bits/stdc++.h>
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <iterator>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <cmath>
#include <iomanip>
#include <string>
#include <sstream>
#include <cstring>
bool prime( long long int );
#define FOR(i,N) for(int i=0;i<(N);i++)
std::vector<long int> vec;
long long  int ja=0,jja,ca1=0,ca0=0;
int casa=1;
std::string sa;
std::string::size_type sza = 0;
using namespace std;
FILE *f,*f1;
void printvec(std::string , vector<long int> v);
bool cka=false;
void printall(char arra[], char tempa[], int ia, int ka, int na)
{
    if(ja<jja)
    {
        sa="";
        if(ia == ka)
        {
            FOR(ma, ka)
            {
                sa=sa+tempa[ma];
            }
            long int la=sa.length();
            if(sa[0]=='1'&& sa[la-1]=='1')
            {
                std::string str = sa;
                long long int iina = std::stoull (str,&sza,10);
                for(ia=2;ia<=10;ia++)
                {
                    cka=false;
                    long long int ulla = std::stoull (str,&sza,ia);
                    cka=prime(ulla);
                    if(cka==false)
                    {
                        sa="";
                        vec.clear();
                        break;
                    }
                }
                if(cka==true)
                    printvec(sa,vec);
            }
            return;
        }
        FOR(pa, na)
        {
            tempa[ia] = arra[pa];
            printall(arra, tempa, ia+1, ka, na);
        }
    }
}
void solve(char arra[], int na, int ka)
{
     char tempa[ka];
     printall(arra, tempa, 0, ka, na);
}
bool prime( long long int na1)
{
    long int aa;
    long long int sqa=sqrt(na1);
    for(aa=2;aa<=sqa;aa++)
    {
        if(na1%aa==0)
        {
            cka=true;
            vec.push_back(aa);
            break;
        }
    }
    if(cka==false)
    {
        sa="";
        vec.clear();

    }
    return cka;
}
void printvec(std::string st,vector<long int> va)
{
    long long  int lena=va.size();
    long long int iia = std::stoull (st,&sza,10);
    long int qa;
    fprintf(f1,"%lld ",iia);
    for( qa=0;qa<lena;qa++)
    {
        fprintf(f1,"%ld ",va[qa]);
    }
    fprintf(f1,"\n");
    sa="";
    ja++;
    vec.clear();
}
int main()
{

    int ma,ta;
    char arra[] = {'1', '0'};
    int na = sizeof(arra)/sizeof(arra[0]);
    f = fopen("i3.txt", "r");
    f1 = fopen("o3.txt", "w");
    fscanf(f, "%d",&ta);
    fscanf(f, "%d%d",&ma,&jja);
    fprintf(f1,"Case #%d:\n",casa);
    solve(arra, na, ma);
    return 0;
}
