#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main(){
    int T,it;
    int R,C,W;
    int min,min1;
	
    FILE *in,*out;
    in=fopen("A-large.in","r");
    out=fopen("A-large.out","w");
    
    fscanf(in,"%d",&T);
    for(it=1;it<=T;it++){
        fscanf(in,"%d %d %d",&R,&C,&W);
        min1=C/W;
		min=min1*R+W-1;
		if(C>min1*W){
            min++;             
        }
		
		
        fprintf(out,"Case #%d: %d\n",it,min);
    }
    fclose(in);
    fclose(out);
    
    //system("pause");
    return 1;
}
