#ifndef CASE_H
#define CASE_H

#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>

class Case
{
private:
	std::vector<std::string> lines;
	
	std::string* solution;
	
	// Traite les lignes du cas pour extraire les attributs du cas
	void extract_attributes();
	
	// Attributs à définir
	int premiere_reponse, seconde_reponse;
	std::vector<std::vector<int> > premier_align;
	std::vector<std::vector<int> > second_align;
	
public:
	Case(std::vector<std::string> _lines);
	
	static int to_int(std::string s);
	static std::vector< int > to_int_vector(const std::string& s);
	static std::vector< std::vector< int > > to_int(const std::vector< std::string >& v);
	
	// Retourne la chaine de solution à mettre devant "Case#1: "
	std::string resolve();
	
	friend std::ostream & operator<<(std::ostream & os, Case & c);
};

std::ostream & operator<<(std::ostream & os, Case & c);
std::ostream & operator<<(std::ostream & os, std::vector<Case> & v);

std::ostream & operator<<(std::ostream & os, const std::vector<int> & v);
#endif // CASE_H
