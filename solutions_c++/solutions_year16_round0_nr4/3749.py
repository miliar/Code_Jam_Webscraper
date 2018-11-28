#include<iostream>
#include<string.h>
using namespace std;
int main(){
	int T,K,C,S;
	cin>>T;
	for(int i=1;i<=T;i++){
		cin>>K>>C>>S;
		if(K-1>S){
			cout<<"case #"<<i<<":"<<" "<<"IMPOSSIBLE"<<endl;
		}
	    else
        {
            if(K==1)
                {
                cout<<"case #"<<i<<": 1"<<endl;
                continue;
            }
            if(C==1&&K==S){
	    	cout<<"case #"<<i<<":";
			for(int j=1;j<=K;j++){
				cout<<" "<<j;
			}
			cout<<endl;
		}
		else if(C==1&&(K-1)==S){
			cout<<"case #"<<i<<":"<<" "<<"IMPOSSIBLE"<<endl;
		}
		else if(C>=2)
		{   cout<<"case #"<<i<<":";
			for(int m=2;m<=K;m++)
			  cout<<" "<<m;
			  cout<<endl;
		}
        }
	}
	return 0;
}
