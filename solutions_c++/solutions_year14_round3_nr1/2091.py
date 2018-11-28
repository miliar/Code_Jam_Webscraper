#include<bits/stdc++.h>
using namespace std;
int test(int q){
  if(q==1 || q==0)
    return 0;
  else if(q%2==1)
    return 1;
  else
    return(test(q/2));
}

int main(){
  int t,i,p,q,count;
  unsigned j;
  cin>>t;
  string s,s1,s2;
  for(i=1;i<=t;i++){
    
    cin>>s;
    j = s.find("/");
    s1=s.substr(0,j);
    s2=s.substr(j+1);
    
    istringstream buffer1(s1);
    buffer1>>p;
    istringstream buffer2(s2);
    buffer2>>q;
    
    count=0;
    
    if(q%2==1)
      {
	cout<<"Case #"<<i<<": "<<"impossible"<<endl;
	
      }
    else{
      
      while(p<q){
	if(q%2==0)
	q=q/2;
	else
	  break;
	count++;
      }
      if(p==q)
	cout<<"Case #"<<i<<": "<<count<<endl;
      else{
	if(test(q)==1)
	  cout<<"Case #"<<i<<": "<<"impossible"<<endl;
	else
	  cout<<"Case #"<<i<<": "<<count<<endl; 
      }
    }
  }
  
  return 0;
}
