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
        bool keep_going = false;
        
        long long unsigned Rounds ;
        long long unsigned runner = 0;
        
        
        issy >> Rounds ;
        
        fprintf(stderr,"Test case number  %llu \n",Rounds );
        
        bool hello[10] ;
        
        for (int x = 0 ; x <10 ; x++ )
        {
            hello[x] = false;
        }
        
        
        stringstream convert;
        
        for (int y = 0 ; y < 200 ; y++)
        {
            runner = runner + Rounds ;
            
            convert << runner ;
        
            rounds_str  = convert.str() ;
        
        unsigned long  len = rounds_str.length();
        
        for (int x=0;x<len;x++)
        {
            int a = stoi(rounds_str.substr(x,1));
            hello[a]=true;
            
        }
        
        keep_going = false ;
        
        for (int x = 0 ; x <10 ; x++ )
        {
            if (!hello[x])
            {
                keep_going = true ;
            }
        }
        
       if( ! keep_going)
       {
           break ;
       }
           // Rounds = Rounds * 2 ;
            
        }
        
        if (keep_going)
        {
            printf("Case #%d: INSOMNIA\n",n+1);
        }
        else
        {
            printf("Case #%d: %llu\n",n+1,runner);
        }
    
    }
    
    return 0;
    
}