#include <iostream>
#include<fstream>
using namespace std;

int main()
{
    int cases,answer1,answer2;
    fstream fin;
    fin.open("/Users/Bob/Desktop/Google/Google/in.txt");
    fin>>cases;
    
    int output[cases];
    int count[cases];
    for (int i = 0;i<cases;i++) {
        output[i] = 0;
        count[i] = 0;
    }
    
    
    for(int l = 0; l<cases; l++) {
        
        //Round 1
        fin>>answer1;
        int number1[4][4];
        
        for(int i=0;i<4;++i) {
            for(int j = 0; j<4; j++) {
                fin>>number1[i][j];
            }
        }
        
        //Round 2
        fin>>answer2;
        int number2[4][4];
        
        for(int i=0;i<4;++i) {
            for(int j = 0; j<4; j++) {
                fin>>number2[i][j];
            }
        }
        
        for(int i = 0; i<4;i++) {
            for (int j = 0;j<4;j++) {
                if(number1[answer1-1][i] == number2[answer2-1][j]) {
                    output[l] = number1[answer1-1][i];
                    count[l]++;
                }
            }
        }
        //cout<<endl;
    }
    
    // Output
    for(int i = 1;i<cases+1;i++) {
        if(count[i-1]==1)
            printf("Case #%d: %d",i,output[i-1]);
        else if(count[i-1]==0)
            printf("Case #%d: Volunteer cheated!",i);
        else
            printf("Case #%d: Bad magician!",i);
        cout<<endl;
    }
    
    return 0;
}

