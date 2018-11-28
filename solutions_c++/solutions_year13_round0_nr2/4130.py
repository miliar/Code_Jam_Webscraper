#include <iostream>
#include <string>
#include <vector>
#include <map>

class Lawnmower
{
      int row, col;
      std::vector< std::vector<int> > lawn;
      typedef std::map< int /*height*/, int /*cell count*/ > Cellcounter;
      Cellcounter cell_count;
      
public:
       void readPattern()
       {
            std::cin >> row;
            std::cin >> col;
            int tmp;
            
            for ( int rrr = 0; rrr < row; ++rrr )
            {
                lawn.push_back( std::vector<int>() );
                for ( int ccc = 0; ccc < col; ++ccc )
                {
                    std::cin >> tmp;
                    lawn[rrr].push_back(tmp);
                    ++cell_count[tmp];
                }
            }
       }
       void isPossible(int testid)
       {
            for( Cellcounter::iterator iii = cell_count.begin(); iii != cell_count.end(); ++iii)
            {
                for ( int rrr = 0; rrr < row; ++rrr )
                {
                    bool pass = true;
                    for ( int ccc = 0; ccc < col; ++ccc )
                    {
                        if ( lawn[rrr][ccc] > iii->first )
                        {
                             pass = false;
                             break;
                        }
                    }
                    if(pass)
                    {
                        for ( int ccc = 0; ccc < col; ++ccc )
                        {
                            if ( lawn[rrr][ccc] == iii->first )
                            {
                                 lawn[rrr][ccc] = -lawn[rrr][ccc];
                                 -- (iii->second);
                            }
                        }
                    }
                }
                if( 0 == iii->second) continue;
                
                for ( int ccc = 0; ccc < col; ++ccc )
                {
                    bool pass = true;
                    for ( int rrr = 0; rrr < row; ++rrr )
                    {
                        if ( lawn[rrr][ccc] > iii->first )
                        {
                             pass = false;
                             break;
                        }
                    }
                    if(pass)
                    {
                        for ( int rrr = 0; rrr < row; ++rrr )
                        {
                            if ( lawn[rrr][ccc] == iii->first )
                            {
                                 lawn[rrr][ccc] = -lawn[rrr][ccc];
                                 -- (iii->second);
                            }
                        }
                    }
                }
                if(iii->second)
                {
                    std::cout << "Case #" << testid << ": NO" << std::endl;
                    return;
                }
            }
            
            std::cout << "Case #" << testid << ": YES" << std::endl; 
       }
};

int main()
{
    int testcases;
    std::cin >> testcases;
    
    for(int iii = 1; iii <= testcases; ++iii)
    {
        Lawnmower solver;
        solver.readPattern();
        solver.isPossible(iii);
    }
        
    return 0;
}
