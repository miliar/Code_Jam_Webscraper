#include <iostream>

using namespace std;

int main() {
	int t,cnt=0;
    cin>>t;
    while(t--){
        int a,b,num=0;
        cin>>a>>b;
        for(int i=a;i<=b;i++){
            if(i==1||i==4||i==9||i==121||i==484||i==676)num++;
        }
        cout<<"Case #"<<++cnt<<": "<<num<<endl;
    }
	return 0;
}