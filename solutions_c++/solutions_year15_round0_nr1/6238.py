#include <iostream>
#include <fstream>
#define DEBUG 0

using namespace std;

int main() {
	
	std::ifstream in("in");
    std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

    std::ofstream out("out");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
	
	int t;
	
	cin >> t;
	
	
	
	for (int i = 0; i < t; i++)
	{
		int num_standing = 0;
		int num_needed = 0;
		
		int max;
		cin >> max;
		
		for (int current_shyness_level = 0; current_shyness_level < max + 1; current_shyness_level++)
		{
			
			if (DEBUG) cout << "Shyness level: " << current_shyness_level << "\n";
			
			char num_people_char;
			cin >> num_people_char;
			
			int num_people = num_people_char - '0';
			
			// If we're at 0, immediately add those people to the total standing.
			if (current_shyness_level == 0)
			{
				num_standing += num_people;
				
				if (DEBUG) cout << "At 0. Number standing is now " << num_standing << "\n";
				
			}				
			
			// Else
			else
			{
				// If we don't have enough people standing, then we need to compensate by inviting more friends.
				if (num_standing < current_shyness_level) 
				{
					// We need to bring the number standing up to the shyness level. So we invite the number
					// of friends equivalent to their difference.
					num_needed += current_shyness_level - num_standing;
					
					if (DEBUG) cout << "Needed more. Had " << num_standing << ", needed " << current_shyness_level << "\n";
					
					// We add the number invited to the number standing.
					num_standing += current_shyness_level - num_standing;
				}
				
				// At this point, there are enough people to ensure that the people of the current shyness
				// level will also be standing. Thus, we can add these people to the number of people standing.
				num_standing += num_people;
				
				if (DEBUG) cout << "Level complete. Number standing is now " << num_standing << "\n";
			}
			
		}// End for each shyness level
		
		cout << "Case #" << i + 1 << ": " << num_needed << "\n";
	}// End for each test case
}