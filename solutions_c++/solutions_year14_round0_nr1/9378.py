
#include <iostream>
#include <stdio.h>
#include <fstream>

#define PrintAnswer 1
#define BadMagician 2
#define VolunteerCheated 3

using namespace std;
ofstream outfile;
void parseInput(int caseNo);

int main(int argc, const char * argv[])
{
    
    outfile.open("/Users/vivekshivam/Desktop/magicianTrick.txt");
    
    char ch;
    fstream fin("/Users/vivekshivam/Desktop/input.in", fstream::in);
    char *ch1 = new char[3];
    int startIndex = 0;
    int count = 0;
    int testCase = 0;
    // for testcase
    while (fin >> noskipws >> ch) {
        if(ch == ' ' || ch == '\n'){
            ch1[startIndex] = '\0';
            testCase = atoi(ch1);
            cout <<"testCase "<< testCase;
            break;
            delete [] ch1;
        }
        else{
            ch1[startIndex] = ch;
            startIndex++;
        }
    }
    

    int curCase = 0;
    for(int i = 0; i < testCase; i++){
        
        // answer 1
        fin >> noskipws >> ch;
        int answer1 = ch - '0';
        cout <<"\n answer1 "<< answer1;
        
        // enter
        fin >> noskipws >> ch;



        startIndex = 0;
        count = 0;
        char *ch2 = new char[3];
        int rowIndex = 1;
        int selRowNos[4];
        int selNosCount = 0;
        while (fin >> noskipws >> ch) {
            
            if(ch == ' ' || ch == '\n'){
                ch2[startIndex] = '\0';
                int val = atoi(ch2);
              //  cout <<"val "<< val;
                count++;
                if(rowIndex == answer1){
                    selRowNos[selNosCount] = val;
                    selNosCount++;
                }
                if(count % 4 == 0){
                    rowIndex++;
                }
                if(count == 16){
                    startIndex = 0;
                    delete [] ch2;
                    break;
                }
                startIndex = 0;
                delete [] ch2;
                ch2 = new char[3];
            }
            else{
                ch2[startIndex] = ch;
                startIndex++;
            }
        }
        
        // answer 2
        fin >> noskipws >> ch;
        int answer2 = ch - '0';
        cout <<"\n answer2 "<< answer2;
        
        // enter
        fin >> noskipws >> ch;

        
        startIndex = 0;
        count = 0;
        ch2 = new char[3];
        rowIndex = 1;
        selNosCount = 0;
        int noOfMatches = 0;
        int noFound = 0;
        while (fin >> noskipws >> ch) {
            
            if(ch == ' ' || ch == '\n'){
                ch2[startIndex] = '\0';
                int val = atoi(ch2);
           //     cout <<"val "<< val;
                count++;
                if(rowIndex == answer2){
                    for(int col = 0; col < 4; col++){
                        if(selRowNos[col] == val){
                            noOfMatches++;
                            noFound = val;
                        }
                    }
                }
                if(count % 4 == 0){
                    rowIndex++;
                }
                if(count == 16){
                    startIndex = 0;
                    delete [] ch2;
                    break;
                }
                startIndex = 0;
                delete [] ch2;
                ch2 = new char[3];
            }
            else{
                ch2[startIndex] = ch;
                startIndex++;
            }
        }
        
//        cout<<"\n answerFor "<<i <<" "<<noOfMatches;
        char *data = new char[100];
        if(noOfMatches > 1){
            cout<<"\n answerFor "<<i <<"Bad magician!";
            sprintf(data, "Case #%d: Bad magician!",(i+1));
        }
        else if(noOfMatches == 0){
            cout<<"\n answerFor "<<i <<" Volunteer cheated";
            sprintf(data, "Case #%d: Volunteer cheated!",(i+1));
        }
        else {
           cout<<"\n answerFor "<<i <<" "<< noFound;
            sprintf(data, "Case #%d: %d",(i+1),noFound);
        }
        outfile << data << endl;
        delete [] data;
    }
    outfile.close();
    return 0;
    int N = 0;
    cin >> N;
    cout<<"\n NoOfCases %d"<<N;

    int carArr[4][4];
    int carArr1[4][4];
    for(int i = 0; i < N; i++) {
        parseInput(i);
    }
    /*
    for(int i = 0; i < 0; i++) {
        
        int *volunteerAns =  new int[2];
        cout<<"\n caseNo %d "<< i;
        int *noInSelectedRow = new int[4];
        // arr1
        cin >> volunteerAns[0];
         cout<<"\n volunteerAns[0] %d "<< volunteerAns[0];
        
        int noCount = 0;
        for(int r = 0; r < 4; r++){
            for(int c = 0; c < 4; c++){
                cin >> carArr[r][c];
                if( (r + 1) == volunteerAns[0]){
                    noInSelectedRow[noCount] = carArr[r][c];
                    noCount++;
                }
            }
        }
        
        // arr2
        cin >> volunteerAns[1];
        cout<<"\n volunteerAns[1]t %d "<< volunteerAns[1];
        for(int r = 0; r < 4; r++){
            for(int c = 0; c < 4; c++){
                cin >> carArr1[r][c];
            }
        }
        
        int r = volunteerAns[1] - 1;
        bool isNormal = true;
        int noOfMatches = 0;
        int selectedNo = -1;
        for(int c = 0; c < 4 && isNormal; c++){
            // check for noOfMatches
            for(int l = 0; l < 4; l++){
                if(noInSelectedRow[l] == carArr1[r][c]){
                    noOfMatches++;
                    selectedNo = carArr1[r][c];
                }
            }
        }
        if(noOfMatches > 1) { //Bad Magician
            caseAnswers[i] = -1;
        }
        else if(noOfMatches == 0) { //Volunteer Cheates
            caseAnswers[i] = -2;
        }
        else if(noOfMatches == 1) { //PrintAnswer
            caseAnswers[i] = selectedNo;
        }
        delete [] noInSelectedRow;
        delete [] volunteerAns;
    }
    
    for(int i = 0; i < 0; i++){
       cout<<"\n answerFor %d"<<i;
        char *data = new char[100];
        if(caseAnswers[i] == -1){
            sprintf(data, "Case #%d: Bad magician!",(i+1));
        }
        else if(caseAnswers[i] == -2){
            sprintf(data, "Case #%d: Volunteer cheated!",(i+1));
        }
        else {
            sprintf(data, "Case #%d: %d",(i+1),caseAnswers[i]);
        }
        outfile << data << endl;
        delete [] data;
    }
     */
    
    return 0;
}

void parseInput(int caseNo){
    int caseAnswers = 0;
    int carArr[4][4];
    int carArr1[4][4];
    int  i = caseNo;
    
    int *volunteerAns =  new int[2];
    cout<<"\n caseNo %d "<< i;
    int *noInSelectedRow = new int[4];
    // arr1
    cin >> volunteerAns[0];
    cout<<"\n volunteerAns[0] %d "<< volunteerAns[0];
    
    int noCount = 0;
    for(int r = 0; r < 4; r++){
        for(int c = 0; c < 4; c++){
            cin >> carArr[r][c];
            if( (r + 1) == volunteerAns[0]){
                noInSelectedRow[noCount] = carArr[r][c];
                noCount++;
            }
        }
    }
    
    // arr2
    cin >> volunteerAns[1];
    cout<<"\n volunteerAns[1]t %d "<< volunteerAns[1];
    for(int r = 0; r < 4; r++){
        for(int c = 0; c < 4; c++){
            cin >> carArr1[r][c];
        }
    }
    
    int r = volunteerAns[1] - 1;
    bool isNormal = true;
    int noOfMatches = 0;
    int selectedNo = -1;
    for(int c = 0; c < 4 && isNormal; c++){
        // check for noOfMatches
        for(int l = 0; l < 4; l++){
            if(noInSelectedRow[l] == carArr1[r][c]){
                noOfMatches++;
                selectedNo = carArr1[r][c];
            }
        }
    }
    if(noOfMatches > 1) { //Bad Magician
        caseAnswers = -1;
    }
    else if(noOfMatches == 0) { //Volunteer Cheates
        caseAnswers = -2;
    }
    else if(noOfMatches == 1) { //PrintAnswer
        caseAnswers = selectedNo;
    }
    delete [] noInSelectedRow;
    delete [] volunteerAns;
    
    cout<<"\n answerFor %d"<<i;
    char *data = new char[100];
    if(caseAnswers == -1){
        sprintf(data, "Case #%d: Bad magician!",(i+1));
    }
    else if(caseAnswers == -2){
        sprintf(data, "Case #%d: Volunteer cheated!",(i+1));
    }
    else {
        sprintf(data, "Case #%d: %d",(i+1),caseAnswers);
    }
    outfile << data << endl;
    delete [] data;

}
