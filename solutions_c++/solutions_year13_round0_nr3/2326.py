#include <stdio.h>
#include <stdlib.h>
#define MAX 10000000

struct node {
    long long int ori;
    long long int sq;
    struct node *next;
};
typedef struct node* Node;

int isCycle(long long int x)
{
    int s[15];
    int i = 0, leng = 0, mid, ret;
    while( x > 0 ) {
        s[i] = x % 10;
        x = (x - s[i]) / 10;
        i++; leng++;
    }
    if( leng == 1 ) return 1;

    if( leng & 0x1 )
        mid = (leng >> 1) + 1;
    else
        mid = leng >> 1;

    i = 0;
    ret = 1;
    leng--;
    while( i <= mid ) {
        if( s[i] != s[leng-i] )
            ret = 0;
        i++;
    }
    return ret;
}

int main()
{
    int i,T;
    long long int A,B,j,num,sq;
    //int table[MAX+1] = {0};
    //long long int sq[MAX+1];
    FILE* iptr;
    FILE* optr;
    iptr = fopen("C-large-1.in","r");
    optr = fopen("out.txt","w");
    Node hPtr = NULL,tPtr = NULL,tempPtr = NULL;
    for(j = 1; j <= MAX; j++) {
        sq = j*j;
        if( isCycle(j) && isCycle(sq) ) {
            tempPtr = (Node) malloc(sizeof(struct node));
            tempPtr->ori = j;
            tempPtr->sq = sq;
            tempPtr->next = NULL;
            if( NULL == hPtr ) {
                hPtr = tempPtr;
            }
            else {
                tPtr = hPtr;
                while( NULL != tPtr->next )
                    tPtr = tPtr->next;
                tPtr->next = tempPtr;
            }
        }
    }
    fscanf(iptr,"%d",&T);
    for(i = 1; i <= T; i++) {
        fscanf(iptr,"%I64d%I64d",&A,&B);
        num = 0;
        tPtr = hPtr;
        while( NULL != tPtr && tPtr->sq <= B ) {
            if( tPtr->sq >= A )
                num++;
            tPtr = tPtr->next;
        }
        fprintf(optr,"Case #%d: %I64d\n",i,num);
    }
    fclose(iptr);
    fclose(optr);
    return 0;
} 
