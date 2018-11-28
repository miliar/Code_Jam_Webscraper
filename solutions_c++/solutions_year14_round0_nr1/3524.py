/*
 * main.cpp
 *
 *  Created on: 12.04.2014
 *      Author: Stefan
 */


/*
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

pick:11

3

3 10 8 1
2 16 4 14
15 9 5 13
11 6 12 7

4

=> compare 9, 10, 11, 12 with 11, 6, 12, 7
=> 11 or 12
*/
#include <fstream>
#include <iostream>

int main() {
	std::ifstream infile("input.txt");
	std::ofstream outfile("output.txt");
    int inputs, pick1, pick2, garbage;
    infile>>inputs;
    int* row1=new int[4];
    int* row2=new int[4];
    int counter=1;
    while(inputs>0){
        infile>>pick1;
        --pick1;
        for(int i=0; i<4; ++i){
            for(int j=0; j<4; ++j){
                if(i==pick1){
                    infile>>row1[j];
                    std::cout<<row1[j]<<", ";
                } else{
                    infile>>garbage;
                }
            }
        }
        infile>>pick2;
        --pick2;

        for(int i=0; i<4; ++i){
            for(int j=0; j<4; ++j){
                if(i==pick2){
                    infile>>row2[j];
                    std::cout<<row2[j]<<", ";
                } else {
                    infile>>garbage;
                }
            }

        }

        int out=0;

        for(int i=0; i<4; ++i){
            for(int j=0; j<4; ++j){
                std::cout<<row1[i]<<", "<<row2[j]<<"\n";
                if(row1[i]==row2[j]){
                     if(out==0){
                         out=row1[i];
                     } else {
                         out=-1;
                         i=4;
                         outfile<<"Case #"<<counter<<": Bad magician!";
                         break;
                      }
                }
            }
        }
        if(out>=0){
            if(out==0)
                outfile<<"Case #"<<counter<<": Volunteer cheated!";
            else
                outfile<<"Case #"<<counter<<": "<<out;
        }
        --inputs;
        ++counter;
        if(inputs>0)
            outfile<<std::endl;
    }

	return 0;
}
