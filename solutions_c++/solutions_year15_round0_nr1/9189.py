#include <iostream>
using namespace std;

int main(){
  int Smax,T;
  cin>>T;
  for (int i=1;i<=T;i++){
    cin>>Smax;
	char input;
	int result=0,count=0;
    for (int j=0;j<=Smax;j++){
		cin>>input;
		if (input==0) continue;
		if (count<j){
			result+=(j-count);
		count+=(input-'0')+j-count;
		}
		else
		count+=(input-'0');
      
    }
    cout<<"Case #"<<i<<": "<<result<<endl;

  }
}
