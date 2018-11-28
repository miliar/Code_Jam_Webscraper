/*
Name:: Vivek Kumar Yadav
Language:: C++
Handle:: vivekjnv93
*/
#include<iostream>
#include<cstdio>
#include<vector>
#include<cmath>
#include<map>
#include<set>
#include<list>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;

#define fori(i,n) for(i=0;i<n;++i)
#define forn(i,n) for(i=n-1;i>=0;--i)
#define nil NULL
#define itr iterator
#define MAX(a,  b) ((a) > (b) ? (a) : (b))
#define MIN(a,  b) ((a) < (b) ? (a) : (b))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define SQ(X) ( (X) * (X) )
//#define getchar getchar_unlocked

typedef long int li;
typedef long long int lli;
typedef long double ld;

/*------------------------------------------------------------------------------
++++++++++++++++++++++++++++++++Source Code+++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------*/
//Functions and Global variables
//main
int A[5][5],B[5][5];

int main()
{
    int t,a,i,j,b,flag=0,val,k;
    FILE *fi= fopen("in.txt","r");
    FILE *fo= fopen("out.txt","w");
    fscanf(fi,"%d",&t);
    k=0;
    while(t--)
    {
        k++;
        flag=0;
        fscanf(fi,"%d",&a);
        a--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fscanf(fi,"%d",&A[i][j]);
            }
        }
        fscanf(fi,"%d",&b);
        b--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fscanf(fi,"%d",&B[i][j]);
            }
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(A[a][i]==B[b][j] && flag==0)
                {
                    flag=1;
                    val = A[a][i];
                }
                else if(A[a][i]==B[b][j] && flag==1)
                {
                    flag = 2;
                }
                else
                    continue;
            }
        }
        if(flag==1)
            fprintf(fo,"Case #%d: %d\n",k,val);
        else if(flag==2)
        {
            fprintf(fo,"Case #%d: Bad magician!\n",k);
        }
        else
            fprintf(fo,"Case #%d: Volunteer cheated!\n",k);
    }
    return 0;




}
