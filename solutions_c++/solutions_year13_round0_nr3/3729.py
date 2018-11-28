
#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int t;
    int a,b;
    int count;
    int s[5]={1, 4, 9, 121, 484};
    cin>>t;
    for (int k=1; k<=t; k++){
            count = 0;
          cin>>a>>b;
          for (int i=a; i<=b; i++){
              for (int j=0; j<=4; j++){
          if (i==s[j]){
          count++;
          }
          }
          }
          cout<<"Case #"<<k<<": "<<count<<endl;
    }
}
