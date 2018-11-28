#include<iostream>
using namespace std;
void a_case(){
    int k,c,s;
    cin>>k>>c>>s;
    long long a=1;
    for(int i=1;i<c;i++){
        a*=s;
    }
    for(int i=0;i<s;i++){
        cout<<a*i+1<<" ";
    }

}
int main(){
    int i;
    cin>>i;
    for(int k=0;k<i;k++){
        cout<<"Case #"<<k+1<<": ";
        a_case();
        cout<<endl;
    }
}
/*
5
2 3 2
1 1 1
2 1 2
2 1 2
3 2 3*/
