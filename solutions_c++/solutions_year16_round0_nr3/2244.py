#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <stdint.h>
#include <math.h>
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

long long unsigned number_calc (int, long long unsigned , int);
long long unsigned prime_check (long long unsigned ,int ,int) ;

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
        int bits ;
        int outputs ;
        long long unsigned divisor[11] ;
        long long unsigned numbercheck = 0 ;
        bool gotone ;
        int got_count  = 0;
        
        issy >> bits >> outputs  ;
        
        fprintf(stderr,"Test case number    bits %d  out puts %d \n",bits,outputs);
        
        int bunarycount = bits - 2 ;
        
        long long unsigned  maxcount = pow(2,bunarycount);
        printf("Case #%d: \n",n+1);
        
        for (int y = 0 ; y < maxcount ; y ++ )
        {
            //loop through all possible numbers
            gotone = true ;
            
            for ( int qual = 2 ; qual < 11 ; qual ++)
            {
                // prime check starting at lowest number
                numbercheck = number_calc ( qual , y ,bunarycount) ;
                fprintf(stderr,"number returned  %llu qual %d y  %d \n",numbercheck,qual,y);
                if (numbercheck == 0 )
                {
                    gotone = false ;
                    break ;
                    
                    
                }
                long long unsigned pc = prime_check (numbercheck,qual,bits) ;
    //            fprintf(stderr,".... returned devisor  %llu \n",pc );
                
                
                if (pc == 0 )
                {
                    gotone = false ;
                    break ;
                    
                
                }
                else
                {
                    divisor[qual] = pc ;
                }
            }
            
            if (gotone)
            {
                
                stringstream convert;
                
               convert << numbercheck ;
                    
                string rounds_str  = convert.str() ;
                    
                int  len = rounds_str.length();
                
                int need  = 31 - len ;
                
                for (int z = 0 ; z < need ; z ++ )
                    {
                        rounds_str = "0"+rounds_str ;
                    }
                rounds_str = "1" + rounds_str ;
                
                printf("%s",rounds_str.c_str());
                for ( int qual = 2 ; qual < 11 ; qual ++)
                {
                   printf(" %llu",divisor[qual]);
                }
                 printf("\n");
                got_count ++ ;
                if (got_count == outputs )
                {
                    break ;
                }
                
            }
            
        }
        
        
        fprintf(stderr,".......got count   %d \n",got_count);
        
        
    }
  //  fprintf(stderr,".......got count   %d \n",got_count);
    return 0;
}

long long unsigned number_calc (int base , long long unsigned midcount , int itterate )
{
    long long unsigned actnumber = 1 ;
    long long unsigned  mult = base ;
    long long unsigned remainder = midcount ;
    bool err = false ;
    for ( int x = 0 ; x < itterate ; x++)
    {
        if (remainder%2 == 1 )
        {
           if (err)
           {
               fprintf(stderr,"********** overflow error ************* \n");

               return 0 ;
           }
            actnumber = actnumber + mult ;
            remainder = (remainder -1 )/2 ;
        }
        else
        {
            remainder = remainder / 2 ;
        }
        long long unsigned previous_mult = mult ;
        mult = mult * base ;
        if ( mult < previous_mult)
        {
            
     //       fprintf(stderr,"********** overflow error ************* \n");
            err = true ;
        }
    }
  //  actnumber = actnumber + mult ;  // not return the large numbeer so we don't over flow
    
    return actnumber ; // return long long unsigned actual number
}

long long unsigned prime_check (long long unsigned  number, int qual , int bits)

{

    long long unsigned sq = 15000 ;
    if ( sq > 15000)
    {
        sq = 15000 ;
    }
    
    for (int x = 2 ; x < sq ; x ++)
    {
       // first take qaul and decid we add qual ^ 31 thats the most significant bit
        // but instead we do
        long long unsigned remainder = qual ;
        long long unsigned modulate = 0 ;
        for (int z = 0 ; z < 6 ; z ++)
        {
            modulate = remainder * powl ( qual , 5);
            remainder = modulate % x ;
        }
        long long unsigned check_num = remainder + number ;
        
        if (check_num%x == 0)
        {
            return x ;
        }
    }
    
    // you get as far as squareroot and you are good
    // you only need to moduo check with prime numbers
    
    return 0 ; // return a divisor
}







    