#include <iostream>

using namespace std;

int main() {
	// your code goes here
	int length, index, counter, current=1, spareFlips, flips;
	string str;
	cin>>length;
	for(index = 0; index < length; index++)
	{
	    counter = 0;
	    flips = 0;
	    spareFlips = 0;
	    current = 1;
	    cin>>str;
	    while(str[counter]!='\0'){
	        if(str[counter] == '-' && current == 1 ){
	            flips = flips + spareFlips+ 1;
	            current = -1;
	            spareFlips = 0;
	        }
	         else if(str[counter] == '+' && (current == -1 || (flips == 0 && spareFlips == 0))){
	            current = 1;
	            spareFlips++;
	        }
	        //cout<<str[counter];
	        counter++;
	    }
	    cout<<"\nCase #"<<index + 1<<": "<<flips;
	}
	return 0;
}