#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <functional>

using namespace std;


const string PATH = "C:/ws/vs_projects/GoogleCodeJam2014/Files/";
const string FILENAME = "B-small-attempt1";

struct Budget {
	Budget() {}
	Budget(double current, double seconds, double cookieProduction) :
		cookies(current), seconds(seconds), cookieProduction(cookieProduction) { }
	double cookies;
	double seconds;
	double cookieProduction;
};

bool operator>(const Budget& a, const Budget& b) {
	return a.seconds > b.seconds;
}


int main() {
	ifstream fin(PATH + FILENAME + ".in");
	ofstream out(PATH + FILENAME + ".out");
	out << fixed;
	int T, t;
	double C, F, X, timeNextStep;
	priority_queue<Budget, vector<Budget>, greater<Budget>> pqueue;
	fin >> T;
	
	t = T;
	while (--t >= 0) {
		pqueue = priority_queue<Budget, vector<Budget>, greater<Budget>>();
		
		pqueue.push(Budget(0.0f,0.0f, 2.0f));
		
		fin >> C >> F >> X;
		Budget current;
		while ((current = pqueue.top()).cookies < X) {
			pqueue.pop();
			
			// possible by just clicking until win
			timeNextStep = (X - current.cookies) / current.cookieProduction;
			pqueue.push(Budget(
				current.cookies + (current.cookieProduction * timeNextStep), // total cookies
				current.seconds + timeNextStep, // total seconds
				current.cookieProduction)); 
			
			
			// possible by going with building production			
			timeNextStep = (C - current.cookies) / current.cookieProduction;								
			pqueue.push(Budget(
				current.cookies + (current.cookieProduction * timeNextStep) - C, // total cookies
				current.seconds + timeNextStep,  // total seconds				
				current.cookieProduction + F));
		}

		// Output:
		
		out << "Case #" << (T - t) << ": ";
		out << current.seconds;
		out << "\n";
	}

	
	return 0;
}