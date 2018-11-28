#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
#include<iostream>
#include<vector>
#include<fstream>
using namespace std;


int main(){
READ("A-small-attempt2.in");
  WRITE("A-small-attempt2.out");
    vector<int>myvector1;
    vector<int>myvector2;
    vector<int>myvector3;
    int array[4][4];
    int num,first,second;
    cin>>num;
    for(int k=0;k<num;k++){
    cin>>first;
    for(int i=0;i<4;i++){
    	for(int j=0;j<4;j++){
    	cin>>array[i][j];
		if(i==first-1)
		myvector1.push_back(array[i][j]);
		}
    }
	
    //cout<<"sssssssssssss\n";
	cin>>second;
	for(int i=0;i<4;i++){
    	for(int j=0;j<4;j++){
    	cin>>array[i][j];if(i==second-1)
		myvector2.push_back(array[i][j]);
		}
    }
	for(int i=0;i<4;i++){
    	for(int j=0;j<4;j++){
    		if(myvector1[i]==myvector2[j])
    		myvector3.push_back(myvector1[i]);
	}
}
if(myvector3.size()==0)
	cout<<"Case #"<<k+1<<": "<<"Volunteer cheated!\n";
	else if(myvector3.size()==1)
	cout<<"Case #"<<k+1<<": "<<myvector3[0]<<endl;
	else cout<<"Case #"<<k+1<<": "<<"Bad magician!\n";
myvector1.clear();
myvector2.clear();
myvector3.clear();
}

}
