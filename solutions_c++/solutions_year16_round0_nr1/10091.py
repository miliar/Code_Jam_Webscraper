#include <cstdlib>
#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>
#include <algorithm>

int tag;
int * status ;

int compute(int num){

	tag++;
	int unseen = 10;
	int i;
	int multiple;
	int temp;
	multiple = num;

	while(1){

		temp = multiple; 
		while(temp){
			i = temp%10;
			temp = temp/10;
			if(status[i] != tag){
				status[i] = tag;
				unseen--;
			}
		}
		if(unseen == 0){
			break;
		}
		multiple = num + multiple;

	}
	return multiple;


}

main(){

	status = new int[10]();

	std::vector<int> data;
	std::string line;
    std::ifstream myfile("A-large.in");
    if (myfile)  // same as: if (myfile.good())
    {

    	std::getline( myfile, line );

        while (std::getline( myfile, line ))  // same as: while (getline( myfile, line ).good())
        {
            std::istringstream ss(line);
    
    		int i;
    		ss >> i;
    		data.push_back(i);

        }
        myfile.close();
    }

    for(int i = 0  ; i < data.size() ; i++)
   	{
   		if(data[i] == 0)
   			std::cout << "Case #" << i+1 << ": INSOMNIA" << std::endl;
   		else
   			std::cout << "Case #" << i+1 << ": " << compute(data[i]) << std::endl;
   	}


}