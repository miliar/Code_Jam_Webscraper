#include<bits/stdc++.h>

using namespace std;

int main(){
     int t,i,k=1;
     string s;
     cin>>t;
     while(t--){ 
     	cin>>s;
	char prev=s.at(0);
	int cnt=0;
	for(i=1;i<s.length();++i){       
      if(s.at(i)==prev)
		continue;
	    cnt++;
	    prev=s.at(i);       
	}
	if(s.at(s.length()-1)=='-')
		cnt++;
	 cout<<"Case #"<<k++<<": "<<cnt<<endl;
   }
  
  return 0;
  }
