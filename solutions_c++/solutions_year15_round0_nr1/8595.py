#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>

template<typename Iterator>
bool zeroExist(Iterator start, Iterator end)
{
    return std::count(start, end, 0) != 0;
}

template<typename Iterator>
int extraFriendsNeeded(Iterator vectorstart, Iterator start, Iterator end, size_t extrapersons = 0)
{
    //find first person that is nonzero after a zero
    auto firstNonZeroAfterZero = std::find_if(std::find(start,end,0), end, [](int a){ return a != 0;});
    int shynessAtNonZero = std::distance(vectorstart,firstNonZeroAfterZero);
    int personsStanding =  std::accumulate(vectorstart,firstNonZeroAfterZero ,0);
    //std::cout << "persons: " << personsStanding<< " shyness: " << shynessAtNonZero<< std::endl;
    if (personsStanding + extrapersons <= shynessAtNonZero)
    {
        extrapersons += shynessAtNonZero - (personsStanding + extrapersons);
        if (zeroExist(firstNonZeroAfterZero, end))
        {
            return extrapersons + extraFriendsNeeded(vectorstart, firstNonZeroAfterZero + 1, end, extrapersons);
        }
        else
            return extrapersons ;
    }
    else return 0;
}

std::ostream& operator<<(std::ostream& o, const std::vector<int>& vec){
    for(auto i: vec)
    {
        o << i;
    }
    o << std::endl;
    return o;
}

int main(int argc, char *argv[])
{
    std::fstream infile("standing.txt");

    size_t nrOfCases;
    infile >> nrOfCases;

    std::string a;
    std::getline(infile,a);

    for (int i = 0; i < nrOfCases; ++i)
    {
        std::string line;
        std::getline(infile, line);

        int Smax;
        std::string people;


        std::istringstream test(line);
        test >> Smax;
        test >> people;
        std::vector<int> convertedInput;
        std::for_each(std::begin(people), std::end(people), [&](char a){convertedInput.push_back(std::stoi(std::string(&a)));});


        //find first zero
        size_t extraFriends = 0;
        if (zeroExist(convertedInput.begin(), convertedInput.end()))
        {
            auto start = std::begin(convertedInput);
            auto current = start;
            while(current != std::end(convertedInput))
            {
                auto nextNonZeroAfterZero = std::find_if(std::find(current, std::end(convertedInput), 0),
                                                         std::end(convertedInput),
                                                         [](int a){return a!=0;});
                current = nextNonZeroAfterZero;
                auto currentShyness = std::distance(start, current);
                if (nextNonZeroAfterZero != std::end(convertedInput))
                {
                    int totalPersonsStanding = std::accumulate(start, current, 0) + extraFriends;
                    //std::cout << "shyness" << currentShyness << " | " <<totalPersonsStanding << "ASDASD" << std::endl;

                    if (currentShyness > totalPersonsStanding)
                    {
                        extraFriends += currentShyness - totalPersonsStanding;
                        //std::cout << "extrafriends now " << extraFriends << std::endl;
                    }
                }

            }
            //extraFriends = extraFriendsNeeded(convertedInput.begin(), convertedInput.begin(), convertedInput.end());
            //if (personsStanding + extraFriends <= shynessAtZero)
            //{
                //extraFriends++;
            //}

        }
        //std::cout << "Case #" << (i + 1) <<": " << extraFriends << " " << convertedInput << std::endl;
        std::cout << "Case #" << (i + 1) <<": " << extraFriends  << std::endl;

    }

    return 0;
}
