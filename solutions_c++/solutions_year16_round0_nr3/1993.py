#include<bits/stdc++.h>
using namespace std;

int x[40];
pair<int,int> y[1000];
int main(){
    int T,n;
    //FILE *in = fopen("input.txt","r");
    FILE *out = fopen("output.txt","w");
    fprintf(out,"Case #1:\n");
    x[0]=x[31]=1;
    int c=0;
    for(int i=0;i<15;i++)
        for(int j=i+1;j<15;j++)
            y[c++]=make_pair(i,j);
   for(int i=0;i<50;i++)
        for(int j=0;j<10;j++){
            pair<int,int>a =y[i];
            pair<int,int>b =y[j];
            for(int k=1;k<=30;k++) x[k]=0;
            x[2*a.first+1]=1;
            x[2*a.second+1]=1;
            x[2*b.first+2]=1;
            x[2*b.second+2]=1;
            for(int k=0;k<=31;k++) fprintf(out,"%d",x[k]);
            fprintf(out," 3 4 5 6 7 8 9 10 11\n");
        }
}
