#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>


using namespace std;


int competition(std::vector<int> & input);


int main (int argc, char** argv) {

//-------------------FILE INPUT -------------------------------------------//
  string line;
  string input ; 
  string output ; 
  if(argc == 3)
  {
    input = argv[1];
    output = argv[2];
  }
  ifstream inputFile (input);
  ofstream outputFile;
  outputFile.open (output);
  vector <int> data ; bool multiDigitInput = true ; bool readTestCase = true ; 
  
  
  if (inputFile.is_open())
  {
    while ( getline (inputFile,line) )
    {
      //out << line << '\n';                     DEBUG
      if(readTestCase) // Handle Corner Case of single Multi Digit 
      {
        istringstream ss(line);
        int num; 
        ss >> num ; 
        //cout << num ;                             DEBUG
        data.push_back(num);
        readTestCase = false; 
      }
      int multiNum = 0 ; // Multiple Digit Number 
      for(char& c : line)
      { 
           if(c == ' ')
           {
               // End of a multi digit number 
               multiDigitInput = false ;
               data.push_back(multiNum);
               //cout << multiNum << endl ;                     DEBUG
               //cout << ">>";                     DEBUG
           }
           else
           {
                int number = c - '0';
                if(multiDigitInput)
                {
                    multiNum *= 10; // Shift the place value; 
                    multiNum += number; 
                }
                else // Single Digit Input 
                {
                    data.push_back(number);
                }
              
           }
           
         }// end for 
      multiDigitInput = true ; 
    } // end while
    inputFile.close();
  }
  else 
  {
     cout << "Unable to open file"; 
  }
 //------------------------------Data Extraction ----------------------------//
int testCases = int(data[0]); 
int sentinel = 0 ;
 int counter = 1; 
cout <<" Test Cases :" << testCases << endl ;
for(int i = 1 ; i <= testCases; ++i)
{
    vector<int> passData; 
    outputFile << "Case #"<< i << ": ";
    sentinel = data[counter];
    passData.push_back(sentinel); 
    for(int i = counter+1 ; i < counter + sentinel + 2; i++)
        {
            passData.push_back(data[i]);
        } 
     
    counter += sentinel+2;
    outputFile << competition(passData) << endl;          
}

  return 0;
}









int competition(std::vector<int> & input)
{
    int result = 0 ; 



    int sentinel = input[0];

    if(sentinel == 0 )
    {
        return 0 ; 
    }
    
   cout << "input : "; 
   for(auto i: input) cout << i ; cout << endl ;
    
    int friends = 0 ;    
    cout << sentinel ; int shyRemovePower = 0;
    for(int i = 1 ; i < input.size() ; i++)
    {
        if(input[i] != 0 ) 
        // if equal zero , then we do not have to raise them 
        {
            int shyness = i - 1 ; // ignoring sentinel
            // Compensate shyness with friends 
            if(shyness > shyRemovePower)
            {
                int needed = (shyness - shyRemovePower);
                
                
                friends += needed; 
                // Frinds give Power
                shyRemovePower += needed; 
                // People who became unshy gives Power
                shyRemovePower += input[i]; 
            }
            else // Enough Power (eople in front )
            {
            
            shyRemovePower += input[i];               
            
            }

        }    
    }
    result = friends ; 
    
    
    

    cout << endl ;
    //result = guess ; 











































    return result;

}













