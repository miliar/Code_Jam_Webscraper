//
//  main.cpp
//  codejam
//
//  Created by cloudzfy on 5/4/13.
//  Copyright (c) 2013 cloudzfy. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int mote[100];
int main()
{
    freopen("A-small-attempt1.in.txt","r",stdin);
	freopen("A-small-attempt1.out.txt","w",stdout);
    int T,A,N;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d%d",&A,&N);
        for(int i=0;i<N;i++)
        {
            scanf("%d",&mote[i]);
        }
        if(A==1)
        {
            printf("Case #%d: %d\n",t,N);
            continue;
        }
        sort(mote,mote+N);
        int tmp=A;
        int result=0;
        int x;
        for(int i=0;i<N;i++)
        {
            x=0;
            while(tmp<=mote[i])
            {
                tmp+=tmp-1;
                x++;
            }
            tmp+=mote[i];
            if(x>=N-i)
            {
                result+=N-i;
                break;
            }
            else
            {
                result+=x;
            }
        }
        printf("Case #%d: %d\n",t,result);
        
    }
    return 0;
}

