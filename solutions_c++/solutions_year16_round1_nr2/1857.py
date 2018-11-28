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

int Lsearch(int Arr[],int S,int n){
    for(int i=0;i<S;i++){
        if(Arr[i]==n)
            return i;
    }
    return -1;
}

int smallest(int Arr[],int S){
    int small=0;
    for(int i=1;i<S;i++){
        if(Arr[i]<Arr[small]){
            small=i;
        }
    }
    return small;
}

void solve(){
    int N;
    cin>>N;
    int K;
    K=0;
    int Nums[2500];
    int Exist[2500];
    for(int i=0;i<(2*N)-1;i++){
            for(int j=0;j<N;j++){
                int x;
                cin>>x;
                int index=Lsearch(Nums,K,x);
                if(index==-1){
                    Nums[K]=x;
                    Exist[K]=1;
                    K++;
                }
                else{
                    Exist[index]=(Exist[index]+1)%2;
                }
            }
    }
    for(int i=0;i<K;i++){
        int index=smallest(Nums,K);
        if(Exist[index])
            cout<<Nums[index]<<" ";
        Nums[index]=INT_MAX;
    }
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int TestCases;
    cin>>TestCases;
    for(int testcase=0; testcase<TestCases; testcase++){
            cout<<"Case #"<<(testcase+1)<<": ";
            solve();
            cout<<endl;
    }
    return 0;
}
