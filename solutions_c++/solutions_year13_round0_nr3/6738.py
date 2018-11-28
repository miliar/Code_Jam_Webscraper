#include <iostream>
#include <fstream>
#include <string>

#include <cstring>
#include <cmath>

using namespace std;
int pri(long int pri){
	/*
	int digis = 0;
	int temp = i;
	do{
		temp /= 10;
		digis++;
	}while (temp);
	int digit = digis;
	for ( ; digis < digis / 2; digis--){
		if (i / (int) pow(10.0, digis) == i % 10) {
			i /= 10;
			continue;
		}
		return 0;
	}
	return 1;
	*/
	char ch[100];
	sprintf(ch,"%d",pri);
	int i, n;
	n = strlen(ch);
	for(i=0; i < n/2; i++) {
      if(ch[i] != ch[n-1-i]) break;
	}
	return i == n / 2;
} 



int main() {
    ofstream fout ("C-small-attempt0.out");
    ifstream fin ("C-small-attempt0.in");
    int time;
	long int lower_limit, upper_limit;
    fin >> time;
	// input
	for (int k = 0; k < time; k++){
		int count = 0;
		fin >> lower_limit >> upper_limit;

		int i = sqrt(lower_limit);
		if (i * i != lower_limit) i++;
		if (i * i > upper_limit) goto out;	
		do{
		 	if (pri(i * i) && pri(i)) count++;
			i++;
		}while(i * i <= upper_limit);
		out: ;
		fout << "Case #" << k + 1 << ": " << count << endl;
	}
	return 0;
}

