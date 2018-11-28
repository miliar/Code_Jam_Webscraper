//#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <map>
#include <algorithm>
using namespace std;

bool shouldRedist(map<int,int>& pancakes2diners);
int maxPancakes;

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T;
	in >> T;
	for (int t=0; t <T; t++) {
		int numDiners;
		in >> numDiners;
		map<int, int> pancakes2diners;
		for (int i =0; i <= 1000; i++)
			pancakes2diners[i] = 0;
		for (int i=0; i < numDiners; i++) {
			int pancs;
			in >> pancs;
			pancakes2diners[pancs]++;
		}
		typedef map<int,int>::iterator iter;
		for (int i = 0; i <= 1000; i++) {
			if (pancakes2diners[i] == 0)
				pancakes2diners.erase(i);
		}

		/*
		int time=0;
		while (!pancakes2diners.empty()) {
			while(shouldRedist(pancakes2diners)) {
				time++;
			}

			//let's eat
			pancakes2diners.erase(1);
			bool eraseNext = false;
			for (int p=2; p <= maxPancakes+1; p++) {
				if (pancakes2diners.find(p) != pancakes2diners.end()) {
					pancakes2diners[p-1] = pancakes2diners[p];
					eraseNext = true;
				}
				else if(eraseNext) {
					pancakes2diners.erase(p-1);
					eraseNext = false;
				}
			}
			time++;
			
		}*/
		int bestTime = std::max_element(pancakes2diners.begin(), pancakes2diners.end())->first;
		for (int height=1; height <bestTime; height++) {
			int time = height;
			for (iter i = pancakes2diners.begin(); i != pancakes2diners.end(); i++) {
				time += ((i->first - 1)/height) * i->second;
				if (time >= bestTime) break;
			}
			if (time < bestTime) bestTime = time;
		}




		out << "Case #" << t+1 << ": " << bestTime << endl;
	} //case
} //main

bool shouldRedist(map<int,int>& pancakes2diners) {
	maxPancakes = std::max_element(pancakes2diners.begin(), pancakes2diners.end())->first;
	int people = pancakes2diners.size();
	int saved = maxPancakes/2;
	if (saved > people) { //redist
		if (pancakes2diners[maxPancakes] > 1)
			pancakes2diners[maxPancakes]--;
		else {
			pancakes2diners.erase(maxPancakes);
		}
		if(pancakes2diners.find(maxPancakes/2) != pancakes2diners.end()) {
			pancakes2diners[maxPancakes/2]++;
		}
		else {
			pancakes2diners[maxPancakes/2] = 1;
		}
		if(pancakes2diners.find(maxPancakes - maxPancakes/2) != pancakes2diners.end()) {
			pancakes2diners[maxPancakes - maxPancakes/2]++;
		}
		else {
			pancakes2diners[maxPancakes - maxPancakes/2] = 1;
		}
		return true;
	}
	else {
		return false;
	}
}