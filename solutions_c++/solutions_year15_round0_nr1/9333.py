#include <iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    for(int k=0;k<t;k++){
        int n;
        cin>>n;
        int a[n+1];
        for(int i=0;i<n+1;i++){
            char c;
            cin>>c;
            a[i]=c-'0';
        }
        int count=0;
        int up=0;
        for(int i=0;i<n+1;i++){
            if(up>=i)up+=a[i];
            else {count=count+i-up;up=a[i]+i;}
        }
        cout<<"Case #"<<k+1<<": "<<count<<endl;
    }
	// your code goes here
	return 0;
}
