#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
	// your code goes here
	stack<char> st;
	int t,flag,count,len,j,r;
	string s;
	cin>>t;
for(int i=1;i<t+1;i++){
	    cin>>s;
	    flag=0;
	    count=0;
	    len = s.length();
	    
	   if(len>1){
	   while(flag!=1){
	       for(r=0;r<len;r++){
	           flag=1;
	           if(s[r]=='-'){
	                flag=0;
	                break;}
	       }
	       
	       if(flag==0){
	       for(int i=0;i<r;i++){
	           if(s[i]=='-'){
	                flag=2;
	                break;}
	       }
	       
	       if(flag==0 && r!=0){
	       for(int i=0;i<r;i++)
	            s[i]='-'; 
	       count++;
	       }
	       
	       
	       flag=0;
	       for(j=len-1;j>=0;j--){
	           flag=1;
	           if(s[j]=='-'){
	                flag=0;
	                break; }
	       }
	       if(flag==0){
	           count++;
	          for(int i=0;i<j+1;i++)
	            st.push(s[i]);
	           int k=0;
	          while(!st.empty()){
	              s[k]=st.top();
	              if(s[k]=='+')
	                s[k]='-';
	              else
	                s[k]='+';
	                st.pop();
	                k++;
	          }
	       }
	       
	      
	     }
	   } 
	    
	}
	else{
	    if(s=="+")
	        count=0;
	    else
	        count++;
	}
	cout<<"Case #"<<i<<": "<<count<<"\n";
 }
	return 0;
}

