#include<math.h>
#include<stdio.h>
#include<iostream.h>
#include<string.h>
using namespace std;


int main() {
    int n,i,t,temp=1;
    
    cin>>t;
    for(temp=1;temp<=t;temp++) {
        string s;
        int count=0;
        cin>>s;
        for(i=0;s[i+1]!='\0';i++){
            if(s[i]!=s[i+1])
                count++;
        }
        if(s[i] == '-')
            count++;
        cout<<"Case #"<<temp<<": "<<count<<endl;
      
    }
        
          
    
    
    
    return 0;
}