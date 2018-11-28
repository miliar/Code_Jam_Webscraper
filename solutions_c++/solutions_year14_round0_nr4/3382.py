#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>


#define MAXN 1005
double Naomi[MAXN], Ken[MAXN];
int visit[MAXN];

int partition(double a[],int low,int high)
{
    double pivotkey;
    pivotkey =a[low];
    while(low<high)
    {
        while(low<high&&a[high]>pivotkey)high--;//对end从小到大排序 
        a[low]=a[high];
        while(low<high&&a[low]<pivotkey)low++;
        a[high]=a[low];          
    }
    a[low]=pivotkey;
    return low;
}

void qqsort(double a[],int low,int high)
{
     int pivotloc;
     if(low<high)
     {
         pivotloc=partition(a,low,high);
         qqsort(a,low,pivotloc-1);
         qqsort(a,pivotloc+1,high);        
     }   
}
int main(void)
{
    int T, Case, i, j;
    int N;
    int normal, abnormal;
    
    FILE *fp1,*fp2;
    if((fp1=fopen("D-large.in","r"))==NULL)exit(0);
    if((fp2=fopen("D-large.out","w"))==NULL)exit(0);
    
    fscanf(fp1,"%d", &T);
    
    Case = 1;
    while(Case <= T)
    {
        fscanf(fp1,"%d", &N);
        for(i = 0; i < N; i++)
        {
            fscanf(fp1,"%lf", &Naomi[i]);
        }
        for(i = 0; i < N; i++)
        {
            fscanf(fp1,"%lf", &Ken[i]);
        }
        qqsort(Naomi, 0, N - 1);
        qqsort(Ken, 0, N - 1);
        
        abnormal = normal = 0;
        /*
        for(i = 0, j = N - 1; i < N, j >=0; i++, j--)
        {
            if(Naomi[i] < Ken[j])abnormal++;
            else
            {
                break;
            }
        }
        */
        memset(visit, 0, sizeof(visit));
        for(i = N - 1; i >= 0; i--)
        {
            for(j = N - 1; j >= 0; j--)
            {
                if(!visit[j] && (Naomi[i] > Ken[j]))
                {
                    abnormal++;
                    visit[j] = 1;
                    break;
                }
            }
        }
        
        memset(visit, 0, sizeof(visit));
        for(i = 0; i < N; i++)
        {
            for(j = 0; j < N; j++)
            {
                if(!visit[j] && (Naomi[i] < Ken[j]))
                {
                    normal++;
                    visit[j] = 1;
                    break;
                }
            }
        }
        
        fprintf(fp2,"Case #%d: %d %d\n", Case, abnormal, N - normal);
        Case++;
    }
    return 0;
}
