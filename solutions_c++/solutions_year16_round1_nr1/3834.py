/*
 * LastWord.cpp
 *
 *  Created on: Apr 15, 2016
 *      Author: tushar
 */

#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

class FileOP{

	private:
		ifstream *m_fOpen;
		ofstream *m_fWrite;
		void vectorizefile(string fileName);


	public:
		~FileOP(){
					m_fWrite->close();
				}
		vector < string > m_vectorizedFile;
		FileOP(string fileName){
			vectorizefile(fileName);
			m_fWrite = new ofstream("Output.txt");
		}


		vector <string> getVectorizedFile(){ return m_vectorizedFile;}
		void printFileContents(vector<char> output, int casenum);

};

void FileOP::vectorizefile(string fileName)
{
	string lineInput;
	m_fOpen = new ifstream(fileName.c_str());
	if(m_fOpen->is_open()){
		while(getline(*m_fOpen,lineInput)){
			string line;
			m_vectorizedFile.push_back(lineInput);
		}


		m_fOpen->close();
	} else {
		cout << "Error opening file!"<<endl;
	}

}

void FileOP::printFileContents(vector<char> output, int casenum){

	stringstream ss;
	if(m_fWrite->is_open()){
		ss<<"Case #"<<casenum<<": ";
		for(int i=0;i<output.size();i++){
				ss<<output[i];
		}
		ss<<endl;

	}else {
		cout << "Error opening Output file!"<<endl;
	}
	*m_fWrite<<ss.str();
}

int main()
{
	FileOP *file= new FileOP("Input.txt");
	int caseNum =  0;
	caseNum = stoi(file->m_vectorizedFile[0]);
	for(int num = 1;num<=caseNum ;num++){
		string inputString = file->m_vectorizedFile[num];
		vector<char> lastWord;
		lastWord.push_back(inputString[0]);
		for(int letterNum=1;letterNum <inputString.size();letterNum++ ){
			int charVal = (int)inputString[letterNum];
			int testVal = (int)lastWord[0];
			if(charVal >= testVal){
				lastWord.insert(lastWord.begin(),(char)charVal);
			}
			else{
				lastWord.push_back((char)charVal);
			}


		}
		file->printFileContents(lastWord,num);

	}

	delete file;

	return 0;

}



