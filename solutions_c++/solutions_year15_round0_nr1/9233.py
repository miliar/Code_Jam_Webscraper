#include <iostream>

using std::cin;

int main()
{

//Number of cases
unsigned int numCases; //Number of tests
unsigned int maxShyness; //Max shyness level for a test
unsigned int shynessLevel; //Current shyness level being analyzed
unsigned int peopleStanding; //Current number of people standing
unsigned int friendsNeeded; //Number of friends needed

cin >> numCases;

for( unsigned int trial = 1; trial <= numCases; ++trial )
{
    //Read in max shyness
    cin >> maxShyness;
    //Read past space
    cin.get();
    //Reset number of people standing and friends needed
    peopleStanding = 0;
    friendsNeeded = 0;
    for( unsigned int shynessLevel = 0; shynessLevel <= maxShyness; ++shynessLevel )
    {
        if( shynessLevel > peopleStanding )
        {
            friendsNeeded += shynessLevel - peopleStanding;
            peopleStanding += shynessLevel - peopleStanding;
        }
        peopleStanding += ( cin.get() - '0' );

    }
    std::cout << "Case #" << trial << ": " << friendsNeeded << std::endl;
    
}

}
