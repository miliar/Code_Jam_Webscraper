#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int t,i;
    cin>>t;
    for(i=0;i<t;i++){
    int n;
    cin >> n;
//        cout<<n<<endl;
    vector<int> arr;
    int j=n,k=1;
     while(1){if(n==0){
             break;
         }
    int num=0; 
    do {
     ++num; 
        arr.push_back(j%10);
     j /= 10;
} while (j);
    sort(arr.begin(),arr.end());
arr.erase(unique(arr.begin(),arr.end()),arr.end());
         if(arr.size()==10)break;
         else j=k*n;
                  k++;
     }
        if(n==0) cout<<"Case #"<<(i+1)<<": "<<"INSOMNIA"<<endl;
else    cout<<"Case #"<<(i+1)<<": "<<(k-1)*n<<endl;
    }
    return 0;
}
