#pragma once
#include <iostream>
#include <string>

class Pancake {
public:
	Pancake(std::string s) : 
		pancake_init(s), 
		pancake_optimized(std::string("")) {};
	int getFlips();
	
private:
	//stack of pancake can optimize to only single "+" and "-" alternately
	//and bottom's "+" can be omited.
	void optimize();
	
private:
	const std::string pancake_init;
	std::string pancake_optimized;
};