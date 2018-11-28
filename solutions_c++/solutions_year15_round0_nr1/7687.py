#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
using namespace std;
int t;
int shyness[1005];
ofstream fout("A-large.out");
int main(){
    freopen("A-large.in","r",stdin);
	cin>>t;
	for(int k=1;k<=t;k++){
        int smax;
        cin>>smax;
        string temp;
        cin>>temp;
        for(int i=0;i<=smax;i++){
            shyness[i]=temp[i]-'0';
//            cout<<shyness[i];
        }
//        cout<<endl;
        int ans=0;
        int audience=shyness[0];
        for(int i=1;i<=smax;i++){
//            cout<<audience<<" ";
            if(shyness[i]&&audience<i){
                ans+=i-audience;
                audience+=i-audience;
            }
            audience+=shyness[i];
        }
//        cout<<audience<<endl;
        fout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}
