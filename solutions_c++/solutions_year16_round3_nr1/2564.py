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

int parties ;
int sens[1000] ;
int majority = 0 ;
int total = 0 ;
int get_greatest();
bool maj_check(int, int);

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
      
        majority = 0 ;
        total = 0 ;
        bool done = false ;
        
        
        issy >> parties  ;
        
        fprintf(stderr,"number of parties  %d \n",parties );
        
        std::getline(infile, testcases) ; // read in the pattern
        std::istringstream issw(testcases);
      
        for (int x = 0 ; x < parties ; x ++)
        {
            
            
            issw>> sens[x] ;
            
            fprintf(stderr,"sens %d \n",sens[x] );
            total = total + sens[x] ;
            fprintf(stderr,"total %d \n",total);
            
        }
        
        printf("Case #%d:",n+1);
        while (!done)
        {
        
        // evalcuate the greatest
            int greatest = get_greatest() ;
            printf(" %c",static_cast<char>(greatest+65));
            sens[greatest] -- ;
            total = total - 1;
            greatest = get_greatest() ;
            if (total == 0) break ;
        
        // evacate another greates if it doesn't cause a majority
            bool fail = maj_check(greatest,total);
            if (total > 0){
            if (!fail)
            {
                printf("%c",static_cast<char>(greatest+65));
                sens[greatest] -- ;
                total = total - 1;
            }
            }
            if (total == 0 ) done = true ;
        
        // loop
        }
        
            printf("\n");
       
    
    }
    
    return 0;
    
}

int get_greatest()

{
    int party = 0 ;
    int ret = 0 ;
    for (int x = 0 ; x < parties ;x ++)
    {
        if (sens[x] > party )
        {
            ret = x ;
            party = sens[x] ;
        }
    }
        return ret ;
}

bool maj_check ( int party , int total )
{
    // check if removing this 1 person causes a majority
    bool fail = false ;
    int majority = (total -1 ) ;
    for (int x = 0 ; x < parties ; x ++)
    {
        //skip party removing the guy
        if (x != party)
        {
            if (sens[x]*2> majority) fail = true ;
            fprintf(stderr,"checking %d %d  %d  %d \n",x ,sens[x] , majority , fail  );
            
        }
        
    }
    return fail ;
}






