#include <cstdio>
#include <string>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
using namespace std;

int T,N,J;
long long interpret[9];
int divisor[9];

long long getInterpretation(int base, int arr[], int quantity){
    long long value=0;
    long long multiply=1;
    for (int i=quantity-1;i>=0;i--){
        value=value+arr[i]*multiply;
        multiply*=base;
    }
    return value;
}

bool isPrime (long long num)
{
    if (num <=1)
        return false;
    else if (num == 2)
        return true;
    else if (num % 2 == 0)
        return false;
    else
    {
        bool prime = true;
        int divisor = 3;
        double num_d = static_cast<double>(num);
        int upperLimit = static_cast<int>(sqrt(num_d) +1);

        while (divisor <= upperLimit)
        {
            if (num % divisor == 0)
                prime = false;
            divisor +=2;
        }
        return prime;
    }
}

bool checkArrayPrime(long long arr[]){
    for (int i=0;i<9;i++){
        if (isPrime(arr[i]))
            return false;
    }
    return true;
}

int getNonTrivialDivisor(long long N){
    for(int i=2;i<=10000;i++){
        if (N%i==0)
            return i;
    }
    return -1;
}

int main(){
    cin >> T;
    cin >> N;
    cin >> J;
    int j=0;;
    int bitar[N];
    bitar[0]=1;
    bitar[N-1]=1;
    for (int i=1;i<=N-2;i++){
        bitar[i]=0;
    }
    int seqPointer=N-2;
    cout<<"Case #1:"<<endl;
    int p=0;
    while(j<J){
    p=0;
        for (int i=0;i<9;i++){
            interpret[i]=getInterpretation(i+2,bitar,N);
            divisor[i]=getNonTrivialDivisor(interpret[i]);
            if (divisor[i]==-1)
                p=-1;
        }

        if (checkArrayPrime(interpret)&&p==0){
            for (int i=0;i<N;i++){
            cout<<bitar[i];
            }
            cout<<" ";
            j++;
            for(int i=0;i<9;i++){
            //cout<<"Base"<<i+2<<":"<<interpret[i]<<endl;
            cout<<divisor[i]<<" ";
            }
            cout<<endl;
            //cout<<"Jamcoin quantity:"<<j<<endl;
        }

        seqPointer=N-2;
        for (seqPointer;seqPointer>0;seqPointer--){
            if (bitar[seqPointer]==0){
                bitar[seqPointer]=1;
                break;
            }
            bitar[seqPointer]=0;
        }
    }
}


//SoliDeoGloria
