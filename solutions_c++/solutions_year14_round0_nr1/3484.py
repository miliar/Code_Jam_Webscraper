#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int T;
	cin>>T;
	for(int x=1;x<=T;x++){
		int N;
		cin>>N;
		int ori[4],fin[4],t;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++){
				cin>>t;
				if(i== N-1)	ori[j]=t;
				}
		cin>>N;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++){
				cin>>t;
				if(i== N-1)	fin[j]=t;
				}
		int no=-1,c=0;
		for(int i =0;i<4;i++){
			for(int j =0;j<4;j++){
				if(ori[i] == fin[j]){
					no = ori[i];
					c++;
					}
				}
			}
		
		cout<<"Case #"<<x<<": ";
		if(c==1)	cout<<no;
		else if(c == 0)	cout<<"Volunteer cheated!";
		else	cout<<"Bad magician!";
		cout<<endl;
		
		}
	return 0;
	}
	
