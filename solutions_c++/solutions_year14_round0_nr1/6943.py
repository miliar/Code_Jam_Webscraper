//  Created by Lyamani Moulay Abdellatif on 13/04/13.
//  Copyright (c) 2013 Lyamani Moulay Abdellatif. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

#define LINESZ 1024
#define BadMagician "Bad magician!"
#define VolunteerCheated "Volunteer cheated!"

template <typename T>
struct matrix
{
    int col, row;
    std::vector<std::vector<T> > data;
    
    matrix(int columns, int rows) :
    col(columns), row(rows),
    data(col, std::vector<T>(row))
    {}
};

int main(int argc, const char * argv[])
{
    freopen("output.out","w", stdout);
    FILE* in = freopen("input.in","r", stdin);
    
    int test,cases;
    int row1 , row2 , a_ij;
    
    char str[LINESZ] ;
    
    cases=0;
    scanf("%d",&test);
    fgets (str, LINESZ, in) ;
    while (test){
        test--;
        cases++;
        
        scanf("%i", &row1) ;
        matrix<int> m(4, 4);
        for (int i = 0; i<4; i++) {
            for (int j = 0; j<4; j++) {
                scanf("%i", &a_ij) ;
                m.data[i][j] = a_ij;
            }
        }
        scanf("%i", &row2) ;
        matrix<int> m2(4, 4);
        for (int i = 0; i<4; i++) {
            for (int j = 0; j<4; j++) {
                scanf("%i", &a_ij) ;
                m2.data[i][j] = a_ij;
            }
        }
        

        int numberOfPossibleAnswers = 0;
        int possibleAnswerEventuelly = 0;
        for (int j = 0; j<4; j++) {
            int v = m.data[row1-1][j];
            for (int k = 0; k<4; k++) {
                if( v == m2.data[row2-1][k]){
                    possibleAnswerEventuelly = v;
                    numberOfPossibleAnswers++ ;
                }
            }
        }
        if(numberOfPossibleAnswers == 1)
            cout<<"Case #"<<cases<<": "<< possibleAnswerEventuelly   <<endl;
        if(numberOfPossibleAnswers == 0)
            cout<<"Case #"<<cases<<": "<< VolunteerCheated   <<endl;
        if(numberOfPossibleAnswers > 1)
            cout<<"Case #"<<cases<<": "<< BadMagician   <<endl;
        
    }
    return 0;
}

