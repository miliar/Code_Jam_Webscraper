#include<iostream>
#include<fstream>
#include<map>
using namespace std;
main(){
    ifstream in("A-large.in");
    ofstream out("output.txt");
    long long Test;
    in>>Test;

    for(int t=1;t<=Test;t++){
        long long N,c=1,result;
        int sum = 0;
        in>>N;
        map <int,int>visit;
        if(N==0)
            out<<"Case #"<<t<<": INSOMNIA\n";
            else{
        while(1){
            long long temp,flag=1;;
            temp=N*c;
            result=temp;
            while(temp!=0){
                long digit=temp%10;
                visit[digit]=1;
                temp/=10;
                }
            sum = 0;
            for(int i=0;i<=9;i++){
                sum+= visit[i];
            }
            if(sum == 10){
                break;
            }
            c++;
        }
        out<<"Case #"<<t<<": "<<result<<endl;}
    }
}
