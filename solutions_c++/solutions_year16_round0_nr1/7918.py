#include<iostream>
#include<stdio.h>
using namespace std;
int take_inp(){
    int  n =0;
    char ch='\0';
    while (ch=getchar_unlocked()){
        if(ch>='0' && ch<='9'){
            n=(n<<3)+(n<<1)+(ch-'0');
        }
        else if(ch=='\n' || ch==' '){
            ////printf("\n++++  take_inp returning %d",n);
            return n ;
        }
        else {
            return 0;
        }
    }
}
bool check(int ind[],int &sum,int num){
    while(num>0){
        int temp=num%10;
        if(ind[temp]==0){
            ind[temp]=1;
            sum=sum+temp+1;
        }
        num=num/10;
    }
    if(sum==55)
        return true;
    return false;
}
int main(){
    int sum=0;
    int ind[10];
    int testcases=take_inp();
    int count=1;
    while(testcases--){
        int N=take_inp();
        bool temp=false;
        sum=0;
        for(int k=0;k<10;k++){
            ind[k]=0;
        }
        int i=0;
        if(N==0)
            i=73;
        for(;i<73;i++){
            if(check(ind,sum,N*i)){
                printf("Case #%d: %d\n",count,N*i);
                temp=true;
                break;
            }
        }
        if(!temp)
            printf("Case #%d: INSOMNIA\n",count);
        count++;
    }
    return 0;
}
