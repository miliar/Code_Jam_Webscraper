#include<stdio.h>
#include<stdlib.h>
#include <inttypes.h>
uint64_t getNumradius(uint64_t radius , uint64_t limit) {
    uint64_t start =0, count=0;
    for(int i =1 ; start <= limit ;i+=4) {
        start +=  2*radius + i;
        if(start <= limit)
            count++; 
    }
    return count;

}

int main() {
    int count;
    uint64_t radius , totalpaint;
    FILE *fp = fopen("input.txt","r");
    int total =1;
    char c;
    fscanf(fp,"%d",&count);
    while(total <= count ) {
        fscanf(fp,"%lld",&radius);
        fscanf(fp,"%lld",&totalpaint);
        printf("Case #%d: %lld\n", total, getNumradius(radius,totalpaint));
        total++;
        fscanf(fp,"%c",&c);

    }

}
