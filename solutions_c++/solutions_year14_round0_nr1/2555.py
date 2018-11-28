#include<iostream>
using namespace std;

int main(void){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("smallOutputA.txt", "w", stdout);
	int T; cin>>T;
	for(int tc=1;tc<=T;tc++){
		cout<<"case #"<<tc<<": ";
		int selRow=-1;int cards[17]={0,};
		cin>>selRow;
		
		for(int i=1;i<=16;i++){
			int card;
			cin>>card;
			if(i > (selRow-1)*4 && i <= selRow*4)
				cards[card] ++;
		}
		cin>>selRow;
		for(int i=1;i<=16;i++){
			int card;
			cin>>card;
			if(i > (selRow-1)*4 && i <= selRow*4)
				cards[card] ++;
		}
		bool occured = false; int i=1; int num; bool found = false;
		for(;i<=16;i++){	 
			if(cards[i] == 2){
				if(occured == true){
					cout<<"Bad magician!"; found = false;
					break;
				}
				else{
					num = i;
					occured = true ; found = true;
				}
			}
		}
		if( occured == false){
			cout<<"Volunteer cheated!";
		}
		else if(found == true ) 
			cout<<num;

		cout<<'\n';
	}
	fclose(stdin); fclose(stdout);
}
