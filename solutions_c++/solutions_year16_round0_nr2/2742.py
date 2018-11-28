#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <stdint.h>
#include <unistd.h>


#define ha //

// 64bitoperations need 32 bit max numbers


using namespace std;

string testcases ;
long long unsigned queue_peoples [1000 ] ;
long long unsigned size_queue ;
long long unsigned num_loops ;
long long unsigned lastitem ;
long long unsigned accumilated_on_loop ;



int main(int argc, const char * argv[]) {
    std::ifstream infile("/Users/marcsaunders/Desktop/codejam/in.txt");
    freopen("/Users/marcsaunders/Desktop/codejam/out.txt","w",stdout);
    std::getline(infile, testcases) ; // read in string number of test cases
    std::istringstream iss(testcases);
    int W ;
    iss >> W;
    fprintf(stderr,"\n");
    fprintf(stderr,"there are %d tests in this guy\n",W);
    
    string rounds_str ;
    
    for(int n=0;n<W;n++)
    {
        
        
        std::getline(infile, testcases) ; // read in the pattern
        std::istringstream issy(testcases);
        string Rounds ;
        
        issy >> Rounds ;
        
        fprintf(stderr,"Test case number  %s \n",Rounds.c_str() );
        
         unsigned long  len = Rounds.length();
        int flips  = 0 ;
        string last = Rounds.substr(0,1);
        
            for (int x=1;x<len;x++)
            {
                if ( last != Rounds.substr(x,1))
                {
                    flips = flips + 1 ;
                    last = Rounds.substr(x,1) ;
                }
                
                
            }
            
        if (Rounds.substr(len-1,1) == "-") flips++ ;
        
            printf("Case #%d: %d\n",n+1,flips);
        
        
    }
    
    return 0;
    
}