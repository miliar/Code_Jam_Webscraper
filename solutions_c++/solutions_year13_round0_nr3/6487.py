
#include<iostream>
#include<fstream>
#include <string>
#include <cmath>

using namespace std;

int temp = 0; 
int checkPal(int num)
{
    if(num > 0)
    {
        temp = (temp*10)+ (num %10);
        checkPal(num / 10); //recursion.        
    }
    return temp;       
}

int main() {

 int* lowerLimit;
 int* upperLimit;
 string inputFileName = "input.txt";
 ifstream inputFile(inputFileName.c_str());

 int numOfCases = 0;

 //open the file
	if(inputFile.is_open())
	{
		//initalize row number
		inputFile >> numOfCases;
		lowerLimit = new int[numOfCases];
		upperLimit = new int[numOfCases];

		for(int i = 1; i <= numOfCases; i++)
		{
			inputFile >> lowerLimit[i];
			inputFile >> upperLimit[i];
		}
		
		//close the file
		inputFile.close();
	}
	else
		cout << "cannot open the image file" << endl;

	int *counter = new int[numOfCases];
	for(int i = 1; i <= numOfCases; i++)
		counter[i] = 0;

	for(int i = 1 ; i <= numOfCases; i++)
	{
		int low = lowerLimit[i];
		int up = upperLimit[i];
		bool isSquare = false;
		bool isPal = false;
		for(int j = low; j <= up; j++)
		{
			//j = 1;
			//check if square
			double root = sqrt(j);
			double intpart = 0;
			double fractpart = modf (root , &intpart);
			isSquare = (fractpart == 0);

			//check if palindrome if it is square
			int tempK = j;
			if(isSquare)
				isPal = (tempK == checkPal(tempK));
			temp = 0;
		//	cout << j << " " << isSquare << endl;
			//check if Fair and square
			int tempL = root;
			if(isSquare == true && isPal == true)
				if(tempL == checkPal(tempL))
					counter[i]++;
			temp = 0;
		}
	}

	//write into a file
	//Declare variables
	string filename = "output.txt";

	//Open a stream for the output file
	ofstream outputFile;
	outputFile.open( filename.c_str(), ios_base::out );
	//Write values into the file stream just like displaying them on the screen
	for(int i = 1; i <= numOfCases; i++)
		outputFile << "Case" << " " << "#" << i << ": " << counter[i] << endl;
	//Close the output file stream
	outputFile.close();

	/*for(int i = 1; i <= numOfCases; i++)
		cout << "Case" << " " << "#" << i << ": " << counter[i] << endl;*/

	/*for(int i = 1; i <= numOfCases; i++)
		cout << lowerLimit[i] << " ";
	cout << endl;

	for(int i = 1; i <= numOfCases; i++)
		cout << upperLimit[i] << " ";*/

}