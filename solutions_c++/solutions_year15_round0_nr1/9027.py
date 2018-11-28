#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<time.h>
#include<algorithm>
using namespace std;
#define EVEN(n) (n%2 == 0)
#define MAX(m,n) ((m)>(n)?(m):(n))
#define RESULT_TYPE long long int
#define MODULE_DIVISOR 1000000009
#define INPUT_SIZE 1005
#define DEBUG 0
typedef struct Data {
	RESULT_TYPE x;
	RESULT_TYPE y;
}DATA;

typedef struct distance {
	RESULT_TYPE d;
	RESULT_TYPE fromIndex;
}Distance;

class ProcessTestcases {
	char input[INPUT_SIZE];
	RESULT_TYPE sMax;
	RESULT_TYPE res;
	RESULT_TYPE T;
	public:
		ProcessTestcases() {}
		void execute() {
			cin>>T;
			RESULT_TYPE i = 1;
			while(T>0) {
				T--;
				init();
				readInput();
				processQuery();
				outputResult(i);
				i++;
			}
		}
		void init() {
		}
		void readInput() {
			cin>>sMax;
			cin>>input;
		}
		void processQuery() {
			RESULT_TYPE audienceCount = 0;
			RESULT_TYPE newAudienceReq = 0;
			RESULT_TYPE audWithShyValueI;
			for (RESULT_TYPE i=0; i<=sMax; i++) {
				audWithShyValueI = input[i] - '0';
				if (audienceCount - i < 0) {
					newAudienceReq += (i - audienceCount);
					audienceCount += (i - audienceCount);
				} 
				audienceCount += audWithShyValueI;
			}
			res = newAudienceReq;
		}
		void outputResult(RESULT_TYPE i) {
			cout<<"Case #"<<i<<": "<<res<<endl;
		}
};

int main() {
	/*clock_t begin, end;
	double time_spent;
	begin = clock();*/

	ProcessTestcases p;//all testcases are handled in the constructor
	p.execute();
	
	/*end = clock();
	time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
	cout<<time_spent;*/
    return 0;
}


