#include <iostream>
#include <vector>
#define MAX 4
#include <fstream>

using namespace std;

typedef int Array[MAX][MAX];


int main(){
ifstream input("A-small-attempt3.in") ;
ofstream output("A-small-attempt3.out") ;
int nbrCas(0);
    input>>nbrCas; //number of cases
    for(int k(0); k<nbrCas; k++){
        int answer1;
        input>>answer1;
        Array arr1;


        for(int i(0); i<MAX; i++){
            for(int j(0); j<MAX; j++){
                input>>arr1[i][j];
            }
        }
        int answer2;
        vector <int> result;
        int possibleCases(0);

        input>>answer2;
        Array arr2;


        for(int i(0); i<MAX; i++){
            for(int j(0); j<MAX; j++){
                input>>arr2[i][j];
            }
        }

            for(int i(0); i<MAX; i++){
                for(int j(0); j<MAX; j++){
                    if(arr1[answer1-1][i]==arr2[answer2-1][j]){
                        possibleCases++;
                        result.push_back(arr1[answer1-1][i]);
                    }
                }
            }



        if(possibleCases ==0)
            output<<"Case #"<<k+1<<": "<<"Volunteer cheated!";
        else if(possibleCases==1)
            output<<"Case #"<<k+1<<": "<<result[0];
        else if(possibleCases>1)
            output<<"Case #"<<k+1<<": "<<"Bad magician!";

        if(k != nbrCas-1)
            output<<endl;

    }




}

