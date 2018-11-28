#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <sstream>
#include <vector>
#include <sstream>

using namespace std;


int main()

{
    freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);

    int N,counter=0;
    cin >> N;
    string stack;
    getline(cin, stack);
	for (int caseN = 1; caseN <= N; ++caseN) {
		counter = 0;
		getline(cin, stack);
		if(stack.length() > 1) {
			for(unsigned i=0; i< stack.length()-1 ; ++i) {
				if ( stack.at(i) != stack.at(i+1) )
					counter++;
			}
			
			if (stack.at(stack.length()-1) == '-')
				counter++;
		}
		
		else if (stack.compare("-") == 0)
			counter++;
			
		
			
		
		cout << "Case #" << caseN << ": " << counter << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;

}
