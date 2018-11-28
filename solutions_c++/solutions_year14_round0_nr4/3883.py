#include <stdio.h>
#include <iostream>
#include <cstring>
using namespace std;
void bsort(double array[]);
int decitful_war();
int get_biggest(double array[],bool taken[]);
int get_smallest(double array[],bool taken[]);
int war();
int first_biggest(double array[],bool taken[],double value);

bool taken_a[1200];
bool taken_b[1200];

double a[1200];
double b[1200];
int m;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("c.out","w",stdout);

    int cases,p=1;
    scanf("%d",&cases);
    while(cases--)
    {
        scanf("%d",&m);

        for(int i=0; i<m; i++)
            cin>>a[i];

        for(int i=0; i<m; i++)
            cin>>b[i];

        bsort(a);
        bsort(b);

        printf("Case #%d: ",p);
        printf("%d %d\n",decitful_war(),war());

        p++;
    }
    return 0;
}


int war()
{
    memset(taken_a, true, sizeof(taken_a));
    memset(taken_b, true, sizeof(taken_b));

    int ret=0;
    int j=m-1;

    int naomi,ken;
    double x,y;

    for(int i=0; i<m; i++)
    {
        ken=first_biggest (b,taken_b,a[i]);
        if(ken!=-1)
        {
            taken_b[ken]=false;
        }
        else
        {
            ken=get_smallest(b,taken_b);
            taken_b[ken]=false;
            ret++;
        }
        taken_a[i]=false;
    }
    return ret;
}

int first_biggest(double array[],bool taken[],double value)
{
    for(int i=0; i<m; i++)
        if(array[i]>value && taken[i])
            return i;
    return -1;
}

int decitful_war()
{
    memset(taken_a, true, sizeof(taken_a));
    memset(taken_b, true, sizeof(taken_b));

    int ret=0;
    int j=m-1;

    int naomi,ken;
    double x,y;

    for(int i=0; i<m; i++)
    {
        x=b[j];
        naomi=get_biggest(a,taken_a);

        if(a[naomi]>b[j])
        {
            ret++;
            taken_a[naomi]=false;
        }
        else
        {
            naomi=get_smallest(a,taken_a);
            taken_a[naomi]=false;
        }
        taken_b[j]=false;
        j--;
    }
    return ret;
}

int get_smallest(double array[],bool taken[])
{
    for(int i=0; i<m; i++)
        if(taken[i])
            return i;
    return -1;
}

int get_biggest(double array[],bool taken[])
{
    for(int i=m-1; i>=0; i--)
        if(taken[i])
            return i;
    return -1;
}

void bsort(double array[])
{
    double swap;
    bool flag;
    for(int i=0; i<m-1; i++)
    {
        flag=true;
        for(int j=0; j<m-1; j++)
            if(array[j]>array[j+1])
            {
                swap=array[j];
                array[j]=array[j+1];
                array[j+1]=swap;
                flag=false;
            }
        if(flag)
            return;
    }
    return ;
}
