#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
using namespace std;
int main(){
FILE *fin = freopen("A-large.in", "r", stdin);
   assert(fin!=NULL);
FILE *fout = freopen("A-large.out", "w", stdout);
int n;
cin >>n;
int* cases=new int[n];
for (int i=0;i<n;i++){
    cin>>cases[i];
}
int nums[10];
for(int i=0;i<10;i++){
    nums[i]=-1;
}
for(int i=0;i<n;i++){
    for(int i=0;i<10;i++){
    nums[i]=-1;
    }
    if(cases[i]==0){
        cout<<"Case #"<<i+1<<": ";
        cout<<"INSOMNIA\n";
        continue;
    }
    int k=1;
    int check=cases[i];
    while(true){
        check=cases[i]*k;
        k++;
        int result=check;
        while(check){
            nums[check%10]=check%10;
            check=check/10;
        }
        bool found=true;
        for(int j=0;j<10;j++){
            if(nums[j]!=j){
                found=false;
                break;
            }
        }
        if(found){
            cout<<"Case #"<<i+1<<": ";
            cout<<result<<endl;
            break;
        }
    }


}
//FILE *fin = freopen("A-small.in", "r", stdin);
  //  assert(fin!=NULL);
//FILE *fout = freopen("A-small.out", "w", stdout);


}
