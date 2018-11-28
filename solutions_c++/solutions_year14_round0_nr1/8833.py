#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

void getCardValue(int row, int cardLayout[][4]);
void printCardLayout(int cardLayout[][4]);
int findMatches(int arr[], int arr2[]);
int getChoice();

ifstream inFile;
int main(int argc, char** argv){
    int cardLayout[4][4];
    string infilename;
    if(argc > 1){
        infilename = argv[1];
    }
    else{
        infilename = "input.txt";
    }
    int numberOfTestCases;
    string svalue;
    string line;
    ofstream outFile;
    string outfilename = "output.txt";
    outFile.open(outfilename.c_str());
    inFile.open(infilename.c_str());
    if(inFile.is_open()){
        numberOfTestCases = getChoice();
        cout<<"numberOfTestCases: "<<numberOfTestCases<<"\n";
        for(int i = 0; i < numberOfTestCases; i++){
            int volunteerChoice = getChoice();
            cout<<"volunteerChoice: "<<volunteerChoice<<"\n";
            //get initial card layout
            for(int j = 0; j < 4; j++){
                getCardValue(j, cardLayout);
            }
            int arr[4];
            for(int j = 0; j < 4; j++){
                arr[j] = cardLayout[volunteerChoice-1][j];
                cout<<arr[j]<<"\n";
            }
            printCardLayout(cardLayout);
            int volunteerChoice2 = getChoice();
            cout<<"volunteerChoice: "<<volunteerChoice2<<"\n";
            //get second card layout
            for(int j = 0; j < 4; j++){
                getCardValue(j, cardLayout);
            }
            int arr2[4];
            for(int j = 0; j < 4; j++){
                arr2[j] = cardLayout[volunteerChoice2-1][j];
                cout<<arr2[j]<<"\n";
            }
            int result = findMatches(arr, arr2);
            if(result == -2){
                outFile << "Case #"<<i+1<<": Bad magician!\n";
            }
            else if(result == -1){
                outFile << "Case #"<<i+1<<": Volunteer cheated!\n";
            }
            else{
                outFile << "Case #"<<i+1<<": "<<result<<"\n";
            }
        }
    }
    inFile.close();
}

int findMatches(int arr[], int arr2[]){
    int value;
    int count = 0;
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            if(arr[i] == arr2[j]){
                count++;
                value = arr[i];
            }
        }
    }
    if(count == 0){
        return -1;
    }
    if(count == 1){
        return value;
    }
    if(count > 1){
        return -2;
    }
}


int getChoice(){
    string line;
    int volunteerChoice;
    if(getline(inFile, line)){
        istringstream ss(line);
        if(ss >> volunteerChoice){
            return volunteerChoice;
        }
        else{
        }
    }
    else{
        cout<<"error in input file\n";
    }
    return -1;
}




void getCardValue(int row, int cardLayout[][4]){
    string line;
    if(getline(inFile, line)){
        cout<<"current line: "<<line<<"\n";
        istringstream ss(line);
        for(int column = 0; column < 4; column++){
            if(ss >> cardLayout[row][column]){
            }
        }
    }
    else{
        cout<<"error in input file\n";
    }
}


void printCardLayout(int cardLayout[][4]){
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            cout<<cardLayout[i][j]<<" ";
        }
        cout<<"\n";
    }
}
