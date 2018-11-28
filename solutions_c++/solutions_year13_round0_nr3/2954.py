#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <fstream>
    FILE *fp2 = fopen("C:/ikj/output.txt","w");
using namespace std;
int ispalin(long int num) {
    int num_digits=0,i;
    while(int(num/pow(10,num_digits))) num_digits++;
    for(i=0;i<num_digits/2;i++) {
        if(((int)(num/pow(10,i))%10) == ((int)(num/pow(10,num_digits-i-1))%10)) continue;
        else {//fprintf(fp2,"%d is not palindrome\n",num);
            return 0;}
    }
  //  fprintf(fp2,"%d is a palindrome\n",num);
    return 1;   
}
int main() {
    int tc,tci,i,j,k,l,start,end;
    long int output,rangea,rangeb;
    FILE *fp = fopen("C:/ikj/input.txt","r");
    fscanf(fp,"%d",&tc);
    for(tci=0;tci<tc;tci++) {
        output=0;
        fscanf(fp,"%ld%ld",&rangea,&rangeb);
        start=int(sqrt(rangea));
        if(start*start < rangea) start++;
        end=int(sqrt(rangeb));
     //   fprintf(fp2,"%d %d\n",start,end);
        for(i=start;i<=end;i++) {
            if(ispalin(i)) {
                if(ispalin(i*i)) output++;
            }
        }
        fprintf(fp2,"Case #%d: %ld\n",tci+1,output);
    }
}
