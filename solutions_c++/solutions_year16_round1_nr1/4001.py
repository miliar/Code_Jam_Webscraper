#include<stdio.h>
#include<iostream>
#include<stdlib.h>
int main(int argc,char **argv)
{
    FILE *fin=fopen(argv[1],"r");
    if(fin!=NULL)
    {
        int i,n;
        fscanf(fin,"%d",&n);
        fgetc(fin);
        char temp;
        int count=0;
        for(i=0;i<n;i++,count=0)
        {
            std::string s1="";
            temp=fgetc(fin);
            s1+=temp;
            while(s1!=""){
                temp=fgetc(fin);
                if(temp=='\n'||temp==EOF||count>=1000) break;
                if(temp>=s1[0])s1=temp+s1;
                else
                    s1+=temp;
            }
            printf("Case #%d: %s\n",i+1,s1.c_str());
        }
    }
    fclose(fin);
    return 0;
}
