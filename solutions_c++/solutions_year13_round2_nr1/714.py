#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string.h>
using namespace std;

long long v[1001000];

main(){
    FILE *fout = fopen("out.txt","w");
    FILE *fin = fopen("in.txt","r");
    int te;
    scanf("%d",&te);
    
    for(int t=1;t<=te;t++){
        
        
        long long size,n;
        scanf("%lld%lld",&size,&n);
        
        for(int i=0;i<n;i++)
            scanf("%lld",v+i);
            
        sort(v,v+n);
        
        
        if(size == 1){
        fprintf(fout,"Case #%d: %lld\n",t,n);
         continue;   
        }
        
        long long resp = 99999999999999LL;
        long long coloca = 0;
        
        for(int i=0;i<n;i++){
            
        //    printf("i=%d coloca = %d\n",i,coloca);
            
            resp = min(resp,coloca + n - i);
            
            if(size > v[i]){
                size += v[i];
                continue;
                }
            
            
            while(size <= v[i]){
            

            
            
            coloca++;
            size = 2*size - 1;
            
        }
            size += v[i];
            
            }
        resp =  min(resp,coloca);
        
        fprintf(fout,"Case #%d: %lld\n",t,resp);
        
        
        
        
    }
    


}
