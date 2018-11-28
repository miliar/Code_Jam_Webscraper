#include <iostream>
#include <stdio.h>
#include<fstream>

using namespace std;

ifstream file("code.txt",ios::in);
ofstream out("output.txt",ios::out);
int secret=1;

int calc(){
    int crap,stand,flag=0;
    file>>crap;
    char maxno[20];
    file.getline(maxno,20);
    for(int i=1,stand =0;i<=crap+1;i++){
        if(i!=1)
            if(stand<i-1){
                flag++;
                stand++;
            }
        stand +=(int)maxno[i]-48;
    }
    return flag;
}

void  print(int g){
    cout<<"Case #"<<secret<<": "<<g<<endl;
    out<<"Case #"<<secret<<": "<<g<<"\n";
    secret++;
}

int main(){
    int testcases,a=0;
    file>>testcases;
    cout<<"Test Cases Detected:"<<testcases<<endl;
    for (int i=0;i<testcases;i++){
        a= calc();
        print(a);
    }
    return 0;
    }
