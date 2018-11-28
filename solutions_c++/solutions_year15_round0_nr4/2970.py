#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main(){
    int T,it;
    int X,R,C;
    int r;
    
    FILE *in,*out;
    in=fopen("D-small-attempt0.in","r");
    out=fopen("D-small-attempt0.out","w");
    
    fscanf(in,"%d",&T);
    for(it=1;it<=T;it++){
        fscanf(in,"%d %d %d",&X,&R,&C);
        r=0;
        
        //if(X==1) r=0;
        if(X==2){
             if((R*C)%2==1){
                 r=1;           
             }
             //else r=0;
        }
        if(X==3){
             if(R==1||C==1){
                 r=1;               
             }
             else{
                 if(R==2&&C==2) r=1;
                 if(R==2&&C==3) r=0;
                 if(R==2&&C==4) r=1;
                 
                 if(R==3&&C==2) r=0;
                 if(R==3&&C==3) r=0;
                 if(R==3&&C==4) r=0;
                 
                 if(R==4&&C==2) r=1;
                 if(R==4&&C==3) r=0;
                 if(R==4&&C==4) r=1; 
             }
        }
        if(X==4){
            if(R==1||C==1){
                 r=1;               
            }
            else{
                 if(R==2&&C==2) r=1;
                 if(R==2&&C==3) r=1;
                 if(R==2&&C==4) r=1;
                 
                 if(R==3&&C==2) r=1;
                 if(R==3&&C==3) r=1;
                 if(R==3&&C==4) r=0;
                 
                 if(R==4&&C==2) r=1;
                 if(R==4&&C==3) r=0;
                 if(R==4&&C==4) r=0;     
            }
        }
		
		
        fprintf(out,"Case #%d: ",it);
        if(r==1){
            fprintf(out,"RICHARD\n");        
        }
        else{
            fprintf(out,"GABRIEL\n");        
        }
    }
    fclose(in);
    fclose(out);
    
    //system("pause");
    return 1;
}
