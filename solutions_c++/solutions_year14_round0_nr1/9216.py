#include <iostream>
#include <stdio.h>

using namespace std;

int mat1[4][4];
int mat2[4][4];

int main(int argc, char *argv[]){
    int T;
    int choice1;
    int choice2;
    int resposta;

    cin>>T;

    for (int w=0; w<T; w++){
            cin>>choice1;
            choice1--;

            for (int i=0; i<4; i++){
                for (int j=0; j<4; j++){
                    cin>>mat1[i][j];
                }
            }

            cin>>choice2;
            choice2--;

            for (int i=0; i<4; i++){
                for (int j=0; j<4; j++){
                    cin>>mat2[i][j];
                }
            }

            int cont = 0;
            for (int i=0; i<4;i++){
                for (int j=0; j<4;j++){
                    if(mat1[choice1][i] == mat2[choice2][j]){
                        cont++;
                        resposta = mat1[choice1][i];
                        if (cont>1){
                            resposta=999;
                        }

                    }
                    else if(cont==0){
                            resposta=888;
                    }

                }
            }


            cout<<"Case #"<<w+1<<": ";
            if (resposta==999)
                cout<<"Bad magician!"<<endl;
            else if(resposta==888)
                cout<<"Volunteer cheated!"<<endl;
            else
                cout<<resposta<<endl;



    }

}

/*
Input

The first line of the input gives the number of test cases, T. T test cases follow.
Each test case starts with a line containing an integer: the answer to the first question.
The next 4 lines represent the first arrangement of the cards: each contains 4 integers, separated by a single space.
The next line contains the answer to the second question, and the following four lines contain the second arrangement in the same format.

Output

For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1).

If there is a single card the volunteer could have chosen, y should be the number on the card. If there are multiple cards the volunteer could have chosen, y should be "Bad magician!", without the quotes. If there are no cards consistent with the volunteer's answers, y should be "Volunteer cheated!", without the quotes. The text needs to be exactly right, so consider copying/pasting it from here.

Limits

1 ≤ T ≤ 100.
1 ≤ both answers ≤ 4.
Each number from 1 to 16 will appear exactly once in each arrangement.

Sample


Input

Output
             //4x4 com cartas
3            //number of test cases T
2            //answer to first question - posicao da carta
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
***********************  Case #1: 7


2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
***************************   Case #2: Bad magician!


2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

***************************  Case #3: Volunteer cheated!



3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16



*/
