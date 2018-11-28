#include <iostream>
#include <fstream>
using namespace std;

int tests,chosen_row,numbers,chosen_number,cards[7][7],answer,possible_cards[7];
ifstream input("input.txt");
fstream output("output.txt");

void magic(){
input >> tests;
for(int i=0;i<tests;i++){
answer = 0;
    input >> chosen_row;
    for(int j=1;j<5;j++){
        for(int k=1;k<5;k++){
            input >> cards[j][k];
            }}

for(int l=1;l<5;l++){
    possible_cards[l]=cards[chosen_row][l];
}

input >> chosen_row;
for(int j=1;j<5;j++){
    for(int k=1;k<5;k++){
        input >> cards[j][k];
        }}

for(int j=1;j<5;j++){
    for(int k=1;k<5;k++){
           if(possible_cards[j]==cards[chosen_row][k]){
                answer++;
                chosen_number = possible_cards[j];
                }}}

if(answer==0)output<<"Case #"<<i+1<<": " << "Volunteer cheated!" << "\n";
if(answer==1)output<<"Case #"<<i+1<<": " << chosen_number << "\n";
if(answer>1) output<<"Case #"<<i+1<<": " << "Bad magician!" << "\n";
}}

int main(){
magic();
return 0;
}
