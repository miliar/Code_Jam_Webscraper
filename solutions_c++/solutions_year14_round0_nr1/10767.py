#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int firstGridCards[4][4];
int secondGridCards[4][4];

int cases = 0;
int n = 0;
int firstRowSelected = 0;
int secondRowSelected = 0;


int main(){
int lineCards;
int cardCorrect = 0;
int cardCorrect_answer = 0;
cin >> cases;
//cout<< "Numero de casos " <<cases<<endl;
	while (n < cases) {
	    //cout << "n = "<< n<<endl;
	    cin >> firstRowSelected;
	    for(int i = 0; i< 4; i++){
	        for (int j = 0; j < 4; j ++){
	            cin>>lineCards;
	            //cout<<lineCards<<endl;
	            firstGridCards[i][j] = lineCards;
	        }
            //cout<<firstGridCards[i][0]<<" "<<firstGridCards[i][1]<<" "<<firstGridCards[i][2]<<" "<<firstGridCards[i][3]<<endl;	       
	    }
	    
	    cin >> secondRowSelected;
	    for(int i = 0; i< 4; i++){
	        for (int j = 0; j < 4; j ++){
	            cin>>lineCards;
	            secondGridCards[i][j] = lineCards;
	        }
	    }
	   // cout << "primeira linha "<<firstRowSelected<<endl;
	    //cout << "segunda linha "<<secondRowSelected<<endl;
	    for(int k = 0; k < 4; k++){
	        for(int y = 0; y < 4; y++){
	            //cout << "numero da primeiro grid "<<firstGridCards[firstRowSelected-1][k]<< " numero do segundo grid "<<secondGridCards[secondRowSelected-1][y]<<endl;
	            if(firstGridCards[firstRowSelected-1][k] == secondGridCards[secondRowSelected-1][y]){
                    cardCorrect++;
                    cardCorrect_answer = firstGridCards[firstRowSelected-1][k];
                }
            }
        }
        //cout << "cardCorrect " <<cardCorrect<< endl;
        if (cardCorrect == 0){
            cout <<"Case #"<<n+1<<": "<< "Volunteer cheated!"<<endl;
        }else if (cardCorrect > 1) {
            cout << "Case #"<<n+1<<": "<< "Bad magician!"<<endl;
        }else if(cardCorrect == 1){
            cout << "Case #"<<n+1<<": "<< cardCorrect_answer<<endl;
        }
        for(int m=0; m < 4; m++){
            for(int n = 0; n < 4; n++){
                firstGridCards[m][n] = 0;
                secondGridCards[m][n] = 0;
            }
       }
       firstRowSelected = 0;
       secondRowSelected = 0;
       lineCards = 0;
       cardCorrect = 0;
       cardCorrect_answer = 0;
       n++;
    }
}    

     
	 

