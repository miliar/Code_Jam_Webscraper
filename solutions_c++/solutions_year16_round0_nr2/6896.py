/*

 * HappyPanCakes.cpp
 *
 *  Created on: Apr 8, 2016
 *      Author: tushar
 */
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

class FileOP1{

	private:
		bool m_isTokenize;
		string m_token;
		ifstream *m_fOpen;
		ofstream *m_fWrite;
		void vectorizefile(string fileName);


	public:
		~FileOP1(){
					m_fWrite->close();
				}
		vector < vector<string> > m_vectorizedFile;
		FileOP1(string fileName,string token){
			m_isTokenize=true;
			m_token=token;
			vectorizefile(fileName);
			m_fWrite = new ofstream("Output.txt");
		}

		vector < vector<string> > getVectorizedFile(){ return m_vectorizedFile;}
		void printFileContents(int output, int casenum);

};

void FileOP1::vectorizefile(string fileName)
{
	string lineInput;
	m_fOpen = new ifstream(fileName.c_str());
	if(m_fOpen->is_open()){
		if(m_isTokenize){
			while(getline(*m_fOpen,lineInput)){
				vector<string> line;

				//code to handle no space
				if(m_token.compare(" ")){
					if(m_token.compare("") == 0){
						stringstream ss;
						   ss << lineInput[0];
						   for (int i = 1; i < lineInput.size(); i++) {
						     ss << ' ' << lineInput[i];
						   }
						   lineInput = ss.str();
					} else {
						while(lineInput.find(m_token)!=string::npos){
							lineInput.replace(lineInput.find(m_token),1," ");
						}
					}
				}


				stringstream ss(lineInput);
				string sample;
				ss >> sample;
				while(ss)
				{
					line.push_back(sample);
					//sample.clear();
					ss >> sample;
				}
				m_vectorizedFile.push_back(line);
			}

		}
		m_fOpen->close();
	} else {
		cout << "Error opening file!"<<endl;
	}

}

void FileOP1::printFileContents(int output, int casenum){

	stringstream ss;
	if(m_fWrite->is_open()){

		ss<<"Case #"<<casenum<<": "<<output<<endl;

	}else {
		cout << "Error opening Output file!"<<endl;
	}
	*m_fWrite<<ss.str();
}


int main() {

	FileOP1 *file= new FileOP1("Input.txt","");
	int caseNum =  0;
	for (int i=file->m_vectorizedFile[0].size()-1;i>=0;i--){
		stringstream ss(file->m_vectorizedFile[0][i]);
		int s;
		ss>>s;
		caseNum+=s*(pow(10,file->m_vectorizedFile[0].size()-1-i));
	}
	//Loop all test cases
	for(int num = 1;num<=caseNum ;num++){
		int moves=0;
		vector<string> happyPanCakes;
		//Create perfect set to move backwards
		for(int i=0;i<file->m_vectorizedFile[num].size();i++) {
			happyPanCakes.push_back("+");
		}


		for(int i=file->m_vectorizedFile[num].size()-1;i>=0;i--) {
			if(file->m_vectorizedFile[num][i].compare(happyPanCakes[i]) != 0){
				fill(happyPanCakes.begin(),happyPanCakes.begin()+i,file->m_vectorizedFile[num][i]);
				++moves;

			}

		}
		file->printFileContents(moves,num);


	}

	delete file;
	return 0;
}



