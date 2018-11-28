/*
 * flippingPancakes.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: jpaone
 */

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

const bool DEBUG = false;

bool inOrder( char *stack, int top, int bottom );
int runPancakes( char *stack, int top, int bottom );
void flipPancakes( char *stack, int top, int bottom );
void invertPancakes( char *stack, int top, int bottom );
void reversePancakes( char *stack, int top, int bottom );
void printStack( char *stack, int top, int bottom );

int main( int argc, char *argv[] ) {

	int T;
	cin >> T;

	for( int i = 1; i <= T; i++ ) {

		string pancakeStack;
		cin >> pancakeStack;

		cout << "Case #" << i << ": " << flush;

		char *pancakes = (char*)pancakeStack.c_str();

		int flipCount = runPancakes( pancakes, 0, pancakeStack.length()-1 );

		cout << flipCount << endl;
	}

	return 0;
}

bool inOrder( char *stack, int top, int bottom ) {
	for( int i = top; i <= bottom; i++ ) {
		if( stack[i] == '-' ) {
			return false;
		}
	}
	return true;
}

int runPancakes( char *stack, int top, int bottom ) {
	int count = 0;

	if (DEBUG) cout << "\nstarting: " << endl;
	if (DEBUG) printStack( stack, top, bottom );

	if( bottom < top ) {
		return count;
	}

	if( !inOrder( stack, top, bottom ) ) {
		if( stack[top] == '+' ) {
			int flippingPoint = top;
			while( stack[flippingPoint] == '+' ) {
				flippingPoint++;
			}
			if (DEBUG) cout << "top is +, flipping top " << flippingPoint-1 << " pancakes";
			flipPancakes( stack, top, flippingPoint-1 );
			count++;
			count += runPancakes( stack, top, bottom );
		} else {
			int flippingPoint = bottom;
			while( stack[flippingPoint] == '+' ) {
				flippingPoint--;
			}
			flipPancakes( stack, top, flippingPoint );
			count++;
			while( stack[flippingPoint] == '+' ) {
				flippingPoint--;
			}
			count += runPancakes( stack, top, flippingPoint );
		}
	}

	return count;
}

void flipPancakes( char *stack, int top, int bottom ) {
	if (DEBUG) cout << "Preinvert: " << endl;
	if (DEBUG) printStack( stack, top, bottom );
	invertPancakes( stack, top, bottom );
	if (DEBUG) cout << "Prereverse: " << endl;
	if (DEBUG) printStack( stack, top, bottom );
	reversePancakes( stack, top, bottom );
	if (DEBUG) cout << "Postflip: " << endl;
	if (DEBUG) printStack( stack, top, bottom );
}

void invertPancakes( char *stack, int top, int bottom ) {
	for( int i = top; i <= bottom; ++i ) {
		if( stack[i] == '+' ) {
			stack[i] = '-';
		} else {
			stack[i] = '+';
		}
	}
}

void reversePancakes( char *stack, int top, int bottom ) {
	for( int i = top; i <= bottom / 2; ++i ) {
		char temp = stack[i];
		stack[i] = stack[ bottom - i ];
		stack[ bottom - i ] = temp;
	}
}

void printStack( char *stack, int top, int bottom ) {
	cout << "\tPrinting Stack[" << top << ":" << bottom << "]: ";
	for( int i = top; i <= bottom; i++ ) {
		cout << stack[i];
	}
	cout << endl;
}
