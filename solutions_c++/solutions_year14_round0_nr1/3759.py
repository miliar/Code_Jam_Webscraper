#include<iostream>
using namespace std;

int main()
{
  int t,a1,a2,F[4],count,ans,temp;
  cin>>t;
  for(int l=1;l<t+1;l++){
    cin>>a1;
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
	cin>>temp;
	if(i==a1-1)
	  F[j]=temp;
      }
    }
    cin>>a2;
    count=0;
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
	cin>>temp;
	if(i==a2-1){
	  for(int k=0;k<4;k++){
	    if(F[k]==temp){
	      count++;
	      ans = temp;
	    }
	  }
	}
      }
    }
    if(count==0)
      cout<<"Case #"<<l<<": Volunteer cheated!"<<endl;
    else if(count==1)
      cout<<"Case #"<<l<<": "<<ans<<endl;
    else 
      cout<<"Case #"<<l<<": Bad magician!"<<endl; 
  }
}
