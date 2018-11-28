#include <iostream>
#include <vector>
#include <string>
int main()
{
  std::vector<std::string> out;
  int cases;

  std:: cin >> cases;
  for (int i = 0; i < cases; ++i)
    {

   
      int guessA;
      int guessB;
      std::cin >>guessA;

      int shuffleA[16];
      int shuffleB[16];
      // for (int k = 0; k < 4; ++k)
      // 	{
	  
	
      // 	  shuffleA[k] = new int[4];

      // 	  shuffleB[k] = new int[4];
      // 	}
for (int k = 0; k < 16; ++k)
  {
	std::cin >> shuffleA[k];	
  }

      std::cin >> guessB;
for (int k = 0; k < 16; ++k)
  {
	std::cin >> shuffleB[k];	

  }

 int tempA[4];
 int tempB[4];
 //std::cout << "Guesses " << guessA << " " <<guessB << std::endl;
 guessA--;
 guessB--;
 for (int k = 0; k < 4; ++k)
   {
     tempA[k] = shuffleA[k+(4*guessA)];
   }

 for (int k = 0; k < 4; ++k)
   {
     tempB[k] = shuffleB[k+(4*guessB)];
   }
 int count = 0;
 int result = -1;
 for (int k = 0; k < 4; ++k)
   {
     for (int j = 0; j < 4; ++j)
       {
	 
       
	 if (tempB[k] == tempA[j])
	   {
	     count++;
	     result = tempB[k];
	   }
       }
   }
 std::string final = "Case #" + std::to_string(i+1)+": ";
 if ( count == 1)
   {
     final += std::to_string(result); 
   }
 else if ( count == 0 )
   {
     final += "Volunteer cheated!";
   }
 else {
   final += "Bad magician!";
 }
 out.push_back(final);

// for (int i = 0; i < 4; ++i)
//   {
//     for (int j = 0; j < 4; ++j)
//       {
// 	std::cout << shuffleA[j][i] << " ";	
//       }
//     std::cout << std::endl;
//   }

// for (int i = 0; i < 4; ++i)
//   {
 
//     for (int j = 0; j < 4; ++j)
//       {
// 	std::cout << shuffleB[j][i] << " ";	
//       }
//     std::cout << std::endl;
//  }
      
    }


  for (int i = 0; i < out.size(); ++i)
   {
     std::cout << out.at(i) << std::endl; 
   } 
}
