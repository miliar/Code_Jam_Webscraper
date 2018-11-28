#include <iostream>
using namespace std;
typedef long long LL;

int main(int argc, const char * argv[]) {
    LL t=0,j=0,s=0,i=0,p=0,diff=0,tot=0;
    LL x[1001] = {0};
    string str;
    cin>>t;
    
    for(j=1;j<=t;j++) {
        cin>>s;
        cin>>str;
        tot=0;
        x[0] = str[0]-48;
        for(i=1;i<str.length();i++) {
            p = str[i]-48;
            diff=0;
            if(p!=0 && x[i-1]<i) {
                diff = i-x[i-1];
                tot+=diff;
            }
            x[i]=x[i-1]+p+diff;
        }
        cout<<"Case #"<<j<<": "<<tot<<endl;
    }
    
    return 0;
}
