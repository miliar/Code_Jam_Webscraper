#include<iostream>
/*
the magician tries to put all the cards in the row of the 1st question in different rows for the 2nd question

bad job: 2 of the cards in one row

cheat: none of the cards in that row
*/
using std::cin;using std::cout;using std::endl;
int main() {
short numTestCases;
cin>>numTestCases;
for (char i=0; i!=numTestCases;++i) {

//1-indexed
short answer1;
cin >> answer1;
short arrang1[16];
for (char j=0; j!=16;++j) cin >> arrang1[j];

short answer2;
cin >> answer2;
short arrang2[16];
for (char j=0; j!=16;++j) cin >> arrang2[j];

char numA1CardsInA2Row=0;
short lastFind = 0;
for (char j=(answer1-1)*4; j != (answer1)*4; ++j) {
for (char k=(answer2-1)*4; k != answer2*4; ++k) {
if (arrang1[j]==arrang2[k]) { ++numA1CardsInA2Row; lastFind = arrang1[j];}
}
}

cout << "Case #"<<(i+1)<<": ";
switch (numA1CardsInA2Row) {
case 0:
cout << "Volunteer cheated!"; break;
case 1:
cout << lastFind; break;
default:
cout << "Bad magician!"; break;
}
cout << endl;

}
}
