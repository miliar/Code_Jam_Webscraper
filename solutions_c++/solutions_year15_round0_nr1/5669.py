#include<iostream>
using namespace std;

void asd(){
    int x,a[1001],count=0,add=0;
    string s;
    cin >> x >> s; x++;
    for(int i=0; i<x; i++){a[i]=int(s[i])-int('0');}
    for(int i=0; i<x; i++){
            if(count>=i and a[i]>0){count+=a[i];}
            else if(a[i]>0){add+=i-count; count=i+a[i];}
    }
    cout << add << endl;
}

int main(){
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);
    int t;
    cin >> t;
    for(int i=1; i<=t; i++){
            cout << "Case #" << i << ": "; asd();
    }
    return 0;
}
