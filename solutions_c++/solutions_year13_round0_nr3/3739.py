#include <iostream>
#include <string>
#include <vector>
#include <cmath>


using namespace std;



vector<string> split(string sent)
{
	if(sent.size() < 1)
		return vector<string>();
	vector<string> answer;
	
	int start = 0, end = 0;
	char delim = ' ';
	
	while( (end = sent.find(delim, start)) != string::npos) {
		string curSubstr = sent.substr(start, end-start);
		if(curSubstr.size() > 0)
			answer.push_back(curSubstr);
		start = end + 1;
	}
	string endSubstr = sent.substr(start, sent.size()-start);
	if(endSubstr.size() > 0)
		answer.push_back(endSubstr);
	return answer;
}



int myLg(int n) {
	if(n < 10)
		return 0;
	return 1 + myLg(n / 10);
}


bool isPalind(int n, int lg) {
	if(lg == 0)
		return true;

	vector<int> digits = vector<int>(lg + 1, -1);
	int curN = n;
	for(int i = 0; i <= lg; ++i) {
		digits[i] = curN % 10;
		curN /= 10;
	}
	int halfLg = (lg + 1) / 2;
	for(int i = 0; i < halfLg; ++i)
		if(digits[i] != digits[lg - i])
			return false;
	return true;
}


bool givesFNS(int n) {
	int nSq = n * n;
	int lgSq = myLg(nSq);
	int lg = (lgSq + 1) / 2;
	bool isPal = isPalind(n, lg);
	bool sqIsPal = isPalind(nSq, lgSq);
	if(isPal && sqIsPal)
		return true;
	else
		return false;
}




// Upper integer part of sq root
int uSqRoot(int n) {
	int sqRoot = (int) sqrtf((float)n);
	if(sqRoot * sqRoot < n)
		return sqRoot + 1;
	else
		return sqRoot;
}

// Lower integer part of sq root
int SqRoot(int n) {
	return (int) sqrtf((float) n);
}



int countFNS(int a, int b) {
	int count = 0;
	for(int i = a; i <= b; ++i) {
		if(givesFNS(i))
			++count;
	}
	return count;
}



void printAnswer(int ti, int number) {
	cout << "Case #" << ti << ": " << number << endl;
}




int main()
{
	freopen("C-small-attempt0.txt", "rt", stdin);
	freopen("out-C-small-attempt0.txt", "wt", stdout);
	
	string readLine;

	// Number of tests
	int T;
	getline(cin, readLine);
	T = atof(readLine.c_str());
	
	for(int ti = 1; ti <= T; ++ti) {
		// A min possible number, B max
		int A, B;
		getline(cin, readLine);
		vector<string> numbers = split(readLine);
		A = atof(numbers[0].c_str());
		B = atof(numbers[1].c_str());
		int a = uSqRoot(A);
		int b = SqRoot(B);

		int count = countFNS(a, b);
		printAnswer(ti, count);

	}
	return 0;
}