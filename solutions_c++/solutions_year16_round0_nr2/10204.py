
#include <iostream> 
#include <vector>
#include <string>

using std::vector;
using std::string;
using namespace std; 


int main() 
{
  int t;
  cin >> t; 

  for (int i = 0; i <= t; i++) 
  {
    string line;
    getline(cin,line, '\n');

    int length = line.size();
    int cur = 0 ; //previous index
    int next = 1 ; //current index
    int count = 0;
    
    if (i > 0 ) 
    {
        //CASE 0: only one sign
        if (length < 2)
        {
          //cout << "Run CASE 0" <<endl;
          if (line[0] == '-')
          {
            line[0] = '+'; //filp!
            count++ ;
          }
        }//end CASE 0

       else
       {
        while(cur < length) 
      	{ 
          //CASE End: the last element
          if (cur == length-1)
          {
            //cout << "Run CASE End" <<endl;
            if (line[cur] == '-')
            {
              for( int k = 0; k <=cur; k++ ) //all flip !
              {
                line[k] = '+' ;
              }
              count++;
            }
            cur++ ;
          }//end CASE End

          // CASE 1: Same sign, both move on or end
          if ((line[cur] == '-' && line[next] == '-') || (line[cur] == '+' && line[next] == '+' )) 
          {
            //cout << "Run CASE --++" <<endl;
            cur++ ;
            next++ ;
          }//end CASE 1

          //CASE 2 Opposite sign, flip to the same & move on
          else if ( line[cur] == '-' && line[next] == '+')
          {
            //cout << "Run CASE -+" <<endl;
            for( int k = 0; k <= cur; k++ ) //flip !
            {
              line[k] = '+' ;
            }
            count++;
            cur++ ;
            next++ ;
          } //end CASE 3

          //CASE 3 Opposite sign, flip to the same & move on
          else if ( line[cur] == '+' && line[next] == '-')
          {
            //cout << "Run CASE +-" <<endl;
            for( int k = 0; k <= cur; k++ ) //flip !
            {
              line[k] = '-' ;
            }
            count++;
            cur++ ;
            next++ ;
          } //end CASE 4
      	}//end while
      }//end else

    cout << "Case #" << i << ": " << " " << count << endl;  

    }//end if

  }//end for 

}//end main
