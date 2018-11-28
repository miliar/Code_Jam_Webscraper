#include <iostream>

using namespace std;

int main(int argc, char** argv){
  int T;
  int ans,wst,crd[16],sol;

  cin>>T;
  for(int i=0; i<T; i++){
    for(int j=0;j<16;j++) crd[j]=0;
    sol=-1;

    cin>>ans;  
    for(int j=0; j<4; j++){
      for(int k=0; k<4; k++){
	cin>>wst;
	if(j+1==ans) crd[wst-1]=1;
      }
    }

    cin>>ans;
    for(int j=0; j<4; j++){
      for(int k=0; k<4; k++){
	cin>>wst;
	if(j+1==ans){
	   if(crd[wst-1]>0)
	    if(sol<0) sol=wst;
	    else if(sol>0) sol=0;
	}
      }
    }

    cout<<"Case #"<<i+1<<": ";
    if(sol<0) cout<<"Volunteer cheated!";
    else if(sol==0) cout<<"Bad magician!";
    else cout<<sol;
    cout<<"\n"; 
  }


  return 0;
}
