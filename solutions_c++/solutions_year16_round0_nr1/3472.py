#include<iostream>
#include<fstream>

using namespace std;

void resetArray(long *arr){
	for (long i = 0; i < 10; ++i)
	{
		arr[i] = 0;
	}
}

void incrementtheArray(long number, long arr[10]){
	if(number == 0){
		arr[0] =  1;
	}else {
		//cout << "in incrementtheArray\n";
		while (number > 0)
		{
	    long digit = number%10;
	    //cout << "Number: " << number << " " << digit << endl;	

	    number /= 10;
	    arr[digit] =  1;
		}
	}
}

bool checkArray(long arr[10]){
	bool decision = true;
	for (long i = 0; i < 10; ++i)
	{
		if(arr[i] <= 0){
			decision = false;
			break;
		}
	}
	return decision;
}


int main(){
	long CHECK = 1000000;
	ifstream input("input.txt");
	ofstream output("output.txt");
	long numberOfInputs;
	input >> numberOfInputs;
	long inputNumber;
	long counter = 0;
	while (numberOfInputs > 0){
		counter++;
		input >> inputNumber;
		long count = 0;
		long* arr = new long[10];
		resetArray(arr);
		for (long i = 0; i < CHECK; i++){
			incrementtheArray(inputNumber*(i+1),arr);
			if(checkArray(arr)){
				output << "Case #" << counter << ": " << inputNumber*(i+1) << endl; 
				break;
			}else if (i == CHECK -1) {
				output << "Case #" << counter << ": " << "INSOMNIA" << endl;
				break;
			}
		}
		numberOfInputs--;
	}	
	input.close();
	output.close();
	return 0;
}

