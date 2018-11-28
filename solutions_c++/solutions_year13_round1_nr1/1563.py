/*
 * File:   main.cpp
 * Author: hawkwing
 *
 * Created on April 26, 2013, 7:47 PM
 */

#include <fstream>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int main(){
	ifstream in("A-small.in");
	ofstream out("A-small.out");
	int T;
	in >> T;
	for(int i=0;i<T;i++){
		unsigned long paint,radius,rings=0;
		in >> radius >> paint;
		radius+=1;//radius of first ring
		//ring area=pi*r**2-pi*(r-1)**2=pi*(2*r-1)=2*r-1 paint
		while(paint>=2*radius-1){
			paint-=2*radius-1;
			rings++;
			radius+=2;
		}
		out << "Case #" << i+1 << ": " << rings << std::endl;
	}
}