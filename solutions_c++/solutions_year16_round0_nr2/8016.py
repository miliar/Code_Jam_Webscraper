#include<iostream>
#include<stdio.h>
using namespace std;
int take_inp(bool a[]){
    int  n =0;
    char ch='\0';
    while (ch=getchar_unlocked()){
        if(ch=='+' || ch=='-'){
            a[n++]= ch=='+'?true:false;
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
void print_(bool a[],int n){
    for(int i=0;i<n;i++){
        if(a[i])
            cout<<"+";
        else
            cout<<"-";
    }
}
void flip(bool a[],int n){
    for(int i=0;i<n/2;i++){
        bool temp=a[i];
        a[i]=!a[n-1-i];
        a[n-1-i]=!temp;
    }
    if(n&1)
        a[n/2]=!a[n/2];
}
int find_plus(bool a[],int n){
    int start=false;
    for(int i=0;i<n-1;i++){
        if(a[i]){
            for(int k=i+1;k<n-1;k++)
                if(a[k]==false)
                    return k;
            return i+1;
        }
    }
    return -1;
}
int find_plus_max(bool a[],int n){
    int max=0,max_temp=0;
    int ind=0,ind_temp=0;
    for(int i=0;i<n-1;i++){
        if(a[i]){
            ind_temp=i+1;
            max_temp++;
            if(max_temp>max){
                max=max_temp;
                ind=ind_temp;
            }
        }
    }
    if(max!=0)
        return ind;
    return -1;
}
int main(){
    bool ch[100];
    int n=0;
    int testcases;
    cin>>testcases;
    take_inp(ch);
    int count=1;
    while(testcases--){
        n=take_inp(ch);
        int ans=0;
        //printf("\n  ==== string=");
        //print_(ch,n);
        //printf(" size=%d",n);
        int N=n;
        while(n>0){
            while(ch[n-1]==true && n>0){
                n--;
            }
            if(n==0)
                break;
            int ind=-1;
            if(ch[0]==true){
                //printf(" going to find plus in string ");
                ind=find_plus_max(ch,n);
            }
            //printf(" plus index is %d",ind);
            if(ind!=-1){
                flip(ch,ind);
                ans++;
                //printf(" after flip string is ");
                //print_(ch,N);
            }
            flip(ch,n);
            //printf(" after flip string is ");
            //print_(ch,N);
            ans++;
            //cin>>ind;
        }
        printf("Case #%d: %d\n",count,ans);
        count++;
    }
    return 0;
}
