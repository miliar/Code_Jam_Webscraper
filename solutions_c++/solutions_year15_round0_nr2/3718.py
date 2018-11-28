#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>


using namespace std;
int pancakes(float num){
    int jNum = (int)num;
    if (num == (float)jNum) {
        return jNum;
	}  
    return jNum + 1;
}


int main() {
	long long int  p, k, singham, max_k = -1, answer, min_answer, i;
	std::vector<int> intVector;
	cin >> i;
	for (int l=1; l<=i;l++)
	{	
		cin >> p;
		singham = p;
		intVector.clear();
		answer = 0;
		while (singham--)
		{	
			cin >> k;
			intVector.push_back(k);
			if (k > max_k)
				max_k = k;
		}
		for (int j=1;j<=max_k;j++){	
			answer = 0;
			for (int l=0; l<p; l++){
				answer = answer + pancakes(intVector[l]*1.0/j) - 1;
			}
			answer = answer + j;
			if (j == 1)		min_answer = answer;
			if (answer < min_answer)		min_answer = answer;
		}
		cout << "Case #" << l << ": " << min_answer << endl;
	}
	return 0;
}
