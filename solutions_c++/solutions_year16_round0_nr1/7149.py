#include <iostream>
#include <string>
#include <cstdio>
#include <map>
using namespace std;
map<int,int> mymap;
bool distinct(int n){
    if(n==0) {
        return true;
    }
    int a=n;
    while(a) {
        mymap[a%10]=1;
        a /= 10;
    }
    if(mymap.size()==10){
        return true;
    } else {return false;}
}

int main(){
freopen("A-large.in","r",stdin);
freopen("output.txt","w",stdout);
int t;
long long int test, test1,i=1;
cin>>t; int T=t;
while(t--) {
    cin>>test;
    test1 = test;
    while(!distinct(test) || i==100){
        test=test+test1;
        i = i+1;
    }
    if(mymap.size()!=10){
    cout<<"Case #"<<T-t<<": INSOMNIA"<<endl;
    } else {
        cout<<"Case #"<<T-t<<": "<<test<<endl;
    }
    i=1;mymap.clear();
}
return 0;
}
