#include<stdio.h>
#include<stdlib.h>
#include<string.h>

FILE* fi;
FILE* fo;

int main(int argc,char* argv[]){
    
    
    fi=fopen(argv[1],"r");
    fo=fopen(argv[2],"w");
    
    int t;
    int cnt=0;
    char arr[105];
    
    fscanf(fi,"%d",&t);
    
    for(int i=1;i<=t;i++){
        
        cnt=0;
        for(int z=0;z<105;z++) arr[z]=0;
        
        fscanf(fi,"%s",arr);
        
        arr[(int)strlen(arr)]='+';
        
        for(int j=1;j<strlen(arr);j++){
            
            if(arr[j]!=arr[j-1]) cnt++;
        }
        
        
        fprintf(fo,"Case #%d: %d\n",i,cnt);
        
    }
    
    fclose(fi);
    fclose(fo);
}