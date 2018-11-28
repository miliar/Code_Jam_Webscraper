#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>

using namespace std;

unsigned long long powr(unsigned long long num1, unsigned long long num2)
{
    unsigned long long answer=1;
    for(int i=0;i<num2;i++){
        answer=answer*num1;
    }
    return answer;
}
unsigned long long isprime(unsigned long long num){
    if (num ==0)
        return 0;
    for(unsigned long long i=2;i<num/2;i++){
        if(num%i==0){
            return i;
        }
        if(i==100000)
            return 0;
    }
    return 0;
}
unsigned long long cnvrt(int* arr,int siz,int base){
    unsigned long  long result=0;
    for(int i=0;i<siz;i++){
        result = result+ powr(base,(siz-i-1))*arr[i];
    }
    return result;
}

int main(){
    int T;
    cin >> T;
    int N;
    int J;
    cin >> N >> J;

    int f;
    int* coin=new int[N];
    int cas =1;
    cout<<"Case #"<<cas<<": \n";
    for(int i=0;i<powr(2,N-2);i++){
        for(int j=0;j<(N-2);j++){
            coin[j+1]=i/int(powr(2,N-3-j))%2;
        }
        coin[0]=1;
        coin[N-1]=1;
        int ch;
        unsigned long long divisors[9];
        for(int ii=0;ii<9;ii++){
            divisors[ii]=0;
        }
        for(int l=0;l<9;l++){
            ch=isprime(cnvrt(coin,N,l+2));
            if (ch==0)
                break;
            else
                divisors[l]=ch;
        }
        if(ch==0)
            continue;
        else{
            J--;
            for(int kk=0;kk<N;kk++) cout<<coin[kk];
            cout<<" ";
            for(int ii=0;ii<9;ii++)cout<<divisors[ii]<< " ";
            cout<<endl;
        }
        if(J==0)
            break;

    }
}
