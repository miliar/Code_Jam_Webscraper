#include<iostream>
#include<fstream>
#include<map>
using namespace std;
main(){
    ifstream in("A-large.in");
    ofstream out("output.txt");
    long Test;
    in>>Test;

    for(int t=1;t<=Test;t++){
        long N,c=1,result;
        in>>N;
        map <int,int>visit;
        if(N==0)
            out<<"Case #"<<t<<": INSOMNIA\n";
            else{
        while(1){
            long temp,flag=1;;
            temp=N*c;
            result=temp;
            while(temp!=0){
                long digit=temp%10;
                visit[digit]=1;
                temp/=10;
                }
            for(int i=0;i<=9;i++){
                if(visit[i]==0){
                    flag=0;
                    break;
                }
            }
            if(flag){
                break;
            }
            c++;
        }
        out<<"Case #"<<t<<": "<<result<<endl;}
    }
}
