//
//  main.cpp
//  codejam2014_Problem A. Magic Trick
//
//  Created by kimtaeyang on 2014. 4. 12..
//  Copyright (c) 2014년 kimtaeyang. All rights reserved.
//

#include <stdio.h>

int T;
int r, a[5][5],check[17];

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int I, i, j, k;
    
    scanf("%d",&T);
    
    for(I=1;I<=T;I++){
        for(k=1;k<=16;k++) check[k]=0;
        for(k=1;k<=2;k++){
            scanf("%d",&r);
            for(i=1;i<=4;i++) for(j=1;j<=4;j++) scanf("%d",&a[i][j]);
            for(j=1;j<=4;j++) check[a[r][j]]++;
        }
        j=0;
        for(i=1;i<=16;i++) if(check[i]==2) j++, k=i;
        if(j==1) printf("Case #%d: %d\n",I,k);
        else if(j>=2) printf("Case #%d: Bad magician!\n",I);
        else printf("Case #%d: Volunteer cheated!\n",I);
    }
    
}

