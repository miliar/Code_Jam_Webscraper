#include <iostream>
#include <string>
#include <cstdio>
#include <vector>


using namespace std;

int countflip(string & input)
{
	size_t l = input.length();
	if(l == 1){
		if(input[0] == '+')
			return 0;	// only 1 '+' no flip
		else
			return 1;	// only 1 '-' flip once
	}
	else if(input[l-1] == '-'){
		int p1 = 0, p2 = 1;
		int count = 0;
		do{
			if(input[p1] != input[p2])
				count++;
			++p1;
			++p2;
		}while(p2 <= l-1);
		return ++count;	//because this ends with '-'
	}
	else if(input[l-1] == '+'){
		int p1 = 0, p2 = 1;
		int count = 0;
		do{
			if(input[p1] != input[p2])
				count++;
			++p1;
			++p2;
		}while(p2 <= l-1);
		return count;	
	}
	else
		return -1; //undefined error
}

int main()
{
	int casenum;
	cin >> casenum;
	getchar();
	
	vector<string> inputs(casenum);
	
	for(int k=0; k < casenum; ++k)
		getline(cin, inputs[k]);
	
	for(int k=0; k < casenum; ++k){
				
		int op = countflip( inputs[k] );
		cout << "Case #" << k+1
			<< ": " << op << endl;
	}
		
	return 0;
}
