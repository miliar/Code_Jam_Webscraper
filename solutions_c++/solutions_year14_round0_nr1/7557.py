#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input("A-small-attempt1.in");
    ofstream output("output.out");
    int first[4], second[4];
    int first_row, second_row;
    int num_case;
    
    input >> num_case;
    
    for(int i=0; i<num_case; i++){
        input >> first_row;
        for(int j=0; j<4; j++){
            int temp;
            if(j+1==first_row){
                for(int k=0; k<4; k++){
                    input >> first[k];
                }
            } else 
                for(int k=0; k<4; k++){
                    input >> temp;
                }
        }
        input >> second_row;
        
        for(int j=0; j<4; j++){
            int temp;
            if(j+1==second_row){
                for(int k=0; k<4; k++)
                    input >> second[k];
            } else
                for(int k=0; k<4; k++){
                    input >> temp;
                }
        }
        
        int match=0;
        int found=0;
        
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++)
                if(first[j] == second[k]){
                    match++;
                    found = j;
                }
        }
        
        output << "Case #" << i+1 << ": ";
        if(match==0)
            output << "Volunteer cheated!";
        else if (match > 1)
            output << "Bad magician!";
        else
            output << first[found];
        output << endl;
    }
    
    
    return 0;
}

