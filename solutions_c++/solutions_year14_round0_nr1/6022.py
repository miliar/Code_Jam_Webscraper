#include <iostream>
#include <vector>

int main(int argc, char ** argv){
    int n; std::cin>>n;
    for (unsigned int i = 0; i < n ; i++) {
        
        unsigned int first_row; std::cin>>first_row; first_row--;
        unsigned int first_card[16];
        for (unsigned int j = 0; j < 16; j++) std::cin>> first_card[j];
        
        unsigned int first_choice[4];
        for (unsigned int j = 0; j < 4; j++) first_choice[j] = first_card[4 * first_row + j];
        
        unsigned int second_row; std::cin>>second_row; second_row--;
        unsigned int second_card[16];
        for (unsigned int j = 0; j < 16; j++) std::cin>> second_card[j];
        
        unsigned int second_choice[4];
        for (unsigned int j = 0; j < 4; j++) second_choice[j] = second_card[4 * second_row + j];
        
        int duplicate = 0;
        int select = 0;
        for (unsigned int j = 0; j < 4; j++) {
            for (unsigned int q = 0; q < 4; q++) {
                if (first_choice[j] == second_choice[q]) {
                    duplicate++;
                    select = first_choice[j];
                }
            }
        }
        
        if (duplicate == 0) std::cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
        else if(duplicate == 1) std::cout<<"Case #"<<i+1<<": "<<select<<std::endl;
        else std::cout<<"Case #"<<i+1<<": Bad magician!\n";
    }
    
    return 0;
}