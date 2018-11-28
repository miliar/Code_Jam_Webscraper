#include<bits/stdc++.h>
#include <string>
using namespace std;
int main (){
ifstream input;
input.open("A-large.in");
ofstream ouptput;
ouptput.open("test1.txt");
int t;
input>>t;
for(int k=0;k<t;k++){
    int cnt=0;
    long long maxs;
    string orx;
    input>>maxs>>orx;
    long long n=orx.length();
    long long arr[n];
    for(int i=0;i<n;i++){
        int x=orx[i]-'0';
        arr[i]=x;
    }
    for(int k=n-1;k>=0;k--){
            int sum=0;
        for(int j=k-1;j>=0;j--){
            sum+=arr[j];

        }
      if(k > sum){
          int diff= k-sum;
            arr[0]+=diff;cnt+=diff;
}
    }
ouptput<<"Case #"<<k+1<<": "<<cnt<<endl;

}









}






