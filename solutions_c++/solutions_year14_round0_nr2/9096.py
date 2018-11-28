#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <iomanip>
#include <cstdlib>
using namespace std;

//C = farm cost
//F = extra cookies per second
//X = goal answer

long double C, F, X;

long double calculatetime() {
	long double rate = 2.0;
	long double timeelapsed = 0.0;
	while (true) {
		//cout << timeelapsed << " " << rate << "\n";
		long double farmbuytime, waittime, farmnextwaittime, timeafter;
		farmbuytime = C / rate;
		waittime = X / rate;
		farmnextwaittime = X / (rate + F);
		timeafter = X / (rate + F + F);
		if (farmbuytime < waittime && farmnextwaittime + farmbuytime < waittime) {
			timeelapsed += farmbuytime;
			rate += F;
		} else {
			timeelapsed += waittime;
			return timeelapsed;
		}
	}
}

int main() {
	int numcase;
	cin >> numcase;
	for (int master = 0; master < numcase; master++) {
		cout << "Case #" << master + 1 << ": ";
		//cost of farm, increase in rate, goal cookies
		cin >> C >> F >> X;
		long double mintime = calculatetime();
		cout << setprecision(7) << fixed << mintime << "\n";
	}
}

/*
long double calculatetime(long double rate, long double timeelapsed, long double amount) {
	//cout << rate << " " << timeelapsed << " " << amount << "\n";
	//check if we have answer or we made miscalclation
	if (amount >= X - 10e-6 && amount <= X + 10e-6) {
		//cout << worstmaxtime << "\n";
		if (timeelapsed < worstmaxtime)
			worstmaxtime = timeelapsed;
		return timeelapsed;
	}
	if (timeelapsed > worstmaxtime) return -1.0;
	if (rate > X) {
		if (timeelapsed < worstmaxtime)
			worstmaxtime = timeelapsed;
		return timeelapsed;
	}
	//buy a farm as soon as we can
	//or wait until we hit X
	long double farmbuytime, waittime;
	long double farmans, waitans;

	farmbuytime = (C - amount) / rate;
	if (farmbuytime < 0) {
		farmbuytime = 0;
		farmans = calculatetime(rate + F, timeelapsed + farmbuytime, amount - C);
	} else {
		farmans = calculatetime(rate + F, timeelapsed + farmbuytime, 0);
	}

	waittime = (X - amount) / rate;
	waitans = calculatetime(rate, timeelapsed + waittime, amount + waittime * rate);

	if (farmans < 0) {
		if (waitans < worstmaxtime) worstmaxtime = waitans;
		return waitans;
	}
	if (waitans < 0) {
		if (farmans < worstmaxtime) worstmaxtime = farmans;
		return farmans;
	}
	if (worstmaxtime > min(waitans, farmans))
		worstmaxtime = min(waitans, farmans);
	return min(waitans, farmans);
}
*/