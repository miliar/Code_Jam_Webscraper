# include <iostream>
# include <fstream>
using namespace std ;
class DecWar
{
      public:
      float *Noami_W ;
      float *Ken_W ;
      ifstream read ;
      ofstream Write ;
      int N ;
      int OptimalCount,WarCount ;
      DecWar()
      {
           read.open("D-large.in");
           Write.open("output.txt");
           
      }
      void Sort()
      {
          float temp ;
          if ( N != 1 )
          {
               for (int i = 0 ; i  < N ; i++ )
               {
                   for ( int j = N-2 ; j >= 0 ; j-- )
                   {
                       if ( Noami_W[j] > Noami_W[j+1] )
                       {
                          temp = Noami_W[j] ;
                          Noami_W[j] = Noami_W[j+1] ;
                          Noami_W[j+1] = temp ;
                       }
                   }
               }
               for (int i = 0 ; i  < N ; i++ )
               {
                   for ( int j = N-2 ; j >= 0 ; j-- )
                   {
                       if ( Ken_W[j] >Ken_W[j+1] )
                       {
                          temp = Ken_W[j] ;
                          Ken_W[j] = Ken_W[j+1] ;
                          Ken_W[j+1] = temp ;
                       }
                   }
               }
          }
    
                
      }
      int Count()
      {
           int check[N];
           for ( int i = 0 ; i < N ; i++ )
           {
               check[i] = 0 ;
           }
           for ( int i = 0 ; i < N ; i++ )
           {
               for ( int j = 0 ; j < N ; j++ )
               {
                   if ( Noami_W[i] > Ken_W[j] && ( check[j] != 1 )  )
                   {
                                   OptimalCount++ ;
                                   check[j] = 1 ;
                                   break ;
                   }
               }
           }
      }
    
      void Perform()
      {
           int TestCases ;
           read >> TestCases ;
           for ( int run = 0; run < TestCases ; run++ )
           {
           OptimalCount = 0 ;
           WarCount = 0 ;
           read >> N ;
           Noami_W = new float[N] ;
           Ken_W = new float[N] ;
           for ( int i = 0 ; i < N ; i++ )
           {
              read >>  Noami_W[i]  ;
           }
           for ( int i = 0 ; i < N ; i++ )
           {
              read >>  Ken_W[i]  ;
           }
           Sort();
           Count();
           bool flag = false ;
           for ( int k = 0 ; k < N ; k++ )
           {
             flag = false ;
             for ( int j = 0 ; j < N && flag == false ; j++ )
             {
                 if ( Noami_W[k] < Ken_W[j] && ( Ken_W[j] != (float) (1.1) ) )
                 {
                      Ken_W[j] = 1.1 ;
                      flag = true ;
                 } 
             }   
             if ( flag == true )
             {
                  flag = false ;
             }
             else
             {
                 
                 WarCount++ ;
             }
           }
          
           Write << "Case #" << run+1 << ": " << OptimalCount << " " << WarCount << endl ;
           
           }
           
      }
     
};

int main()
{
    DecWar obj ;
    obj.Perform();
    //            system("pause");
    return 0 ;
}
