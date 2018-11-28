#include <iostream>
#include <string>
using namespace std;

int main() {
	string pan;
	string rpan;
	int t;
	int count;
	cin>>t;
	
	for(int i=1;i<=t;i++){
	    count = 0;
	    cin>> pan;
	    //cout<<pancakes<<" "<<pancakes[3] << endl;
	    if(pan.size() != 1)
	    {
    	    for(int j=0;j<pan.size()-1;j++)
    	    {
    	        //cout<<j<<" "<<pan[0]<<endl;
    	        if(pan[j] != pan[j+1]){
    	           // pan.replace(0,j+1,pan[j+1]+"");
    	            count++;
    	           // j=0;
    	        }
    	    }
    	    if(pan[pan.size()-1]=='-') count++;
    	    cout<<"Case #"<<i<<": "<<count<<endl;
	    }else{
	        cout<<"Case #"<<i<<": "<<(pan[0]=='+'?0:1)<<endl;
	    }
	}
	return 0;
}
