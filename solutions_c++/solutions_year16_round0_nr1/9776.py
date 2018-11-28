#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
using namespace std;
int chk(int arr[])
{

    for(int i=0;i<10;i++)
    {
        if(arr[i]==0)
            return 0;
    }
    return 1;
}
int main()
{
    FILE *fp,*fp1;
    int t,n,c=0,num;
    char bf[255];
	fp=fopen("C:\\Users\\jai maa\\Downloads\\A-small-attempt2.in","r");
	fp1=fopen("outupt.txt","w");
    fgets(bf, 255,fp);
    sscanf(bf,"%d",&t);
    char str[255];
    while(t--)
    {
        char str1[1000]="Case #";
        char str2[]=": INSOMNIA\n";
        int arr[10]={0},coun=1;
        c++;
        //n=0;
        fgets(bf, 255,fp);
        sscanf(bf,"%d",&n);
        if(n==0)
        {
            sprintf(str,"%d",c);
            strcat(str1,str);
            strcat(str1,": INSOMNIA\n");
            fputs(str1,fp1);
        }

        else
        {
            num=n;
            while(num!=0)
            {
                arr[num%10]++;
                num=num/10;
            }
            while(chk(arr)==0)
            {
                coun++;
                num=coun*n;
                while(num!=0)
                {
                    arr[num%10]++;
                    num=num/10;
                }
            }
            if(chk(arr)==1)
            {
                sprintf(str,"%d",c);
                strcat(str1,str);
                strcat(str1,": ");
                sprintf(str,"%d",coun*n);
                strcat(str1,str);
                fputs(str1,fp1);
            }
        }
    }
    return 0;
}
