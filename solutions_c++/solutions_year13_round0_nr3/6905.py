#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

int main()
{

    long int min,t,count,max,j,x,i,num1,len,k;
    float num;
    char rev[10],rev1[10];
    fstream fp,fp1;
    fp.open("input.txt");
    fp1.open("output.txt");
    fp>>t;
    for(i=0;i<t;i++)
    {
            count=0;
            fp>>min;
            fp>>max;
            for(j=min;j<=max;j++)
            {
                //itoa(j,rev,10);//rev=itoa(j);
                snprintf(rev, 10, "%d", j);
                //strcpy(rev1,rev);
                //cout<<"rev is "<<rev<<endl;
                //strrev(rev1);
                //reverse(rev1.begin(),rev1.end());
                len=strlen(rev);
                k=0;
                //cout<<"len is "<<len<<endl;
                while(len>0)
                {
                    rev1[k]=rev[--len];
                    k++;
                }
                rev1[k]='\0';
               // cout<<"rev1 is "<<rev1<<endl;
                x=strcmp(rev,rev1);
                if(x==0)
                {
                    num=sqrt(j);
                    num1=sqrt(j);
                    if(num!=num1)
                    {
                        num1=12;
                    }
                    snprintf(rev, 10, "%d",num1);
                    //rev=itoa(j*j);

                    //strcpy(rev1,rev);
                    //strrev(rev1);
                    //reverse(rev1.begin(),rev1.end());
                 len=strlen(rev);
                 k=0;
                while(len>=0)
                {
                    rev1[k]=rev[--len];
                    k++;
                }
                rev1[k]='\0';
                //cout<<"rev1 inside is  ie sqrt is "<<rev1<<"rev normal is "<<rev<<endl;
                    x=strcmp(rev,rev1);
                    if(x==0)
                    {
                           //cout<<"Val "<<j<<" "<<sqrt(j)<<endl;
                            count++;
                    }
                }

            }
            fp1<<"Case #"<<i+1<<": "<<count<<endl;
    }
}
