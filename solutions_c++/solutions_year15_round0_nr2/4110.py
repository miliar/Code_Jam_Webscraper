#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;



int findMin(int A[50],int n){
    int t1,t2,max,newN,i,B[50],t3;
    sort(A,A+n);
    t1=A[n-1];
    newN=n;
    if(A[n-1]<4) return t1;
    max=A[n-1];
    for(i=0;i<n;i++) B[i]=A[i];
    for(i=n-1;i>=0;i--){
        if(A[i]==max){
            if(A[i]%2==0){
                A[newN++]=A[i]/2;
                A[i]=A[i]/2;
            }
            else{
                A[newN++]=A[i]/2;
                A[i]=A[i]/2+1;
            }
        }
        else break;
    }
    t2=findMin(A,newN)+newN-n;
    newN=n;

    max=B[n-1];
    for(i=n-1;i>=0;i--){
        if(B[i]==max){
            if(B[i]%3==0){
                B[newN++]=B[i]/3;
                B[newN++]=B[i]/3;
                B[i]=B[i]/3;
            }
            else if(B[i]%3==1){
                B[newN++]=B[i]/3;
                B[newN++]=B[i]/3;
                B[i]=B[i]/3+1;
            }
            else{
                B[newN++]=B[i]/3;
                B[newN++]=B[i]/3+1;
                B[i]=B[i]/3+1;
            }
        }
        else break;
    }
    t3=findMin(B,newN)+newN-n;
    if(t1<t2){
        if(t1<t3) return t1;
        else return t3;
    }
    else{
        if(t2<t3) return t2;
        else return t3;
    }
}



int main() {
    int i,j,k,T,count,d,n,A[50];
    cin>>T;
    for(j=1;j<=T;j++){
        cin>>d;
        for(i=0;i<d;i++) cin>>A[i];
        cout<<"Case #"<<j<<": "<<findMin(A,d)<<"\n";
    }
    return 0;
}
