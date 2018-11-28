#include<stdio.h>
#include<stdlib.h>
bool notinken(float a,float b[],size_t l)
{
    for(int i=0;i<l;i++)
    {
        if(b[i]==a)
            return false;
    }
    return true;
}
int larsmall(float a[], float b[], size_t l, bool t)
{
    int ret, i;
    if (t==false)
        ret=larsmall(a,b,l,true);
    else
        ret=0;
    for(i=0;i<l;i++)
    {
        if(t==true){
        if(a[ret]<a[i])
            ret=i;}
        else
        {
            if(a[ret]>a[i]&& a[i]!=0&&notinken(a[i],b,l))
                ret=i;
        }
    }
    return ret;
}
int findbig(float a[], size_t l, float val)
{
    int i;
    for(i=l-1;i>=0;i--)
    {
        if(a[i]> val)
            return i;
    }
    return -1;
}
int floatcomp(const void* elem1, const void* elem2)
{
    if(*(const float*)elem1 < *(const float*)elem2)
        return 1;
    if(*(const float*)elem1 > *(const float*)elem2)
        return -1;
    if(*(const float*)elem1 == *(const float*)elem2)
        return 0;
}
int main()
{
    FILE *fr, *fw;
    fr=fopen("D-large.in","r");
    fw=fopen("oup3.txt","w");
    int i,j,t,n,sum,sum1,nm;
    fscanf(fr,"%d",&t);
    for(i=0;i<t;i++)
    {
        sum=0;
        fscanf(fr,"%d",&n);
        float nao[2][n], ken[2][n];
        for(j=0;j<n;j++)
        {
            fscanf(fr,"%f",&nao[0][j]);
            nao[1][j]=nao[0][j];
        }
        for(j=0;j<n;j++)
        {
            fscanf(fr,"%f",&ken[0][j]);
            ken[1][j]=ken[0][j];
        }
        qsort(ken[0],n,sizeof(float),floatcomp);
        for(j=0;j<n;j++)
        {
            nm=larsmall(nao[0],ken[0],n,true);
            if(nao[0][nm]>ken[0][j])
            {
                sum=sum+1;
            }
            else
            {
                nm=larsmall(nao[0],ken[0],n,false);
            }
            nao[0][nm]=0.0f;
            ken[0][j]=0.0f;
        }
        qsort(nao[1],n,sizeof(float),floatcomp);
        qsort(ken[1],n,sizeof(float),floatcomp);
        sum1=0;
        for(j=n-1;j>=0;j--)
        {
            nm=findbig(ken[1],n,nao[1][j]);
            if(nm==-1)
            {
                sum1=sum1+1;
            }
            else
            {
                ken[1][nm]=0;
            }
        }
        fprintf(fw,"Case #%d: %d %d",i+1,sum,sum1);
        if(i!=t-1)
            fprintf(fw,"\n");
    }
    fclose(fr);
    fclose(fw);
}
