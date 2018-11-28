#include <iostream>

using namespace std;

int main() {
	int length, i, number, multiplier, arrayIndex, lastNo, index, array[10], counter, found, value;
	cin>>length;
	for(index = 0; index < length; index++)
	{
	    counter = 1;
	    cin>> number;
	    
	    if(number == 0){
	        cout<<"\nCase #"<<index+1<<": INSOMNIA";
	    } else{
	        arrayIndex = 0;
	        multiplier = 0;
	        for(i = 0; i<10; i++){
	            array[i] = -1;
	        }
	        while(1) {
	            multiplier++;
	            value = number * multiplier;
	            while(value){
	                lastNo = value %10;
	                value = value / 10;
	                found = 0;
	                for(i = 0; i<10; i++){
	                    if(lastNo == array[i]){
	                        found=1;
	                    }
	                }
	                if(!found){
	                    array[arrayIndex] = lastNo;
	                    arrayIndex++;
	                }
	            }
	            if(arrayIndex == 10){
	                break;
	            }
	        }
	        cout<<"\nCase #"<<index+1 <<": "<<number * multiplier;
	    }
	}
	return 0;
}