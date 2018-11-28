#include <cstdio> 
#include <cstdlib> 
#include <iostream> 

using namespace std; 

// Function to find the number of friends that needs to be invited 
// in order to obtain a standing ovation, given the shyness of the 
// people in the audience 
int findFriendsForOvation(int *numppl, int smax) 
{ 
  // We observe that if the last person (i.e. most shy) stands up, 
  // then everyone would have stood up. Another observation is that 
  // if we perform a cumulative sum of the number of people with 
  // shyness less than the current shyness, we would know if the 
  // people with current shyness would stand up or not. If there 
  // are not enough people, we will add our friends 
  int numfriends = 0; 
  int cumppl = 0; 
  
  // We go through the different levels of shyness, starting from 
  // the least shy. We note that the people who are not shy (i.e. 
  // shyness level 0) will always stand up 
  for (int i = 0; i <= smax; i++) 
  { 
    // Check if there is anyone in this shyness level, if not 
    // we don't have to check 
    if (!numppl[i]) continue; 

    // Check if the number of people before this shyness level 
    // is greater than or equal to the shyness level 
    if (cumppl >= i) 
    {
      // Then the people in this shyness level will stand up 
    } else { 
      // There is not enough critical mass, so we need to 
      // invite our friends 
      numfriends += i - cumppl; 
      cumppl += i - cumppl;  
    } 

    // Hence the people in this shyness level will stand up 
    cumppl += numppl[i]; 
  } 

  // Hence returns the number of friends needed 
  return numfriends; 
} 


// Main function 
int main(int argc, char **argv) 
{ 
  // Check for the input arguments
  if (argc < 3) 
  {
     cout << "Usage: ProblemA input.txt output.txt" << endl;

     // Unsuccessful run  
     return -1; 
  } 

  // Get the input and output filenames 
  char *infilename = argv[1]; 
  char *outfilename = argv[2]; 
  
  // Open the files for reading and writing 
  FILE *fin = fopen(infilename, "r"); 
  FILE *fout = fopen(outfilename, "w+"); 

  // Read in the inputs 
  int numcases = 0; 
  while (!feof(fin)) 
  {
    fscanf(fin, "%d\n", &numcases); 

    // Process each test case 
    for (int k = 0; k < numcases; k++) 
    {
      // Get the maximum shyness 
      int smax = 1; 
      fscanf(fin, "%d ", &smax); 
      if (feof(fin)) break; 

      // Setup an array of the number of people with the given shyness 
      int *numppl = new int[smax + 1]; 

      // Read in the number of people with the given shyness 
      for (int i = 0; i <= smax; i++) 
      { 
        unsigned char c = '0'; 
        fscanf(fin, "%c", &c); 
        numppl[i] = c - '0'; 
      }
  
      // Find the number of friends needed to be invited to obtain a standing ovation 
      int numfriends = findFriendsForOvation(numppl, smax); 

      // Hence output the number of friends that need to be invited 
      fprintf(fout, "Case #%d: %d\r\n", k + 1, numfriends); 
      printf("Case #%d: %d\r\n", k + 1, numfriends); 

      // Free the array created to store the number of people with the given shyness 
      if (numppl) 
      {  
        delete[] numppl; 
        numppl = NULL; 
      } 

    }
  } 

  // Closes the files 
  if (fin) 
  { 
     fclose(fin); 
     fin = NULL; 
  } 
  if (fout) 
  { 
     fclose(fout); 
     fout = NULL; 
  } 

  // Succcessful run 
  return 0; 
} 
