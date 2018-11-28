#include <iostream>
#include <limits>
#include <string>

std::string check_garden(int const * const garden, const int N, const int M)
{
    for(int r=0 ; r<N ; ++r)
    {
        int min = 10000;

        //find min in row
        for(int c=0 ; c<M ; ++c)
        {
            int i = c+r*M;
            if(garden[i] < min) { min = garden[i]; }
        }

        //see if row is all that min value, if so try next row
        int sum = 0;
        for(int c=0 ; c<M ; ++c)
        {
            int i = c+r*M;
            sum += garden[i];
        }
        if(sum==(min*M)) { continue; }

        //for those that are min in this row, check they min in col too
        for(int c=0 ; c<M ; ++c)
        {
            int i = c+r*M;
            if(garden[i] <= min)
            {
                for(int r2=0 ; r2<N ; ++r2)
                {
                    int i2 = c+r2*M;
                    if(garden[i2] > garden[i]) { return "NO"; }
                }
            }
        }
    }

    return "YES";
}

int main()
{
    int N;
    std::cin >> N;
    ++N;//test cases are indexed from 1

    //now ingore the rest of the line inc newline, eases some tests that
	//try to read a line at a time (and stick on this \n if not removed)
    std::cin.ignore( std::numeric_limits<std::streamsize>::max() , '\n' );

    for( int test_case=1 ; test_case<N ; ++test_case )
    {
    //Prep
        int N, M;
        std::cin >> N >> M;

        int garden[N*M];

        for(int i=0 ; i<N*M ; ++i) { std::cin >> garden[i]; }

    //Work
        std::cout << "Case #" << test_case << ": " << check_garden(garden, N, M) << std::endl;

    //Clean Up
    }
}
