#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
	int T,CASES=1;
	

	ofstream output;
	output.open("output.out");
	ifstream input;
	input.open("A-small-attempt5.in");

	input>>T;
	while(CASES<=T){
		int first,second;
		int cnt[17]={};
		int cards[5][5]={};
		input>>first;
		int i,j;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++){
				input>>cards[i][j];
			}
		for(j=1;j<=4;j++)
			cnt[cards[first][j]]++;
		input>>second;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				input>>cards[i][j];
		for(j=1;j<=4;j++)
			cnt[cards[second][j]]++;
		int guess2=0,guess;
		for(i=1;i<=16;i++){
			if(cnt[i]==2){
				guess2++;
				guess=i;
			}
		}
		if(guess2==0)
			output<<"Case #"<<CASES<<": Volunteer cheated!\n";
		else if(guess2==1)
			output<<"Case #"<<CASES<<": "<<guess<<endl;
		else
			output<<"Case #"<<CASES<<": Bad magician!\n";
		CASES++;
	}
	output.close();
	input.close();
	return 0;
}