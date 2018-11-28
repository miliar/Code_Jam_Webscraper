
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <math.h>
using namespace std;

int main () {


	ifstream File;
	int numberofCases;
    File.open("A-small-attempt7.in");
    ofstream outfile;
    outfile.open("out4.txt");
    File >> numberofCases;
    int arr[numberofCases];
    for (int i = 0; i < numberofCases; i++)
    {
        File >> arr[i];
    }

for(int in = 0; in < numberofCases; in++ )
    {
    int array[10] = {0,1,2,3,4,5,6,7,8,9};
    string line;
    //cout<<arr[in]<<endl;
	int string_size = 0;
	int ender = 0;
	int int_l = 0;

	int int_line=0;

	int jack = 0;
	int inputer = arr[in];
	int powa = 1;
	int input_1 = 0;
	int input_2 = 0;
	int limit = 0;
	int sizer = 0;
	int x1=0;
    int input = 0;
	while (jack != 1){
		x1 = x1+1;
		input = inputer*x1;
		ostringstream ss;
        ss << input;
        string sizr = ss.str();
        int sizer = sizr.size();
		input_2 = input;
        //cout<< input;
		for(int i = sizer; i > 0 ; --i)
		{

			if (i != 1){
				input_1 = input_2 %10;

			}
			else{
				input_1 = input_2;

			}
			input_2 = input_2 /10;
			for (int k =0 ; k < 10 ; k++)
			{

				if(input_1 == array[k])
				{
					array[k] = 1;

				}
				//cout<< array[k];


			}
			//checking if all array in == 10
			for(int j =0; j< 10; j++)
			{
				if(array[j] != 1)
					break;
				if(j == 9 && array[j]==1)
				{

					outfile<< "Case #"<<in+1<<": ";



					outfile<< input;
                    outfile<< "\n";
					jack= 1;
					break;
				}

			}
			if(jack== 1)
                break;
		}
		limit++;
		if(limit == 10000){



					outfile<< "Case #"<<in+1<<": ";



					outfile<< "INSOMNIA";

                    outfile<< "\n";
					jack= 1;
					break;

		}


	}


}

}
