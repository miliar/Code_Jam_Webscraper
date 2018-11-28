#include <cstdio>
#include <cstdlib>
#include <cassert>
#include<cmath>
#include <iostream>
using namespace std;
unsigned long long power(unsigned long long num1, unsigned long long num2)
{
    unsigned long long answer=1;
    for(int i=0;i<num2;i++){
        answer=answer*num1;
    }
    return answer;
}
unsigned long long isprime(unsigned long long num){
    for(unsigned long long i=2;i<num/2;i++){
        if(num%i==0){
          //  cout<<num<< "  "<<i<<endl;
            return i;
        }
        if(i==100000)
            return 0;
    }
    return 0;
}
unsigned long long convert(int* arr,int siz,int base){
    unsigned long  long result=0;
    /*if(base==10){
        for (int i=0;i<siz;i++)
            cout<<arr[i];
       }
        cout<<endl;*/
    for(int i=0;i<siz;i++){
        //if (base ==10)
        //cout<<power(base,siz-i-1)*arr[i]<<endl;
        result = result+ power(base,(siz-i-1))*arr[i];
    }
    //cout<<siz<<"  "<<result<<endl;
    return result;
}
int main(){
    FILE *fin = freopen("C-small.in", "r", stdin);
    assert(fin!=NULL);
    FILE *fout = freopen("C-small.out", "w", stdout);
    int n;
    cin >>n;
    int dig;
    int nums;
    cin >>dig>>nums;

    int f;
    int* coin=new int[dig];
    int cas =1;
    cout<<"Case #"<<cas<<": \n";
    for(int i=0;i<pow(2,dig-2);i++){
        for(int j=0;j<(dig-2);j++){
            coin[j+1]=i/int(pow(2,dig-3-j))%2;
        }
        coin[0]=1;
        coin[dig-1]=1;
        int ch;
        unsigned long long divisors[9];
        for(int ii=0;ii<9;ii++){
            divisors[ii]=0;
        }
        for(int l=0;l<9;l++){
            ch=isprime(convert(coin,dig,l+2));
            if (ch==0)
                break;
            else
                divisors[l]=ch;
        }
        if(ch==0)
            continue;
        else{
            nums--;
            for(int kk=0;kk<dig;kk++) cout<<coin[kk];
            cout<<" ";
            for(int ii=0;ii<9;ii++)cout<<divisors[ii]<< " ";
            cout<<endl;
        }
        if(nums==0)
            break;

    }
}
