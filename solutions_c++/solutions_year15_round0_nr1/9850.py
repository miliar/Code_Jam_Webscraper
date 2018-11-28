#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
    FILE *f1,*f2;
    int test;
    char ch;
    char str[1001];
    f1=fopen("/home/archit/Documents/COdejam/Qualification/Standing ovation/A-small-attempt1.in","r");
    f2=fopen("/home/archit/Documents/COdejam/Qualification/Standing ovation/2.txt","w");
    fscanf(f1,"%d",&test);
    ch=fgetc(f1);
    for(int m=1;m<=test;m++){
        //cout<<"A";
        int i=0,N=0;
        fscanf(f1,"%d",&N);
        ch=fgetc(f1);
        ch=fgetc(f1);
        while(ch!='\n'&&ch!='\0'){
            //cout<<"B";
            str[i]=ch;
            i++;
            ch=fgetc(f1);
        }
        str[i]='\0';
        int sum=0,no_of_friends=0;
        for(int i=0;i<=N;i++){
            if((str[i]-48)==0)
                continue;
            if(sum>=i){
                sum+=str[i]-48;
                //cout<<"a"<<i<<"s"<<sum<<endl;
            }
            else{
                no_of_friends+=(i-sum);
                sum+=no_of_friends+str[i]-48;
                //cout<<"b"<<i<<"s"<<sum<<"f"<<no_of_friends<<endl;
            }
        }
        fprintf(f2,"Case #%d: %d\n",m,no_of_friends);

    }
    fclose(f1);
    fclose(f2);
    return 0;
}
