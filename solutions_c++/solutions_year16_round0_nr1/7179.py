#include<stdio.h>
#include<stdlib.h>

FILE* fi;
FILE* fo;

int main(int argc,char* argv[]){
    
    fi=fopen(argv[1],"r");
    fo=fopen(argv[2],"w");
    
    int t;
    int arr[10];
    int cnt=0;
    long long int mul=1;
    long long int n;
    fscanf(fi,"%d",&t);
    
    for(int i=1;i<=t;i++){
        
        for(int j=0;j<10;j++){
            
            arr[j]=0;
        }
        cnt=0;
        mul=1;
        
        fscanf(fi,"%lld",&n);
        
        if(n==0){
            fprintf(fo,"Case #%d: INSOMNIA\n",i);
            continue;
        }
        
        while(cnt<10){
            
            long long int cal=n*mul;
            long long int tmp=cal;
            
            while(tmp!=0){
                
                //printf("%lld %lld %lld\n",tmp,tmp%10,tmp/10);
                
                if(arr[tmp%10]==0){
                    cnt++;
                    arr[tmp%10]=1;
                }
                
                tmp=tmp/10;
            }
            
            if(cnt==10){
                
                fprintf(fo,"Case #%d: %lld\n",i,cal);
                break;
            }
            
            mul++;
        }
        
    }
    
    fclose(fi);
    fclose(fo);
}
