# include <iostream>
# include <fstream>
using namespace std ;

class Cardss 
{
    public:
    ifstream read ;
    
    int Cards[4][4] ;
    int CardSecond[4][4] ;
    int FirstArrangementrow ,SecondArrangementrow ;
    int num ;
    int check ;
    ofstream Write ;
    Cardss()
    {
           read.open("q1.txt");
           Write.open("output.txt");
           
    }
    void Perform()
    {
         int TestCases ;
         read >> TestCases ;
         for ( int run = 1 ; run <= TestCases ; run++ )
         {
         read >> FirstArrangementrow ;
         FirstArrangementrow-- ;
         for (int i = 0 ; i < 4 ; i++ )
         {
               for ( int j = 0 ; j < 4 ; j++ )
               {
                   read >> Cards[i][j] ;
               }
         } 
         read >> SecondArrangementrow ;
         SecondArrangementrow-- ;
         for (int i = 0 ; i < 4 ; i++ )
         {
               for ( int j = 0 ; j < 4 ; j++ )
               {
                   read >> CardSecond[i][j]  ;
               }
         }    
         if ( check_isSame() == false )
         {
              Write << "Case #" << run << ": Volunteer cheated!" << endl ;
         }
         else
         {
            if ( check_Cards() == true )
            {
                 Write << "Case #" << run << ": " << num  << endl ;
            }
            else
            {
                Write << "Case #" << run << ": Bad magician!" << endl ;
            }
         }
         }
         read.close();
         Write.close();
         
    }
    bool check_isSame()
    {
          bool flag = true ;
          bool flag1 = false ;
          check = 0 ;
          for ( int j = 0 ; j < 4 ; j++ )
          {
                    for ( int k = 0 ; k < 4 ; k++ )
                    {
                        if ( Cards[FirstArrangementrow][j] == CardSecond[FirstArrangementrow][k] )
                        {   
                             flag1 = true  ;
                        }
                    }
                    if ( flag1 == false  )
                    {
                        flag = false ;
                        
                    }
                    else
                    {
                        
                        flag1 = false ;
                    } 
          }
          if ( (flag == true && FirstArrangementrow != SecondArrangementrow)  )
          {
              return false ;
          }
          bool a = false ;
          for ( int j = 0 ; j < 4 ; j++ )
          {
                    for ( int k = 0 ; k < 4 ; k++ )
                    {
                        if ( Cards[FirstArrangementrow][j] == CardSecond[SecondArrangementrow][k] )
                        {   
                            a = true ;
                        }
                    }
                    if ( a == false )
                    {
                         check++ ;
                    }
                    else
                    {
                        a = false ;
                    }
          }
          if ( check == 4 ) 
          {
               return false ;
          }
          
          
          
              return true ;
          
    }
    
    bool check_Cards()
    {
          int count = 0 ;
          
          for ( int j = 0 ; j < 4 ; j++ )
          {
                    for ( int k = 0 ; k < 4 ; k++ )
                    {
                        if ( Cards[FirstArrangementrow][j] == CardSecond[SecondArrangementrow][k] )
                        {   
                             count++ ;
                             num =  Cards[FirstArrangementrow][j] ;
                        }
                    }
          }
          if ( count == 1 )
          {
               return true ;
          }
          else
          {
              return false ;
          }
    }               
         
    
};
int main()
{
    Cardss obj ;
    obj.Perform();
    //system("pause");
    return 0;
}
