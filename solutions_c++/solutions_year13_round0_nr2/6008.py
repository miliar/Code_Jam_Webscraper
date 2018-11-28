#include <iostream>
using namespace std;
int pattern[100][100];
int max_col[100];
int max_row[100];

int main(){
  int T;
  cin>>T;
  for(auto i=0; i< T; i++){
    int height, width;
    cin>>height>>width;
    for(auto j=0;j<height;j++){
      int max=0;
      for(auto k=0; k<width;k++){
	cin>>pattern[j][k];
	if(max<pattern[j][k])
	  max = pattern[j][k];
      }
      max_col[j]=max;
    }
    for(auto k=0; k< width; k++){
      int max=0;
      for(auto j=0; j<height; j++){
	if(max<pattern[j][k])
	  max=pattern[j][k];
      }
      max_row[k]=max;
    }
    int OK = 1;
    for(auto j=0;j<height;j++){
      for(auto k=0; k<width;k++){
	if(pattern[j][k]<max_col[j]&&pattern[j][k]<max_row[k]){
	  OK = 0;
	  break;
	}
      }
    }
    if(OK){
      cout<<"Case #"<<i+1<<": YES"<<endl;
    }
    else{
      cout<<"Case #"<<i+1<<": NO"<<endl;
    }
  }
  return 0;
}

	
	
	    
    
