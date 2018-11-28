# include <iostream>
# include <fstream>
# include <iomanip>
using namespace std ;
int main()
{   
    ifstream read ;
    ofstream Write ;
    int noOfFarms = 0 ;
    double C,F,X ;
    double Time = 0 ;
    bool flag = false ;
    double Production = 2 ;
    int cookies = 0 ;
    read.open("q2.txt");
    Write.open("output.txt");
    int TestCases ;
    read >> TestCases ;
    
    for ( int i = 0 ; i < TestCases ; i++ )
    {
        Time = 0.0000 ;
        flag = false ;
        Production = 2 ;
    read >> C ;
    read >> F ;
    read >> X ;
    float a = 1 ;
    
    
    //system("pause");
    
    while ( flag != true )
    {
          if ( (Time + X/Production) > (Time + C/Production + X/(Production+F)) )
          {
               cookies = 0 ;
               Time += (double) ( C/Production) ;
               Production+= F ;
          }
          else
          {
              Time += (double) ( X/Production) ;
              flag = true ;
          }
    }
    std::cout.setf( std::ios::fixed, std:: ios::floatfield );
    cout << "Case #" << i+1 <<": "  << Time  << endl ;
}
    system("pause");
    return 0 ;
}
    
    
    
    
    
