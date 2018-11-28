#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main() {
	int numCases;
	cin >> numCases;
	
	for(int x = 1; x <= numCases; x++) {
		int maxShyness;
		string counts;
		cin >> maxShyness >> counts;
		
		int numCounts = maxShyness + 1;
		int standing = 0;
		int added = 0;
		for(int level = 0; level < numCounts; level++) {
			if(standing < level) {
				int diff = level - standing;
				added += diff;
				standing += diff;
			}
			standing += (counts[level] - '0');
		}
		
		cout << "Case #" << x << ": "; 
		cout << added;
		cout << "\n";
	}
}
