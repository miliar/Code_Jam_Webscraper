#include<iostream>
#include<fstream>
using namespace std;

int main(){
	int t;
	cin>>t;
	int n=1;
	ofstream myfile;
	myfile.open ("output.txt");
	if(t>=1 && t<=1000){
		while(t>0){
			int won=0;
			char board[4][4];
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					cin>>board[i][j];
				}
			}
			int count[10][3]={0};
			for(int i=0;i<4;i++){
				switch(board[i][i]){
				case 'X':
					count[0][0]++;
					break;
				case 'O':
					count[0][1]++;
					break;
				case 'T':
					count[0][2]++;
					break;
				}
			}
			for(int i=0;i<4;i++){
				switch(board[i][3-i]){
				case 'X':
					count[1][0]++;
					break;
				case 'O':
					count[1][1]++;
					break;
				case 'T':
					count[1][2]++;
					break;
				}
			}
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					switch(board[i][j]){
					case 'X':
						count[i+2][0]++;
						break;
					case 'O':
						count[i+2][1]++;
						break;
					case 'T':
						count[i+2][2]++;
						break;
					}
				}
			}
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					switch(board[j][i]){
					case 'X':
						count[i+6][0]++;
						break;
					case 'O':
						count[i+6][1]++;
						break;
					case 'T':
						count[i+6][2]++;
						break;
					}
				}
			}
			for(int i=0;i<10;i++){
				if(count[i][0]==4 || (count[i][2]+count[i][0])==4){
					myfile<<"Case #"<<n<<": X won"<<"\n";
					won=1;
					break;
				}
				else
				{
					if(count[i][1]==4 || (count[i][2]+count[i][1])==4){
						myfile<<"Case #"<<n<<": O won"<<"\n";
						won=1;
						break;
					}
				}
			}
			if(won==0){
				int sum=0;
				for(int i=0;i<4;i++){
					sum+=count[i+2][0]+count[i+2][1]+count[i+2][2];
				}
				if(sum==16){
					myfile<<"Case #"<<n<<": Draw"<<"\n";
				}
				else
				{
					myfile<<"Case #"<<n<<": Game has not completed"<<"\n";
				}
			}
			n++;
			t--;
		}
	}
	myfile.close();
	return 0;
}