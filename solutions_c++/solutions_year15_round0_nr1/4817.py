#include <iostream>
#include <sstream>
#include <utils/codejam_io.h>

using namespace std;


int find_min_invitees(int smax, string audience)
{
  

  int standing = 0;
  int invited = 0;
  //cout << "smax = " << smax << " " << audience << endl;
  for(int shyness = 0; shyness < (smax+1); shyness++)
  {
    stringstream ss;
    
    ss << audience[shyness];
    
    int people = 0;
    
    ss >> people;
    
    // If there are people for that shyness index 
    if(people != 0)
    {  
	// Can people at that shyness level stand up ?
	// Yes, if there are already enough standing people.
	if(standing >= shyness )
	{
	    standing+=people;
	}
	else // if there are not enough standing folks then we need to invite.
	{
	   
	   int required = shyness-standing; 
	   //cout << "index " << shyness << " standing " << standing << " required " << required << endl;
	   invited += required;
	   standing += required;
	   standing += people;
	}
    }
  }
  
  return invited;
}


int main(int argc, char **argv)
{
    //CJInputFile input_file;
    CJInputFile input_file("A-large.in");
    ofstream	output_file("results.txt", std::ios::out);
    
    int 	number_of_tests = input_file.getNumberOfTests();
    
    for(int i = 0; i < number_of_tests; i++)
    {
	int 	smax = input_file.nextIntegerToken();
	string  audience = input_file.nextToken();
	int result = find_min_invitees(smax,audience);
	output_file << "Case #" << i+1 <<": " << result << endl;
    }
    
    return 0;
}
