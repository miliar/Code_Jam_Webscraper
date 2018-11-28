#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

int main(){
    int t,i;
    cin>>t;
    
    for(i=0;i<t;i++){
        int count=0,ans=0,n,j;
        char str[105];
        
       // cin>>str;
        
        cin>>n;
        cin>>str;
        
        for(j=0;j<n+1;j++){
            if(count>=j){
                count = count + ((int)str[j]-48);
            }
            else{
                ans = ans + j - count;
                count = count + j - count + ((int)str[j]-48);
            }
        }
	fflush(stdout);
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
	fflush(stdout);
    }
    
    return 0;
}
