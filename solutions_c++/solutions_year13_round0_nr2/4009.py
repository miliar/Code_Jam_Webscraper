//============================================================================
// Name        : test.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <boost/algorithm/string.hpp>

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>

#include <stdlib.h>

#include "Number.h"

class ProblemB {
public:
	ProblemB() {
	}

	std::vector<bool> getTmpResult(int M){
		std::vector<bool> tmpResult;
		for(int i = 0 ; i <M; i++){
			tmpResult.push_back(false);
		}
		return tmpResult;
	}

	void analyseHorizontal(std::vector<std::vector<int> > & tc, int N, int M,
			std::vector<std::vector<bool> > & result) {
		// pour chaque ligne
		for (int i = 0; i < N; i++) {
			std::vector<bool> lineResult;
			std::vector<int> & vec = tc[i];
			if(analyseList(vec, M, lineResult)){
				for(int j = 0; j < M; j++){
					result[i][j] = result[i][j] ||lineResult[j];
				}
			}
		}
		//en prennant par  la droite
		if(M > 1){
			for (int i = 0; i < N; i++) {
				std::vector<bool> lineResult;
				std::vector<int> vec;
				for(int j = M-1; j >= 0; j--){
					vec.push_back(tc[i][j]);
				}
				if(analyseList(vec, M, lineResult)){
					for(int j = 0; j < M; j++){
						result[i][j] = result[i][j] ||lineResult[M-j-1];
					}
				}
			}
		}


	}

	void analyseVertical(std::vector<std::vector<int> > & tc, int N, int M,
			std::vector<std::vector<bool> > & result) {
			// pour chaque colonne
			for (int i = 0; i < M; i++) {
				std::vector<bool> lineResult;
				std::vector<int> vec;
				for(int j = 0; j < N; j++){
					vec.push_back(tc[j][i]);
				}
				if(analyseList(vec, N, lineResult)){
					for(int j = 0; j < N; j++){
						result[j][i] = result[j][i] ||lineResult[j];
					}
				}
			}
			//par en bas
			if(N>1){
				for (int i = 0; i < M; i++) {
					std::vector<bool> lineResult;
					std::vector<int> vec;
					for(int j = N-1; j >= 0; j--){
						vec.push_back(tc[j][i]);
					}
					if(analyseList(vec, N, lineResult)){
						for(int j = 0; j < N; j++){
							result[j][i] = result[j][i] ||lineResult[N-j-1];
						}
					}
				}
			}
		}

	//analyse une serie de nombre, il faut la liste correspondent a un suite de nombre inferieur ou
	//egale au premier de la serie
	bool analyseList(std::vector<int> & list, int size, std::vector<bool> & result){
		int first = *(list.begin());
		return analyseList_rec(list, size, result, first);

	}

	bool analyseList_rec(std::vector<int> & list, int size, std::vector<bool> & result, int tondeuseSize){
		//reinit result
		result = getTmpResult(size);
		for (int j = 0; j < size; j++) {
			if (tondeuseSize == list[j]) {
				result[j] = true;
			}
			//il y a une valeur superieur a la premiere de la liste
			//on reprend avec cette valeur
			if (list[j] > tondeuseSize) {
				return analyseList_rec(list, size, result, list[j]);
			}
		}
		return true;
	}



	std::vector<std::vector<bool> > getResultTab(int N, int M) {
		std::vector<std::vector<bool> > result;
		for (int i = 0; i < N; i++) {
			result.push_back(std::vector<bool>());
			std::vector<bool> & vec = result[i];
			for (int j = 0; j < M; j++) {
				vec.push_back(false);
			}
		}
		return result;
	}

	bool checkResult(std::vector<std::vector<bool> > & result, int N, int M) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				std::cout << result[i][j];
				if (result[i][j] == false) {
					std::cout << std::endl;
					return false;
				}
			}
			std::cout << std::endl;
		}
		return true;
	}

	std::string analyse(std::vector<std::vector<int> > & tc, int N, int M) {
		std::vector<std::vector<bool> > result = getResultTab(N, M);
		checkResult(result, N, M);
		analyseHorizontal(tc, N, M, result);
		analyseVertical(tc, N, M, result);
		if (checkResult(result, N, M)) {
			return "YES";
		} else {
			return "NO";
		}
	}
};

typedef std::deque<std::pair<int, bool> > deque_res;

int main(int argc, char* argv[]) {

	if (argc == 3) {

		//fichier d'entre
		std::fstream inputFile;
		inputFile.open(argv[1]);

		//lecture nombre de test case
		std::string sNb;
		std::getline(inputFile, sNb);
		int nb = Number::getInt(sNb);

		//fichier de sortie
		std::fstream outputFile;
		outputFile.open(argv[2], std::fstream::out);

		ProblemB pb;

		//pour chaque test case ou si l'on a atteint la fin du fichier
		for (int i = 0; (i < nb) && (inputFile.eof() == false); i++) {

			std::cout << "tc " << i << std::endl;
			//std::vector<std::string> svLine;
			std::vector<std::vector<int> > tc;

			std::string sLine;
			std::getline(inputFile, sLine);
			std::vector<int> NM = Number::getInts(sLine);

			//lecture de chaque ligne
			for (int j = 0; j < NM[0]; j++) {
				std::string sLine;
				std::getline(inputFile, sLine);

				if (sLine.empty()) {
					std::cout << "errr empty line in test case" << std::endl;
				}

				tc.push_back(Number::getInts(sLine));

			}
			outputFile << "Case #" << (i + 1) << ": "
					<< pb.analyse(tc, NM[0], NM[1]) << std::endl;

		}
		outputFile.close();
		std::cout << "ok" << std::endl;
	} else {
		std::cout << "invalid number of parameter " << std::endl;
	}
	return 0;
}
