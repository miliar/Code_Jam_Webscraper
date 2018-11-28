#include <bits/stdc++.h>

using namespace std;

typedef long long lld;

#define MAX 100005

int main(){
    
    //freopen("input.txt","r",stdin);
    lld test,i,j,k,num[MAX],on,thre,fiv,sev,nin,temp;
    
    char str[MAX];
    
    scanf("%lld",&test);
    
    for(i=1;i<=test;i++){
        
        lld num[MAX]={0};
        
        scanf("%s",str);
        
        for(j=0;j<strlen(str);j++){
            
            temp=(int)str[j];
            num[temp]++;
        }
        
        on = num[79]-num[90]-num[85]-num[87];
        
        thre = num[72]-num[71];
        
        sev = num[83]-num[88];
        
        fiv = num[86]-sev;
        
        nin = num[73]-num[88]-num[71]-fiv;
        
        
        printf("Case #%lld: ",i);
        
        for(j=0;j<num[90];j++){
            
            printf("0");
        }
            
        for(j=0;j<on;j++){
            
            printf("1");
        }
        
        for(j=0;j<num[87];j++){
            
            printf("2");
        }
            
        for(j=0;j<thre;j++){
            
            printf("3");
        }
        
        for(j=0;j<num[85];j++){
            
            printf("4");
        }
            
        for(j=0;j<fiv;j++){
            
            printf("5");
        }
        
        for(j=0;j<num[88];j++){
            
            printf("6");
        }
        
        for(j=0;j<sev;j++){
            
            printf("7");
        }
        
        for(j=0;j<num[71];j++){
            
            printf("8");
        }
        
        for(j=0;j<nin;j++){
            
            printf("9");
        }
        
        printf("\n");
    }
    
	return 0;
}
