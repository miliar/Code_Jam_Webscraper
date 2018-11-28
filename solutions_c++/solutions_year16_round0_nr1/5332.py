#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <vector>
using namespace std;
bool present(int val, vector<long> &yay){
	for (long i=0; i<yay.size();i++){
		if (yay[i] == val){
			return true;
		}
		
	}
	return false;
}
long sleepChecker(long value){
	bool loopcheck = true;
	long value_temp;
	long stored_val;
	int a=0;
	vector<long> remembered_values;
	
	while (loopcheck){
		
		value_temp = (a+1)*value;
		stored_val = value_temp;
		
	if (value_temp == 0){
		return 0;
	}
	else if (value_temp>0){
		while (value_temp > 0){
			int temp = value_temp%10;
			if (present(temp, remembered_values)==0){
				remembered_values.push_back(temp);
				
				value_temp = value_temp/10;
			}
			else{
				value_temp=value_temp/10;
				
			}
		}
					if (remembered_values.size() == 10){
		
		return stored_val;
	}
	else{
		a++;
	}
	}

	}
}

int main()
{
	FILE *fin = freopen("A-large.in", "r", stdin);
    assert(fin!=NULL);
    FILE *fout = freopen("A-large.out", "w", stdout);
    long output;
    long num_test_cases;
    cin >> num_test_cases;
    for (long i =0;i<num_test_cases;i++){
    	long entry;
    	cin >> entry;
    	
    	output = sleepChecker(entry);
    	if (output ==0){
    		cout << "Case #" << i+1 << ": " << "INSOMNIA\n" ; 
    	}
    	else{
    		cout << "Case #" << i+1 << ": " << output << endl;
    	}
    }
}