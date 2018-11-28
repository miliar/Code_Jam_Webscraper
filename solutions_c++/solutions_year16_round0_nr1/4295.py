#include<stdio.h>
#include<iostream>
#include<conio.h>
#include<set>
#include<vector>
#include<string>
#include<fstream>
#include<stdlib.h>
#include<math.h>

using namespace std;

int finish(long long digits[]){
    for(int i=0;i<10;i++){
        if(digits[i]==0)
            return 0;
    }
    return 1;
}

int stucked(long long digits[]){
    long long max=digits[0], min=digits[0];
    for(int i=1;i<10;i++){
        if(digits[i]>max)
            max=digits[i];
        if(digits[i]<min)
            min=digits[i];
    }
    if(min==0){
        if(max-min>=1000)
            return 1;
    }
    return 0;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int TestCases;
    cin>>TestCases;
    for(int testcase=0; testcase<TestCases; testcase++){
            cout<<"Case #"<<(testcase+1)<<": ";
            long long N,M,rem;
            cin>>N;
            long long digits[10];
            for(int i=0;i<10;i++){
                digits[i]=0;
            }
            for(long long i=1;;i++){
                M=N*i;
                do{
                    rem=M%10;
                    M/=10;
                    digits[rem]++;
                }while(M);
                if(finish(digits))
                {
                    cout<<(N*i);
                    break;
                }
                else if(stucked(digits)){
                    cout<<"INSOMNIA";
                    break;
                }
            }
            cout<<endl;
    }
    return 0;
}
