#include<iostream>
#include <bits/stdc++.h>
using namespace std;


int main() {
	int t,p,n,m,mode,ans;
	string s;
	cin>>t;
	for(int k=0;k<t;k++){
	    p=0;mode=0;ans=0;
	    cin>>s>>n;
	    m=s.size();
	    mode=m-n+1;
	    for(int i=0;i<mode;i++){
	        if(s[i]=='+');
	        else{
    	        ans++;
    	        //cout<<i<<s<<endl;
	            for(int j=i;j<i+n;j++){
    	            if(s[j]=='+')s[j]='-';
    	            else s[j]='+';
    	        }    
	        }
	        
	    }
	    //cout<<s<<endl;
	    if(s[m-n]=='-')p=1;
	    for(int i=m-n+1;i<m;i++){
	        if(s[i]!=s[i-1]){
	            p=1;
	            break;
	        }
	    }
	    if(p==1)cout<<"Case #"<<k+1<<": "<<"IMPOSSIBLE"<<endl;
	    else cout<<"Case #"<<k+1<<": "<<ans<<endl;
	}
	
	return 0;
}
