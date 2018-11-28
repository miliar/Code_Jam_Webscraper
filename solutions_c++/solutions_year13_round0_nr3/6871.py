#include<stdio.h>
#include<iostream>
#include<fstream.h>
#include<string>
using namespace std;

int main(){
    int c[5]={1,4,9,121,484};
    char s1[50],s2[50],s3[50];
    int t;
    ifstream f1("input.txt");
    ofstream f2("output.txt");
    f1 >> s1;
    t=atoi(s1);
    int i;
    for (i=1;i<=t;i++){
        int a,b;
        f1 >> s2;
        f1 >> s3;
        a=atoi(s2);
        b=atoi(s3);
        int j,count=0;
        for (j=0;j<5;j++){
            if (c[j]>=a && c[j]<=b)
            count++;
            }
            if (i<t)
        f2 << "Case #"<<i<<": "<<count<<endl;
        else 
        f2 << "Case #"<<i<<": "<<count;
        }
    }
