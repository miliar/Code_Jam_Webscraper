#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

int main(){
	ifstream cin("A-small-attempt0.in");
	ofstream out("bbb.txt");
	int T,a,b,cases=1;
	int card1[4][4],card2[4][4];
	cin>>T;
	while(T--){
		int rec[17]={0};
		cin>>a;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>card1[i][j];
			}
		}
		cin>>b;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>card2[i][j];
			}
		}
		for(int i=0;i<4;i++){
			rec[card1[a-1][i]]=1;
		}
		int count=0,record=-1;
		for(int i=0;i<4;i++){
			if(rec[card2[b-1][i]]==1){
				count++;
				record = card2[b-1][i];
			}
		}
		if(count==0){
			out<<"Case #"<<cases++<<": Volunteer cheated!"<<endl;
		}else if(count==1){
			out<<"Case #"<<cases++<<": "<<record<<endl;
		}else{
			out<<"Case #"<<cases++<<": Bad magician!"<<endl;
		}

	}
}