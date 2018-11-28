//-------------------------------
//  Round_1_B Problem 1
//-------------------------------
#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
//-------------------------------
//  Basic Structures
//-------------------------------

//-------------------------------
//  Function Prototypes
//-------------------------------

//-------------------------------
//  main
//-------------------------------
int main()
{
    std::ifstream myFile("B-small-attempt0.in.txt");
    std::ofstream output("output.txt");
    
    // body
    int count;
    myFile>>count;
    int A,B,K;
    for(int ii=1;ii<=count;++ii){
        int amount=0;
        myFile>>A;
        myFile>>B;
        myFile>>K;
        int result=0;
        
        for(int ii=0;ii<A;++ii){
            for(int jj=0;jj<B;++jj){
                int c=ii&jj;
                if(c<K)
                    result++;
            }
        }
        
        std::cout<<"Case #"<<ii<<":"<<" "<<result<<std::endl;
    }
    return 0;
}