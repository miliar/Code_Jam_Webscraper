//postfix calculator

#include <iostream>
#include <vector>
#include <utility> 
#include <algorithm>
#include <fstream>
#include <set>

using namespace std;

double v, cookies, sec, c, f, tests, goal;


void buildFarm() {
	cookies -= c;
	v += f;
}

double timeWithNewFarm() {
	return (goal / (v + f)) + ((c-cookies)/v);
}

double timeGoal() {
	return (goal - cookies) / v;
}

//returns true if goal is reached
bool next() {
	/*cout << " secs: " << fixed << sec << " cookies " << fixed << cookies << " speed " << v << endl;
	cout << "time new Farm: " << fixed << timeWithNewFarm();
	cout << " time goal : " << fixed << timeGoal() << endl << endl; */
	if ((goal - cookies) <= (c - cookies) || timeWithNewFarm() >= timeGoal() )   {
		sec += (goal - cookies) / v;
		return true;
	} else {
		sec += (c - cookies) / v;
		cookies += c - cookies;
		buildFarm();
		return false;
	}
}

int main() {
    ofstream fOutput;
    fOutput.open ("rBig.out");
    fOutput.precision(7);
    cin >> tests;
	for (int i = 1; i <= tests; i++) {
        v = 2; sec = 0; cookies = 0;
        cin >> c;
        cin >> f;
        cin >> goal;

        double t = 0, o;
        while (!next());

        fOutput << "Case #" << i << ": ";
        fOutput << fixed << sec << endl;
    }

    return 0;
}
