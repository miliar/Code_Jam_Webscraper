#include<iostream>
#include<string>
#include<fstream>
using namespace std;
ofstream fout("out.txt");
int main(){
	int caseNum;
	cin>>caseNum;
	for(int i=1;i<=caseNum;i++){
		int m,n;
		int a[4][4];
		int b[4][4];
		cin>>m;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++)
				cin>>a[j][k];
		}
		cin>>n;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++)
				cin>>b[j][k];
		}
		int count = 0;
		int num=-1;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(a[m-1][j]==b[n-1][k]){
					count++;
					num = a[m-1][j];
				}
			}
		}
		if(count==1){
			fout<<"Case #"<<i<<": "<<num<<endl;
		}else if(count>1){
			fout<<"Case #"<<i<<": Bad magician!"<<endl;
		}else
			fout<<"Case #"<<i<<": Volunteer cheated!"<<endl;

	}
}