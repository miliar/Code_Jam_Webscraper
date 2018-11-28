#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
int T;
cin >> T;
int* cases=new int[T];
for (int i=0;i<T;i++){
    cin>>cases[i];
}
int nums[10];
for(int i=0;i<10;i++){
    nums[i]=-1;
}
for(int i=0;i<T;i++){
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
            cout << "Case #" << i+1 << ": ";
            cout << result << endl;
            break;
        }
    }


  }

}
