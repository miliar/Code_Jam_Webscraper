#include <cstdio>

using namespace std;

int main(){
    int i,j,k,l,m,n,o,p,r,s,t,h,okcelk;
    int pole[100][100];
    //int mam[100][100];
    int rok[100];
    int sok[100];
    
    scanf("%d",&n);
    
    for(l=0;l<n;l++){
        scanf("%d",&r);
        scanf("%d",&s);
        for(i=0;i<r;i++){
            for(j=0;j<s;j++){
                scanf("%d",&p);
                //mam[i][j]=0;
                pole[i][j]=p;
            }
        }
        /*for(i=0;i<r;i++){
            for(j=0;j<s;j++){
                printf("%d ",pole[i][j]);
            }
            putchar('\n');
        }*/
        
        okcelk = 1;
        
        for(h=0;h<110;h++){
            for(i=0;i<r;i++){
                rok[i]=1000;
            }
            for(i=0;i<s;i++){
                sok[i]=1000;
            }
            for(i=0;i<r;i++){
                k=0;
                m=0;
                for(j=0;j<s;j++){
                    if(pole[i][j]==h){
                        k++;
                        m++;
                    }
                    if(pole[i][j]<h){
                        m++;
                    }
                }
                //printf("i: %d rok[i]: %d\n",i,rok[i]);
                if((k>0)&&(m<s)){
                    //printf("pokazene na riadku: %d h: %d k: %d m: %d s: %d\n",i,h,k,m,s);
                    rok[i]=0;
                }else{
                    //printf("riadok: %d je ok\n",i);
                    rok[i]=1;
                }
                //printf("i: %d rok[i]: %d\n",i,rok[i]);
            }
            
            
            for(j=0;j<s;j++){
                k=0;
                m=0;
                for(i=0;i<r;i++){
                    if(pole[i][j]==h){
                        k++;
                        m++;
                    }
                    if(pole[i][j]<h){
                        m++;
                    }
                }
                if((k>0)&&(m<r)){
                    //printf("pokazene na stlpci: %d h: %d k: %d m: %d r: %d\n",j,h,k,m,r);
                    sok[j]=0;
                }else{
                    //printf("stlpec: %d je ok\n",j);
                    sok[j]=1;
                }
            }
            
            /*printf("height: %d\n",h);
            printf("riadky:");
            for(i=0;i<r;i++){
                printf(" %d",rok[i]);
            }
            putchar('\n');
            
            printf("stlpce:");
            for(i=0;i<s;i++){
                printf(" %d",sok[i]);
            }
            putchar('\n');*/
            
            for(i=0;i<r;i++){
                for(j=0;j<s;j++){
                    if((pole[i][j]==h)&&(rok[i]==0)&&(sok[j]==0)){
                        okcelk=0;
                        //printf("vyska: %d riadok: %d stlpec: %d nefunguje\n",h,i,j);
                    }
                }
            }
            
            if(okcelk==0){
                break;
            }
        }
        
        if(okcelk){
            printf("Case #%d: YES\n",l+1);
        }else{
            printf("Case #%d: NO\n",l+1);
        }
    }
    
    return 0;
}
