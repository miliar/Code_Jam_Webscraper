/*
 * REVENGE OF THE PANCAKES
 * Google Code Jam 2016 - Qualification Round (Problem B)
 * 	by Yago González
 * 
 * Scans each array, having as loop invariant the fact that all the
 * elements behind the cursor have the same symbol, without mattering
 * whether it's a + or a -.
 * This way, whenever the cursor finds a cell which contains the
 * opposite symbol, let's say at cell i, flips the whole stack that goes
 * from 0 to i - 1, making the stack that goes from 0 to i homogeneous,
 * and keeping the loop invariant.
 * 
 * */

#include <iostream>
#include <fstream>
#include <string.h>

#define STACKSIZE	101	// Add 1 for the null terminator

using namespace std;

int main() {
	// Open the input/output files
	ifstream input ("B-large.in");
	ofstream output ("out.txt");
	
	unsigned short cases = 0, count = 0;
	input >> cases;
	
	string line;
		
	for(short c = 1; c <= cases; c++)  {
		count = 0;	// Reset the maneuvers counter
		
		char stack[STACKSIZE] = "";
		
		// String-to-array conversion of this case's input
		input >> line;
		strncpy(stack, line.c_str(), STACKSIZE);
		stack[STACKSIZE - 1] = 0;	// Add null terminator
		
		char current = stack[0];
		for(unsigned short i = 1; i < line.length(); i++) {
			if(stack[i] != current) {
				// Flip the whole pre-stack
				if(current == '+') {
					for(short j = 0; j < i; j++) {
						stack[j] = '-';
					}
				} else {
					for(short j = 0; j < i; j++) {
						stack[j] = '+';
					}
				}
				
				current = stack[i];	// Set the new current symbol
				count++;	// Add 1 to the amount of maneuvers
			}
		}
		
		// Final flip, in case the whole stack is now upside-down
		if(current == '-') {
			for(unsigned short i = 1; i < line.length(); i++) {
				stack[i] = '+';
			}
			count++;
		}
		
		output << "Case #" << c << ": " << count << "\n";
	}
	
	input.close();
	output.close();
}
