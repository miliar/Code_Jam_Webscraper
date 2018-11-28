#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
int main(){
    int t,l,k,i,j,n,a[4],b[4],c[4],x;
    ifstream in;
    in.open("input.txt");
    ofstream op;
    op.open("output.txt");
    in>>t;
    for(l=1;l<=t;l++){
        in>>n;
        for(i=1;i<5;i++){
            if(i==n){
                for(j=0;j<4;j++)
                    in>>a[j];
            }
            else{
                for(j=0;j<4;j++)
                    in>>x;
            }
        }
        in>>n;
        for(i=1;i<5;i++){
            if(i==n){
                for(j=0;j<4;j++)
                    in>>b[j];
            }
            else{
                for(j=0;j<4;j++)
                    in>>x;
            }
        }
        int k=0;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                if(a[i]==b[j]){
                    c[k++]=b[j];
                    b[j]=a[i]=-1;
                    break;
                }
            }
        }

        op<<"Case #"<<l<<": ";
        if(k==0)
            op<<"Volunteer cheated!"<<endl;
        else if(k==1)
            op<<c[0]<<endl;
        else op<<"Bad magician!"<<endl;
    }
    return 0;
}
