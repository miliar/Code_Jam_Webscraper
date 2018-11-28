#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("answer.txt");
bool flag[10];

void init(){
    for(int i=0;i<10;i++){
        flag[i]=false;
    }
}

void divide(long long n){
    while(n){
        flag[n%10]=true;
        n/=10;
    }
}

bool judge(){
    for(int i=0;i<10;i++){
        if(!flag[i]){
            return false;
        }
    }
    return true;
}

int main(){
    int T;
    fin>>T;
    for(int t=1;t<=T;t++){

        init();

        fout<<"Case #"<<t<<": ";
        long long num;
        fin>>num;

        if(num==0){
            fout<<"INSOMNIA"<<endl;
            continue;
        }

        int i=1;
        while(!judge()){
            divide(num*i);
            i++;
        }
        fout<<num*(i-1)<<endl;
    }
	return 0;
}
