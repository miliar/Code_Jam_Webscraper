#include<stdio.h>
int main(){
    FILE *input,*output;
    int t,n,num,tmp,i,j,new_num,hash[10];
    input=fopen("input.in","r");
    if(!input){
        printf("Invalid Input");
        return 0;
    }
    output=fopen("output.txt","w");
    fscanf(input,"%d",&t);
    for(i=1;i<=t;i++){
        for(j=0;j<10;hash[j++]=0);
        fscanf(input,"%d",&num);
        if(num==0)  fprintf(output,"Case #%d: INSOMNIA\n",i);
        else{
            j=1;
            while(1){
                new_num=j*num;
                tmp=new_num;
                while(tmp){
                    hash[tmp%10]=1;
                    tmp/=10;
                }
                for(tmp=0;tmp<10 && hash[tmp];tmp++);
                if(tmp==10) {
                    fprintf(output,"Case #%d: %d\n",i,new_num);
                    break;
                }
                j++;
            }
        }
    }
    return 0;
}
