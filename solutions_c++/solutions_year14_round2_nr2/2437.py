#ifndef CASE_H
#define CASE_H

#include <vector>
#include <string>
#include <iostream>
#include <sstream>

class Case
{
private:
	std::vector<std::string> lines;
	
	std::string* solution;
	
	// Traite les lignes du cas pour extraire les attributs du cas
	void extract_attributes();
	
	// Attributs à définir
	int a;
	int b;
	int k;
	
public:
	Case(std::vector<std::string> _lines);
	
	// Retourne la chaine de solution à mettre devant "Case#1: "
	std::string resolve();
	
	friend std::ostream & operator<<(std::ostream & os, Case & c);
};

std::ostream & operator<<(std::ostream & os, Case & c);
std::ostream & operator<<(std::ostream & os, std::vector<Case> & v);
#endif // CASE_H
