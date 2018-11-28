#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
    int t,n,i,j,stand,ext;
    char s[7];
    cin>>t;
    for(i=0;i<t;i++){
        stand=0;
        ext=0;
        cin>>n;
        scanf("%s",s);
        for(j=0;j<=n;j++){
            if(stand<j&&s[j]!='0'){
                ext+=(j-stand);
                stand+=ext;
            }
            stand+=(s[j]-48);
        }
        cout<<"Case #"<<i+1<<": "<<ext<<endl;
    }
	return 0;
}
