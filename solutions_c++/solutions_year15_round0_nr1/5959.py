#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int calculate_minimum_to_sheer_crowd (std::string &crowd)
{
    unsigned int number_of_friends = 0;
    unsigned int number_of_people_sheering_up = crowd [0] - '0';
    
    for (unsigned int k = 1; k < crowd.length();k++)
    {
    	if (number_of_people_sheering_up < k)
	{
	    number_of_friends += (k - number_of_people_sheering_up);
 	    number_of_people_sheering_up += (k - number_of_people_sheering_up); 
        }
        number_of_people_sheering_up += crowd [k] - '0';
    }  
    return number_of_friends;
}

int main ()
{
    unsigned int number_of_cases = 0;
    cin >> number_of_cases;
    
    for (int i = 0; i < number_of_cases; i++)
    {
       unsigned int people;	
       std::string crowd;
       cin >> people >> crowd;
       unsigned int minimum = calculate_minimum_to_sheer_crowd (crowd);
       cout << "Case #" << i + 1 << ": " << minimum << endl;
    } 	
}

