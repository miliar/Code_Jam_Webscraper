#include <cstdio>
#include <iostream>
#include <fstream>
using namespace std;

int order1[4][4];
int order2[4][4];
char filename[] = "D:\\Users\\lenovo\\Desktop\\test.txt";
ofstream fout(filename,ios::app);
int main(){
	int N;
	cin>>N;
	for(int n=1;n<=N;n++){
		
		int row1,row2;
		cin>>row1;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>order1[i][j];
			}
		}
		cin>>row2;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>order2[i][j];
			}
		}
		int count=0;
		int result=-1;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(order1[row1-1][i]==order2[row2-1][j]){
					count++;
					result=order1[row1-1][i];
				}
			}
		}
		
		fout<<"Case #"<<n<<": ";
		cout<<"Case #"<<n<<": ";
		if(count==0){
			cout<<"Volunteer cheated!";
			fout<<"Volunteer cheated!";
		}else if(count==1){
			cout<<result;
			fout<<result;
		}else{
			cout<<"Bad magician!";
			fout<<"Bad magician!";
		}
		cout<<endl;
		fout<<endl;
	}
	return 0;
}