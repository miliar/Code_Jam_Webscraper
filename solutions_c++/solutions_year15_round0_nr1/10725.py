#include "FileLoader.h"

#include <fstream>
#include <sstream>

FileLoader::FileLoader(){
}

FileLoader::FileLoader(std::string filename){
	loadFile(filename);
}

FileLoader::~FileLoader(){
	lines.clear();
}

void FileLoader::loadFile(std::string filename){
	std::ifstream file(filename);
	if (!file.is_open()){
		throw new FileLoaderException("The specified file could not be opened");
	}
	
	for (std::string line; std::getline(file, line); numLines++){
		lines.push_back(line);
	}
}

int FileLoader::getNumLines(){
	return numLines;
}

std::string FileLoader::getLine(int i){
	return lines[i];
}

std::vector<std::string> FileLoader::getLines(){
	return lines;
}

std::vector<std::string> FileLoader::split(std::string s, char d){
	std::stringstream ss(s);
	std::string i;
	std::vector<std::string> result;
	while (std::getline(ss, i, d)){
		result.push_back(i);
	}

	return result;
}


