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

long long nums[11];

void convert(int number[],int N){

    for(int i=2;i<=10;i++){
            nums[i]=0;
            for(int j=0;j<N;j++){
                nums[i]=nums[i]*i+number[j];
            }
    }

}

int isValid(){
    for(int i=2;i<11;i++){
        int f=0;
        if(nums[i]%2==0)
            f=1;
        else{
            for(long long j=3;j<=sqrt(nums[i]);j+=2){
                if(nums[i]%j==0){
                    f=1;
                    break;
                }
            }
        }
        if(f==0){
            return 0;
        }
    }
    return 1;
}

void proofs(){
    for(int i=2;i<11;i++){
        for(long long j=2;j<=sqrt(nums[i]);j++){
            if(nums[i]%j==0){
                cout<<" "<<j;
                break;
            }
        }
    }
}

void increament(int number[],int N){
    int i=N-2;
    number[i]++;
    while(number[i]>1&&i>0){
        number[i]-=2;
        number[i-1]++;
        --i;
    }
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);

    int TestCases;
    cin>>TestCases;
    for(int testcase=0; testcase<TestCases; testcase++){
            cout<<"Case #"<<(testcase+1)<<":\n";
            int N,J;
            cin>>N>>J;
            int number[17]={0};
            number[0]=number[N-1]=1;
            for(int i=0;i<J;){
                convert(number,N);
                if(isValid()){
                    for(int j=0;j<N;j++){
                        cout<<number[j];
                    }
                    proofs();
                    cout<<endl;
                    i++;
                }
                increament(number,N);
            }
    }
    return 0;
}
