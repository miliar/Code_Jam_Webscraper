#include<iostream>
#define ul unsigned long
#define MAX 1000
#include<stdio.h>

using namespace std;

ul pal[MAX+100];

bool checkPal(ul num){
    ul rev=0;
    ul temp = num;
    while(num!=0){
        rev *= 10;
        rev += num%10;
        num /= 10;
    }
    if(temp==rev) return true;
    return false;
}

void pre_code(){
    ul cnt=0;
    for(int i=1;i<=MAX;i++){
        if(i*i>MAX){
                if(pal[i]==0) pal[i] = pal[i-1];
        }
        else{
            if(pal[i]==0) pal[i] = pal[i-1];
            if((checkPal(i))&&(checkPal(i*i))){
                cnt++;
                pal[i*i]=cnt;
            }
        }
    }
}

int main(){
    freopen("Csmalloutput.txt","w",stdout);
    pre_code();
    int T,cases = 1;
    cin>>T;
    while(T--){
        ul a,b;
        cin>>a>>b;
        cout<<"Case #"<<cases++<<": "<<pal[b]-pal[a-1]<<endl;
    }
    return 0;
}
