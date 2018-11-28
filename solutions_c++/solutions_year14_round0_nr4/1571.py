#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
FILE *fin = fopen("input.txt","r");
FILE *fout = fopen("output.txt","w");
using namespace std;
void pro()
{
    int n;
    double ken[1000],naomi[1000];

    fscanf(fin,"%d",&n);
    for(int i=0;i<n;i++)
        fscanf(fin,"%lf",&naomi[i]);
    for(int i=0;i<n;i++)
        fscanf(fin,"%lf",&ken[i]);
    sort(ken,ken+n);
    sort(naomi,naomi+n);
    int index=n-1,cnt_n=0;
    for(int j=n-1;j>=0;j--)
    {
        if(ken[j]<naomi[index])
        {
            cnt_n++;
            index--;
        }
    }
    index=n-1;
    int cnt_k=0;
    for(int j=n-1;j>=0;j--)
    {
        if(naomi[j]<ken[index])
        {
            cnt_k++;
            index--;
        }
    }
    fprintf(fout,"%d %d\n",cnt_n,n-cnt_k);
}
int main()
{
    int n;
    fscanf(fin,"%d",&n);
    for(int i=0;i<n;i++)
    {
        fprintf(fout,"Case #%d: ",i+1);
        pro();
    }
    return 0;
}
