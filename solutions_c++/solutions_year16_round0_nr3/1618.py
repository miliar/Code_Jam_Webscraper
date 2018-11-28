#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int N, J;
int divs[10];
int divs1[10] = {257, 2, 65537, 2, 17, 2, 97, 2, 17};
int divs2[10] = {65537, 2, 641, 2, 353, 2, 193, 2, 353};
int num[10];
int tens[10];
int twos[15];

void make_ten(){
    tens[0] = 1;
    int i;
    for(i = 1; i < 10; i++){
        tens[i] = tens[i-1] * 10;
    }
    return;
}

void make_two(){
    twos[0] = 1;
    int i;
    for(i = 1; i < 15; i++){
        twos[i] = twos[i-1] * 2;
    }
    return;
}

void make_divs(){
    int i;
    if(N == 16){
        for(i = 0; i < 9; i++) divs[i] = divs1[i];
    }
    else{
        for(i = 0; i < 9; i++) divs[i] = divs2[i];
    }
    return;
}

int make_num(int xp){
    int x = xp;
    int j;
    int Num = 0;
    for(j = 0; j < 10; j++){
        if(x % 2 == 1){
            Num += tens[j];
        }
        x = x / 2;
    }
    return Num;
}

main(){
    FILE *inp = fopen("coinjam.in", "r"), *outp = fopen("coinjam.out", "w");
    fscanf(inp, "%d", &N);
    fscanf(inp, "%d %d", &N, &J);
    fprintf(outp, "Case #1:\n");
    int i,j;
    int num;
    make_divs();
    make_ten();
    make_two();
    long long int temp;
    long long int TEN = 1000000000000000;
    for(i = 0; i < J; i++){
        num = make_num(i);
        temp = TEN + 1 + num*10;
        fprintf(outp, "%lld%lld ", temp, temp);
        for(j = 0; j < 9; j++){
            fprintf(outp, "%d ", divs[j]);
        }
        fprintf(outp, "\n");
    }
    return 0;
}
