#include <iostream>
#include <fstream>

using namespace std;

static int first_cards[4][4] = {0, };
static int second_cards[4][4] = {0, };

void InitCard(){
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			first_cards[i][j]=0;
			second_cards[i][j]=0;
		}
	}
}

int main(void){
	int T=0, caseCnt=0;
	fstream fin("in.txt", fstream::in);
	fstream fout("out.txt", fstream::out);


	fin>>T;

	while(caseCnt<T){
		int A1=0, A2=0;
		int cand[4] = {0, };
		int cand_count=0;

		fin>>A1;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				fin>>first_cards[i][j];
		fin>>A2;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				fin>>second_cards[i][j];

		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if(first_cards[A1-1][i]==second_cards[A2-1][j])
					cand[cand_count++] = second_cards[A2-1][j];
			}
		}
		if(cand_count==1){
			fout<<"Case #"<<caseCnt+1<<": "<<cand[0]<<endl;
		}else if(cand_count>1){
			fout<<"Case #"<<caseCnt+1<<": "<<"Bad magician!"<<endl;
		}else{
			fout<<"Case #"<<caseCnt+1<<": "<<"Volunteer cheated!"<<endl;
		}

		caseCnt++;
	}
	return 0;
}