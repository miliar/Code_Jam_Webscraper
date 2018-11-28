#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
using namespace std;
#include <stdio.h>
#include <cstdio>

int jugdeMagic(int turn);

int main(){
   int i,T;
   int results[1000];
   scanf("%d",&T);
   
   for(i=1; i<T+1;i++){
	   results[i] = jugdeMagic(i+1);
   }

   for(i=1; i<T+1;i++){
	   if(results[i]==0)cout << "Case #"<<i<<": " << "Volunteer cheated!" << endl;
	   else if(results[i]==-1)cout << "Case #"<<i<<": " << "Bad magician!" << endl;
	   else cout << "Case #"<<i<<": " << results[i] << endl;
   }

   system("pause");
   return 0;
}


/*Returns card number. -1 if bad magician, 0 if cheating volunteer*/
int jugdeMagic(int turn){
	int i, j, row1, row2;
	int table1[4][4];
	int table2[4][4];

	/*Input all the info*/
	cin >> row1;
	for(i=0; i<4; i++)
		for(j=0; j<4; j++)
			cin >> table1[i][j];
	cin >> row2;
	for(i=0; i<4; i++)
		for(j=0; j<4; j++)
			cin >> table2[i][j];

	/*Which card was chosen? Or are thr multiple answers?*/
	int chosen_card = 0; //if 0 after for loop then volunteer cheated
	int multiple_answers = 0; //if 1 after for loop magician is stupid
	for(i=0; i<4; i++){
		for(j=0; j<4; j++){
			if(table1[row1-1][i] == table2[row2-1][j]){
				if(chosen_card != 0) multiple_answers = 1;
				else chosen_card = table1[row1-1][i];
			}
		}
	}

	/*Display answer*/
	string message;
	if(chosen_card!=0 && multiple_answers==0)
		return chosen_card;//cout << "Case #"<<turn<<": " << chosen_card << endl;
	else{
		if(chosen_card == 0) return 0;//cout << "Case #"<<turn<<": " << "Volunteer cheated!" << endl;
		else return -1;//cout << "Case #"<<turn<<": " << "Bad magician!" << endl;
	}

}