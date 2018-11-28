#include <iostream>
#include <fstream>
#include <set>
#include <utility>

using std::cout;    using std::set;         using std::ios;
using std::endl;    using std::ofstream;    using std::pair;
using std::ifstream;

set<int> readRow(ifstream &inputFile, int rowNumber);
int findCommon(set<int> &firstRowCards, set<int> &secondtRowCards);

const int num_rows = 4;
const int num_columns = 4;

int main(int argc, char* argv[]){
    if (argc != 3){
        cout << "usage: " << argv[0] << " INPUT_FILE OUTPUT_FILE" << endl;
        return -1;
    }

    ofstream outputFile(argv[2]);
    ifstream inputFile(argv[1]);

    int numCases = 0;

    inputFile >> numCases;
    
    for (int i = 0; i != numCases; i++){
        int selection = 0;
        inputFile >> selection;
        set<int> firstRowCards = readRow(inputFile, selection);

        inputFile >> selection;
        set<int> secondtRowCards = readRow(inputFile, selection);

        int card = findCommon(firstRowCards, secondtRowCards);
        

        if (card < 0){
            outputFile << "Case #" << i+1 << ": Volunteer cheated!" << endl;
        }
        else if (!card){
            outputFile << "Case #" << i+1 << ": Bad magician!" << endl;
        }
        else {
            outputFile << "Case #" << i+1 << ": " << card << endl;
        }


    }

    inputFile.close();
    outputFile.close();

    return 0;
}

/* Returns value of card if positive, 0 if "Bad magician!", or negative if 
 * "Volunteer cheated!"
 */
int findCommon(set<int> &firstRowCards, set<int> &secondtRowCards){
    int foundCard = -1; // default is volunteer cheated
    for (std::set<int>::iterator it=firstRowCards.begin(); 
            it!=firstRowCards.end(); ++it){
        if (!secondtRowCards.insert(*it).second){
            cout << *it;
            if (foundCard > 0){
                return 0; // bad magician
            }
            foundCard = *it;
        }
    }
    return foundCard;
}

set<int> readRow(ifstream &inputFile, int rowNumber){
    set<int> selectedRow;

    for (int i = 0; i != num_rows; i++){
        int cardsInRow[num_columns];
        for (int j = 0; j != num_columns; j++){
            inputFile >> cardsInRow[j];
        }
        if (i + 1 == rowNumber){
            selectedRow.insert(cardsInRow, cardsInRow + num_columns);
        }
    }
    return selectedRow;
}
