//
//  main.cpp
//  TestA
//
//  Created by Nontawat on 4/11/2558 BE.
//  Copyright (c) 2558 Nontawat Klangpetch. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <sstream>

#define CASE_SIZE_POS 0

bool readFile(const std::string &_location,
			  std::vector < std::string > &_lines)
{
	std::ifstream _file (_location);
	if (!_file.is_open()) {
		std::cout << "Invalid file at location: " << _location << std::endl;
		return false;
	}
	
	std::string _line;
	while (getline(_file, _line))
	{
		_lines.push_back(_line);
	}
	return true;
}

bool writeFile(const std::string &_location,
			   const std::vector < std::string > &_lines)
{
	std::ofstream _file (_location);
	if (!_file.is_open()) {
		std::cout << "Invalid file at location: " << _location << std::endl;
		return false;
	}
	
	if (!_lines.empty()) {
		unsigned int i=0;
		_file << _lines[i++];
		for (; i<_lines.size(); i++) {
			_file << "\n" << _lines[i];
		}
	}
	_file.close();
	return true;
}

void strToken(std::vector < std::string > &_tokenList,
			  const std::string &_input,
			  const std::string _delim=",")
{
	if (_input.empty()) {
		return;
	}
	
	std::size_t _spos = 0;
	std::size_t _dpos = _input.find(_delim);
	while (1)
	{
		const std::string _str = _input.substr(_spos, (_dpos-_spos));
		_tokenList.push_back(_str);
		if (_dpos==std::string::npos) {
			break;
		}
		_spos = _dpos+1; // Next start position
		_dpos = _input.find(_delim, _spos);
	}
}

void strToken(std::vector < int > &_tokenList,
			  const std::string &_input,
			  const std::string _delim=",")
{
	std::vector < std::string > _list;
	strToken(_list, _input, _delim);
	_tokenList.resize(_list.size());
	for (unsigned int i=0; i<_list.size(); i++) {
		_tokenList[i] = atoi(_list[i].c_str());
	}
}

void strToken(std::vector < double > &_tokenList,
			  const std::string &_input,
			  const std::string _delim=",")
{
	std::vector < std::string > _list;
	strToken(_list, _input, _delim);
	_tokenList.resize(_list.size());
	for (unsigned int i=0; i<_list.size(); i++) {
		_tokenList[i] = std::stod(_list[i]);
	}
}

void strToken(std::set < std::string > &_tokenList,
			  const std::string &_input,
			  const std::string _delim=",")
{
	if (_input.empty()) {
		return;
	}
	
	std::size_t _spos = 0;
	std::size_t _dpos = _input.find(_delim);
	while (1)
	{
		const std::string _str = _input.substr(_spos, (_dpos-_spos));
		_tokenList.insert(_str);
		if (_dpos==std::string::npos) {
			break;
		}
		_spos = _dpos+1; // Next start position
		_dpos = _input.find(_delim, _spos);
	}
}

void parseCharactor(const std::string &_input,
					std::vector < std::string > &_result)
{
	_result.resize(_input.size());
	for (unsigned int i=0; i<_input.size(); i++) {
		_result[i] = _input[i];
	}
}

void parseCharactor(const std::string &_input,
					std::vector < int > &_result)
{
	std::vector < std::string > _list;
	parseCharactor(_input, _list);
	
	_result.resize(_list.size());
	for (unsigned int i=0; i<_list.size(); i++) {
		_result[i] = atoi(_list[i].c_str());
	}
}

int main(int argc, const char * argv[])
{
	const std::string _inputPath = "/Users/Non/Documents/Work/CodeJam2015/TestA/file/A-small-attempt5.in";
	const std::string _outputPath = "/Users/Non/Documents/Work/CodeJam2015/TestA/file/small-output.out";
	
	std::vector < std::string > _lines;
	if (!readFile(_inputPath, _lines)) {
		std::cout << "Read file failed" << std::endl;
		return 0;
	}
	
	if (_lines.empty()) {
		std::cout << "Invalid line" << std::endl;
		return 0;
	}
	
	int _currentLine = 0;
	const int _caseSize = atoi(_lines[CASE_SIZE_POS].c_str());
	_currentLine++;
	
	std::stringstream _ss;
	std::vector < int > _audience;
	std::vector < std::string > _tmp;
	std::vector < std::string > _result (_caseSize);
	for (int i=0; i<_caseSize; i++) {
//		std::cout << "Case #" << i+1 << ": " << _lines[_currentLine++] << std::endl;
		
		_tmp.clear();
		const std::string _line = _lines[_currentLine++];
		strToken(_tmp, _line, " ");
		if (_tmp.size()!=2) {
			std::cout << "Invalid line format: " << _line << std::endl;
			continue;
		}
		
		_audience.clear();
		parseCharactor(_tmp[1], _audience);
//		std::cout << "Case #" << i+1 << std::endl;
//		for (unsigned int j=0; j<_audience.size(); j++) {
//			std::cout << "_audience[" << j << "]: " << _audience[j] << std::endl;
//		}
		
		unsigned int _level = 0;
		unsigned int _totalAudience = _audience[_level];
		unsigned int _additionalAudience = 0;
		_level++;
		for (; _level<_audience.size(); _level++) {
			if (_audience[_level]==0) {
				continue;
			}
			
			if (_totalAudience<_level) { // Total audience is not enought add additional audience
//				std::cout << i << " level: " << _level << " total audience: " << _totalAudience << std::endl;
				_additionalAudience += _level - _totalAudience;
				_totalAudience += _additionalAudience;
			}
			_totalAudience += _audience[_level]; // Increase total audience by current level audience
		}
		
		_ss.str("");
		_ss << "Case #" << i+1 << ": " << _additionalAudience;
		_result[i] = _ss.str();
//		std::cout << "Case #" << i+1 << ": " << _additionalAudience << std::endl;
	}
	
	writeFile(_outputPath, _result);
	return 0;
}
