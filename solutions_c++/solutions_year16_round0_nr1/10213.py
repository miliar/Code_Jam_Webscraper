#include <stdio.h>
#include <stdlib.h>
using namespace std;

int chk[10];

void chkIni();
int numInput();
int findLast(int);
bool numChk();
void chkUpdate(int n);

FILE *fin;

int main(){
    int n;
    fin = fopen("input.txt", "r");
    FILE *fout = fopen("output.txt", "w");
    fscanf(fin, "%d", &n);
    for(int z=1;z<=n;z++){
        int num;
        chkIni();
        num = numInput();
        if(num == 0)
            fprintf(fout, "Case #%d: INSOMNIA\r\n", z);
        else{
            fprintf(fout, "Case #%d: %d\r\n", z, findLast(num));
        }
    }
    fclose(fout);
    fclose(fin);
    return 0;
}

void chkIni(){
    for(int i=0;i<10;i++)
        chk[i] = 0;
}

int numInput(){
    int num = 0;
    char tmp = '\n';
    while(tmp < '0') fscanf(fin, "%c", &tmp);
    while('0'<=tmp && tmp <='9'){
        num = num * 10 + ((int)tmp - 48);
        fscanf(fin, "%c", &tmp);
    }
    return num;
}

int findLast(int n){
    int i=1;
    do{
        chkUpdate(n*i);
        i++;
    }while(!numChk());
    return n*(i-1);
}
bool numChk(){
    int i;
    for(i=0;i<10;i++){
        if(chk[i] == 0)
            break;
    }
    return (i==10) ;
}

void chkUpdate(int n){
    do{
        chk[n%10] = 1;
        n /= 10;
    } while (n!= 0);
}
