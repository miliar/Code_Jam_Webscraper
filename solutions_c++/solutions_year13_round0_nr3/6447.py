#include <string>
#include <math.h>
#include <stdio.h>
#include <fstream>
#include <Windows.h>

using namespace std;

struct Limit {
	long start;
	long end;
	long output;
};

bool isSquare(long number,long &square) {
	float s ;   
	s = sqrt((float)number) ;   
	long ps = s ;   
	if (ps == s) {
		square = ps;
		return true;
	}
	return false;
}

bool isPalindrome(long number) {
	int digit;
	long rev=0;
	long n = number;
	while(n!=0) {
        digit = n%10;
        rev = (rev*10)+digit;
        n = n/10;
    }
    if(rev == number) {
		return true;
	}
	return false;
}

DWORD WINAPI FairAndSquare (LPVOID param) {
	struct Limit *limit = (struct Limit*)param;
	limit->output = 0;

	for(long i=limit->start;i<=limit->end;i++) {
		long square=0;
		if(isPalindrome(i)) {
			if(isSquare(i,square)) {
				if(isPalindrome(square)) {
					limit->output++;
				}
			}
		}
	}
	
	return 0;
}

int main() {

	int T;
	string input;
	char filename[50];

	printf("Enter the testcase filename: ");
	scanf("%s",filename);

	ifstream file(filename);

	if(file >> T) {
		printf("\nTestcase: %d\n",T);
	} else {
		printf("Invalid file\n");
		system("pause");
		return 0;
	}
	
	HANDLE *hThread = new HANDLE[T];
	struct Limit *board = new struct Limit[T];

	for(int i=0;i<T;i++) {
		
		//Reads Limit values
		file>>board[i].start;
		file>>board[i].end;
		printf("%ld %ld\n",board[i].start,board[i].end);
		hThread[i] = CreateThread( NULL,0,FairAndSquare,&board[i],0,0);
	}
	file.close();

	ofstream outfile("output.txt");

	printf("\nOutput\n");
	for(int i=0;i<T;i++) {
		char output[100];
		WaitForSingleObject( hThread[i], INFINITE );
		sprintf(output,"Case #%d: %d\n",i+1,board[i].output);
		printf("%s",output);
		outfile<<output;
		
	}
	
	outfile.close();

	system("pause");
	return 0;
}