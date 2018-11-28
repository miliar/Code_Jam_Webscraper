#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int T,i,j,k,l,smax;
    cin>>T;
    int ans[T];
     string shy;
        for(i=0;i<T;i++) {
            int count=0,frnd=0;
           
            cin>>smax>>shy;    
            for(j=0;j<smax;j++){
            count=count+((int)shy[j])-48;
            if(shy[j+1]>'0' && count<(j+1)){
                 frnd=frnd+(j+1-count); 
                   count+=j+1-count;
               }  
            }
          
            ans[i]=frnd;
        }
        
    for(i=0;i<T;i++){
        cout<<"Case "<<"#"<<i+1<<": "<<ans[i]<<endl;
    }
    
    return 0;
}