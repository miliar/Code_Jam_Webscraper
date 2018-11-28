// magic.cpp : Defines the entry point for the console application.
//

#include <iostream>

using namespace std;

float compute(float C, float F, float X){
	int n=0;
	float t=0;
	float t_1=0;
	float T=0;
	for(;;){
	t=X/(2+n*F);
	t_1=C/(2+n*F)+X/(2+(n+1)*F);
	if(t_1>t) {T=T+t; break;}
	else {T=T+C/(2+n*F); n++;}
	}
	return T;
}
void test(int i){
	float C,X,F;
	cin >> C;
	cin >> F;
	cin >> X;
	float t=compute(C,F,X);
	cout << "Case #"<<i<<": "<<t<< endl;
}
int main(int argc, char* argv[])
{
	int testcases;
	cin >>testcases;

	cout.precision(8);
	for(int i=0;i<testcases;i++){
		test(i+1);
	}

	return 0;
}

