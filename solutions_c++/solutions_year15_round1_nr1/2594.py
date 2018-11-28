//Written by Jorge Beltran
//Takes mushrooms.in as input.

#include <fstream>
using namespace std;


int main()
{
  //declare variables
  ifstream fin;
  int NCases;
  int* Method1;
  int* Method2;

//get input from file.
  //read input from file
  fin.open("Mushrooms.in");
  if(!fin.good()) throw "I/O error";

  //get the number of cases.
  fin >> NCases;
  fin.ignore(1000,10);  
 


  //create arrays to store the 2 method answers.
  Method1 = new int[NCases];
  Method2 = new int[NCases];

  for(int i = 0; i < NCases; i++)
  {
    //case logic
    int ArrayLength;
    int* MushroomAmounts;

    //get the length of the mushroomAmounts array
    fin >> ArrayLength;
    fin.ignore(1000, 10);



    //create an array to hold the mushroom times.
    MushroomAmounts = new int[ArrayLength];

    for(int j = 0; j < ArrayLength; j++)
    {
      fin >> MushroomAmounts[j];
    }

    //method 1.  
    //for the array, have a2 - a1 be the number of mushrooms eaten in 10 sec.
    //loop through the array and get a sum of the differences.
    //this is the answer to the method 1.

    //int to store the total
    int sum = 0;
    int temp = 0;

    for(int j = 0; j < (ArrayLength-1); j++)
    {
      //find the difference between 2 adjacent elements
      temp = (MushroomAmounts[j] - MushroomAmounts[j+1]);       
      

      //if it is non-negative, add it to the sum
      if(temp >= 0)
      {
        sum += temp;
      }

    }



    //save it to the method 1 array.
    Method1[i] = sum;

    //method 2
    //Find the greatest rate of consumption.
    int rate = 0;
   
    for(int j = 0; j < (ArrayLength-1); j++)
    {
      //find the difference between 2 adjacent elements
      temp = (MushroomAmounts[j] - MushroomAmounts[j+1]); 

      //if temp is greater than the old rate, if becomes the new rate.
      if(temp > rate)
      {
        rate = temp;
      }
    }


    //now add mushrooms to the sum.
    //first, reset the sum.
    sum = 0;

    //Cycle through the elements again.
    for(int j = 0; j < (ArrayLength-1); j++)
    {
      //x > y
      if(MushroomAmounts[j] > MushroomAmounts[j + 1])
      {
        //+ rate if x >= rate
        if(MushroomAmounts[j] >= rate)
          sum += rate;
        //+x if x < rate
        else
          sum += MushroomAmounts[j];
      }
      //x == y
      else if(MushroomAmounts[j] == MushroomAmounts[j + 1])
      {
        //+ rate if x >= rate.
        if(MushroomAmounts[j] >= rate)
          sum += rate;
        else
          sum += MushroomAmounts[j];
      }
      //x < y
      else if(MushroomAmounts[j] < MushroomAmounts[j + 1])
      {
        //+rate if rate <= x.
        if(rate <= MushroomAmounts[j])
          sum += rate;
        //+x if rate > x. 
        else
          sum += MushroomAmounts[j];  
      }

    }

    //the sum is the answer to method 2.
     Method2[i] = sum;

    //delete the new stuff
    delete [] MushroomAmounts;

  }

  //close file.
  fin.close();
  

  //output
  //Open new file
  ofstream fout;
  fout.open("Mushrooms.txt");

  //output loop
  for(int i = 0; i < NCases; i++)
  {
    fout << "Case #" << i+1 << ": " << Method1[i] << " " << Method2[i] << endl;
    
  }


  //delete new stuff
  delete [] Method1;
  delete [] Method2;

  return 0;

}