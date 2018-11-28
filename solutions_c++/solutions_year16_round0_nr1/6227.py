#include<iostream>
#include<fstream>
using namespace std;
    ifstream inn("A-large.in");
    ofstream out("out.txt");

int main(){
     long  T;
    inn>>T;
    for(int TS=1;TS<=T;TS++){
        long long N;
        inn>>N;
        long long count=1;
        int arr[10]={0};

        while(1){
                if(N==0){
                     out<<"Case #"<<TS<<": INSOMNIA"<<endl;
                    break;
                }
            long long temp=count*N;
            count++;
            while(temp!=0){
                int val=temp%10;
                temp/=10;
                arr[val]=1;
            }int f=0;
            for(int i=0;i<10;i++){
                if(arr[i]!=1){
                    f=1;
                    break;
                }
            }
            if(f==0){
                    out<<"Case #"<<TS<<": "<<(count-1)*N<<endl;
                    break;
            }
        }
    }
}
