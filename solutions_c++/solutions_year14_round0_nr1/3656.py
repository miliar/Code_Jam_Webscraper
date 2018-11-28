//
//  main.cpp
//  google code jam
//
//  Created by Tapan on 12/04/14.
//  Copyright (c) 2014 Tapan. All rights reserved.
//

#include <stdio.h>
int main(int argc,const char * argv[])
{
    int t;int f=1;
    FILE *p,*q;
    p=fopen("A-small-attempt3.in","r");
    q=fopen("output.txt","w");
    fscanf(p,"%d",&t);
    while(t--){
        int k,i,j,m=2,c=0,n;int a[4][4];int b[17]={0};
        while(m--){
        fscanf(p,"%d",&k);
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                fscanf(p,"%d",&a[i][j]);
                if((i+1)==k){
                    b[a[i][j]]++;
                }
            }
            }
        }
        for(i=1;i<=16;i++){
            if(b[i]==2){
                c++;n=i;
            }
        }
        printf("Case #%d: ",f);
        f++;
        if(c==0)printf("Volunteer cheated!\n");
        if(c==1)printf("%d\n",n);
        if(c>=2)printf("Bad magician!\n");
    }
    fclose(p);fclose(q);
    return 0;
}

