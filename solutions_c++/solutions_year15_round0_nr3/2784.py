#include <iostream>
//#include <fstream>
//#include <string>
//#include <sstream>
//#include <stdio.h>
//#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

int sign(int i){
    if (i >= 0) return 1;
    else return -1;
}

int multiply(int i, int j, vector<vector<int> > &multiplications){
    return sign(i)*sign(j)*multiplications[abs(i)][abs(j)];
}

int reverseMultiply(int i, int j, vector<vector<int> > &multiplications){
    return sign(i)*sign(j)*multiplications[abs(j)][abs(i)];
}

vector<int> multiplicationsRange(int start, int end, vector<int> &values, vector<vector<int> > &multiplications){
    vector<int> multiplicationsToPoint;
    multiplicationsToPoint.push_back(values[start]);
    for(int j = start + 1; j < end; j++){
        multiplicationsToPoint.push_back(multiply(multiplicationsToPoint[j-start-1], values[j], multiplications));
    }
    return multiplicationsToPoint;
}

vector<int> reverseMultiplicationsRange(int start, int end, vector<int> &values, vector<vector<int> > &multiplications){
    vector<int> multiplicationsToPoint;
    multiplicationsToPoint.push_back(values[start]);
    for(int j = start + 1; j < end; j++){
        multiplicationsToPoint.push_back(reverseMultiply(multiplicationsToPoint[j-start-1], values[j], multiplications));
    }
    return multiplicationsToPoint;
}

bool checkBetweenIK(vector<int> &iPosPlaces, vector<int> &kPosPlaces, vector<vector<int> > &multiplications, vector<int> &lettersTransformed){
    for(int i = 0; i < iPosPlaces.size(); ++i){
        int iPos = iPosPlaces[i];
        if(kPosPlaces.size() > 0){
            int lastKPos = kPosPlaces[0];
            if(lastKPos > iPos + 1){
                vector<int> mult = multiplicationsRange(iPos + 1, lastKPos, lettersTransformed, multiplications);
                vector<int> jPosPlaces;
                for(int j = 0; j < mult.size(); j++){
                    if(mult[j] == 3) jPosPlaces.push_back(j + iPos + 1);
                }
                for(int k = 0; k < kPosPlaces.size(); ++k){
                    int kPos = kPosPlaces[k];
                    for(int j = 0; j < jPosPlaces.size(); ++j){
                        int jPos = jPosPlaces[j];
                        if (kPos == jPos+1) return true;
                    }
                }
            }
        }
    }
    return false;
}

void print(vector<int> &vectorName){
    for(int j = 0; j < vectorName.size(); j++){
        cout << vectorName[j] << " ";
    }
    cout << '\n';
}

int main(){
    ofstream fout ("output.out");
    ifstream fin ("C-small-attempt2.in");

    vector<int> rowminusone;
    rowminusone.push_back(0);
    rowminusone.push_back(0);
    rowminusone.push_back(0);
    rowminusone.push_back(0);
    rowminusone.push_back(0);
    vector<int> row0;
    row0.push_back(0);
    row0.push_back(1);
    row0.push_back(2);
    row0.push_back(3);
    row0.push_back(4);
    vector<int> row1;
    row1.push_back(0);
    row1.push_back(2);
    row1.push_back(-1);
    row1.push_back(4);
    row1.push_back(-3);
    vector<int> row2;
    row2.push_back(0);
    row2.push_back(3);
    row2.push_back(-4);
    row2.push_back(-1);
    row2.push_back(2);
    vector<int> row3;
    row3.push_back(0);
    row3.push_back(4);
    row3.push_back(3);
    row3.push_back(-2);
    row3.push_back(-1);

    vector<vector<int> > multiplications;
    multiplications.push_back(rowminusone);
    multiplications.push_back(row0);
    multiplications.push_back(row1);
    multiplications.push_back(row2);
    multiplications.push_back(row3);

    int numTests;
    fin >> numTests;

    for (int i = 0; i < numTests; ++i){
        cout << "Run " << i + 1 << '\n';
        int length, repeats;
        fin >> length >> repeats;
        string letters;
        fin >> letters;

        int total_length = length*repeats;

        bool win = false;

        if(total_length >= 3 && length > 1){
            vector<int> lettersTransformed;
            for(int r = 0; r < repeats; r++){
                for(int j = 0; j < length; j++){
                    if(letters[j] == 'i') lettersTransformed.push_back(2);
                    else if(letters[j] == 'j') lettersTransformed.push_back(3);
                    else lettersTransformed.push_back(4);
                }
            }
            vector<int> copyLetters = lettersTransformed;
            reverse(copyLetters.begin(), copyLetters.end());

            vector<int> wholeMultiplied = multiplicationsRange(0, total_length, lettersTransformed, multiplications);
            vector<int> reverseMultiplied = reverseMultiplicationsRange(0, total_length, copyLetters, multiplications);

            vector<int> iPosPlaces;
            for(int j = 0; j < total_length; j++){
                if(wholeMultiplied[j] == 2) iPosPlaces.push_back(j);
            }
            vector<int> kPosPlaces;
            for(int j = 0; j < total_length; j++){
                if(reverseMultiplied[j] == 4) kPosPlaces.push_back(total_length-j-1);
            }

        //print(iPosPlaces);
        //print(kPosPlaces);


            win = checkBetweenIK(iPosPlaces, kPosPlaces, multiplications, lettersTransformed);
        }
        /*
        int iPos = 0;
        if(total_length >= 3 && length > 1){
            while(!win && iPos < total_length - 2){
                if(wholeMultiplied[iPos] == 2){
                    vector<int> subMultiplied = multiplicationsRange(iPos + 1, total_length, lettersTransformed, multiplications);
                    int jPos = 0;
                    while(!win && jPos + iPos < total_length - 1){
                        if(subMultiplied[jPos] == 3){
                            vector<int> finalMultiplication = multiplicationsRange(jPos + iPos + 2, total_length, lettersTransformed, multiplications);
                            if(finalMultiplication[finalMultiplication.size()-1] == 4) win = true;
                        }
                        jPos++;
                    }
                }
                iPos++;
            }
        }
        */

        if(win) fout << "Case #" << (i+1) << ": " << "YES" << "\n";
        else fout << "Case #" << (i+1) << ": " << "NO" << "\n";
    }
    return 0;
}
