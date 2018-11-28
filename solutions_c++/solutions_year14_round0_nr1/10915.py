#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    freopen("/home/amr/Downloads/A-small-attempt2.in","r",stdin); // For reading input
    freopen("/home/amr/Downloads/output.txt","w",stdout); // for writing output
    int tCases, firstRow,secondRow;
    string firstArrang[16];
    string secondArrang[16];
    int count;
    int row1,row2;
    string card;
    string *output;

    cin >> tCases;  //reads the no. of test cases

    output = new string[tCases];

    for(int j=0; j<tCases; j++){
        count =0;
        cin >> firstRow; //the 1st answer of the player

        switch(firstRow)
        {
        case 1: row1 = 0; break;
        case 2: row1 = 4; break;
        case 3: row1 = 8; break;
        case 4: row1 = 12; break;
        }

      for (int i =0; i<16; i++){ //the 1st arrangement of the magician
            cin >> firstArrang[i];
        }



        cin >> secondRow; //the 2nd answer of the player

        switch(secondRow)
        {
        case 1: row2 = 0; break;
        case 2: row2 = 4; break;
        case 3: row2 = 8; break;
        case 4: row2 = 12; break;
        }
        for (int i =0; i<16; i++){ //the 2nd arrangement of the magician
            cin >> secondArrang[i];
        }


        for(int n =row1 ;n < row1+4; n++){
            for(int k = row2; k< row2+4; k++){

                 if(firstArrang[n] == secondArrang[k])
                {
                     card = firstArrang[n];
                     count ++;
                 }
            }
        }


        if(count == 0)
         output[j] = "Volunteer cheated!";
     else if(count == 1)
         output[j]= card;
     else
         output[j]= "Bad magician!";
    }

    for(int j=0; j<tCases; j++){
        cout << "Case #"<< j+1 << ": " << output[j] << endl;
    }


    return 0;
}

