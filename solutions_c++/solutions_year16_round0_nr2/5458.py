#include<iostream>
using namespace std;
int a_case(){
    string pancakes;
    cin>>pancakes;
    pancakes+='+';
    int count=0;
    for(int i=0;i<pancakes.size()-1;i++){
        if(pancakes[i]!=pancakes[i+1])  count++;
    }
    return count;
}
int main(){
    int n;
    cin>>n;
    string output="";
    for(int i=0;i<n;i++){
        cout<<"Case #"<<i+1<<": "<<a_case()<<endl;
    }
}
