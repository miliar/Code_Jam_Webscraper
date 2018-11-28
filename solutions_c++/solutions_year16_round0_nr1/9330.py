#include <bits/stdc++.h>

using namespace std;

int main(){

    int n;

    cin>>n;

    for(int i = 1;i<=n;i++){
    int num;

    cin>>num;

    set<int> l;

    if(num == 0){

    cout<<"Case #"<<i<<": INSOMNIA"<<endl;

    }

    else{


    int k = num;
    while(l.size()<10){


    int x = num;
   while(x>0){
    int d = x%10;
    x = x/10;
    l.insert(d);
   }

    num = num + k;
    }

    cout<<"Case #"<<i<<": "<<num - k<<endl;
    }
    }
}
