#include <iostream>
using namespace std;
 
int main(){
	int a,b,c,j,i,k,T;
    long long count;
    cin>>T;
 
    for(k=1;k<=T;k++) {
         count=0;
        cin>>a>>b>>c;
        for (i=0;i<a;i++) {
            for (j=0;j<b;j++) {
                if ((i&j)<c) {
                    count++;
                }
            }
        }
        cout << "Case #"<<k<<": "<<count<<endl;
    }
    return 0;
}