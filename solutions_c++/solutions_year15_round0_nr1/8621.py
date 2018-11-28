#include<iostream>
#include<cstdio>

using namespace std;

int main(){
  int t;
  cin>>t;
  int caseVar=1;
  while(t--){
    int max;
    string s;
    cin>>max;
    cin>>s;
    if(s.size()>1){
       int count=0;
       int len=0;
       for(int i=1;i<s.size();i++){
	 len+=int(s[i-1]-'0');
	 int currentChar=int(s[i]-'0');
         if(len<i && currentChar!=0) {
	   count+=i-len;
	   len+=i-len;
	   //cout<<len<<" "<<count<<" "<<currentChar<<" "<<i<<endl;
	   
	}
	
	 
      }
      cout<<"Case #"<<caseVar<<": "<<count<<endl;
      caseVar++;
    }
    else{
      cout<<"Case #"<<caseVar<<": 0"<<endl;
      caseVar++;
    }
  }
  
  return 0;
}