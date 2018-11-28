#include<iostream>
#include<set>
using namespace std;

void c() {
    int l;
   cin>>l;
    if(l==0) {cout<<"INSOMNIA";return;}
    set<int> st;
    int i=1;
    while(i) {
        int a = i*l;
        while(a>0) {
            int digit = a % 10;
            st.insert(digit);
            a/=10; 
        }
        if(st.size()==10) {
            cout<<i*l;
            return;
        }
        i++;
        
    }
}

int main() {
    int t;
    cin>>t;
    for(int i=1;i<=t;i++) {cout<<"Case #"<<i<<": ";c();cout<<endl;}
}
