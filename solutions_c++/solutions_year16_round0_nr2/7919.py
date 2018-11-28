#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int cnt=0;
int numall;
void reverses(char a[],int num){
    char b[num];
    for(int i=0;i<num;i++){
        b[num-i-1] = a[i]=='+' ? '-':'+';
    }
    for(int i=0;i<num;i++){
        a[i] = b[i];
    }
    cnt++;
}
void flips(char a[],int num){
    if(num>0){
        if(a[0]=='-' && a[num-1]=='-'){
            reverses(a , num);
            int tmp = num-1;
            while(a[tmp] != '-'){
                num--;
                tmp--;
            }
            flips(a,num);
        } else if(a[0]=='+' && a[num-1] =='-') {
            int tmp = 0;
            while(a[tmp++]=='+');
            reverses(a,tmp-1);
            flips(a,num);
        } else {
            int tmp = num-1;
            while(a[tmp] != '-'){
                num--;
                tmp--;
            }
            flips(a,num);
        }
    }
}

int main(){
    char x[101]={};
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        cnt=0;
        scanf("%s",x);
        int z = (unsigned)strlen(x);
        numall = z;
        flips(x,z);
        printf("Case #%d: %d\n",i+1,cnt);
    }
}
