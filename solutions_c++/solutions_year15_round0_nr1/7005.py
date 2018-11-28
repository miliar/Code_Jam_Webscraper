#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main(void)
{
    FILE *fp1,*fp2;
    fp1=fopen("A-large.in","r");
    fp2=fopen("2nd.txt","w");
    int T,N,i,count1,a,case1=1;
    char sonveer[1001];
    int array1[1001];
    //cin>>T;
    fscanf(fp1,"%d",&T);
    while(T--)
    {
        count1=0;
        //cin>>N;
        //cin>>sonveer;
        fscanf(fp1,"%d%s",&N,sonveer);
        memset(array1,0,sizeof(array1));
        array1[0]=sonveer[0]-48;
        if(array1[0]==0&&N!=0)
            {
                count1++;
                array1[0]=1;
            }
        for(i=1;i<=N;i++)
        {
            a=sonveer[i]-48;
            if(a==0&&array1[i-1]==i)
            {count1++;array1[i]=array1[i-1]+1;}
            else
                array1[i]=array1[i-1]+a;
               // cout<<array1[i]<<"      "<<i<<"      "<<count1<<endl;
        }
        //cout<<count1<<endl;
    fprintf(fp2,"Case #%d: %d\n",case1,count1);case1++;
    }
    fclose(fp1);
    fclose(fp2);
    return 0;
}
