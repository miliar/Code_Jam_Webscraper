/*
 * SleepingSheep.cpp
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

class FileOP{

	private:
		bool m_isTokenize;
		string m_token;
		ifstream *m_fOpen;
		ofstream *m_fWrite;
		void vectorizefile(string fileName);


	public:
		~FileOP(){
					m_fWrite->close();
				}
		vector < vector<int> > m_vectorizedFile;
		FileOP(string fileName){
			m_isTokenize=false;
			m_token="";
			vectorizefile(fileName);
			m_fWrite = new ofstream("Output.txt");
		}
		FileOP(string fileName,string token){
			m_isTokenize=true;
			m_token=token;
			vectorizefile(fileName);
			m_fWrite = new ofstream("Output.txt");
		}

		vector < vector<int> > getVectorizedFile(){ return m_vectorizedFile;}
		void printFileContents(vector<int> output, int casenum);

};

void FileOP::vectorizefile(string fileName)
{
	string lineInput;
	m_fOpen = new ifstream(fileName.c_str());
	if(m_fOpen->is_open()){
		if(m_isTokenize){
			while(getline(*m_fOpen,lineInput)){
				vector<int> line;

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
				int sample;
				ss >> sample;
				while(ss)
				{
					line.push_back(sample);
					//sample.clear();
					ss >> sample;
				}
				m_vectorizedFile.push_back(line);
			}

		} /*else {
			while(getline(*m_fOpen,lineInput)){
				vector<int> line;

				line[0]=lineInput;
				m_vectorizedFile.push_back(line);
			}

		}*/
		m_fOpen->close();
	} else {
		cout << "Error opening file!"<<endl;
	}

}

void FileOP::printFileContents(vector<int> output, int casenum){

	stringstream ss;
	if(m_fWrite->is_open()){

		if(output[0] == 0){
			ss<<"Case #"<<casenum<<": INSOMNIA"<<endl;

		} else {
			ss<<"Case #"<<casenum<<": ";
			for(int i=0;i<output.size();i++){
					ss<<output[i];
			}
			ss<<endl;
		}
	}else {
		cout << "Error opening Output file!"<<endl;
	}
	*m_fWrite<<ss.str();
}


int main() {

	FileOP *file= new FileOP("Input.txt","");
	//file->printFileContents();
	int caseNum =  0;
	stringstream ss;
	for (int i=file->m_vectorizedFile[0].size()-1;i>=0;i--){
		caseNum+=file->m_vectorizedFile[0][i]*(pow(10,file->m_vectorizedFile[0].size()-1-i));
	}
	//Loop all test cases
	for(int num = 1;num<=caseNum ;num++){
		int set[10] ={0,0,0,0,0,0,0,0,0,0};
		int goldensum = 45;

		//Not Zero
		if(!(file->m_vectorizedFile[num].size()==1 && file->m_vectorizedFile[num][0] == 0)){
			int multiple=0;
			int testSum=0;
			//initial setup of checking digits and marking in array
			for(int i=0;i<file->m_vectorizedFile[num].size() ;i++){
				//First time marked
				if(set[file->m_vectorizedFile[num][i]] == 0){
					set[file->m_vectorizedFile[num][i]] = 1;
					testSum +=file->m_vectorizedFile[num][i];
				}
			}

			multiple=1;
			vector<int> result=file->m_vectorizedFile[num];
			while(testSum != goldensum || set[0]==0){
				++multiple;
				int carryFwd = 0;
				//Adding multiple
				for(int i=file->m_vectorizedFile[num].size()-1;i>=0;i-- ){
					int sum = result[i+(result.size()-file->m_vectorizedFile[num].size())] + file->m_vectorizedFile[num][i] + carryFwd;
					result[i+(result.size()-file->m_vectorizedFile[num].size())] = sum%10;

					if(set[sum%10] == 0){
						set[sum%10] = 1;
						testSum +=sum%10;
					}

					carryFwd = sum/10;

				}
				if(carryFwd !=0 ){
					for(int i=(result.size()-file->m_vectorizedFile[num].size()-1);i>=0;i++){

						int sum = result[i]+1;
						result[i] = sum%10;

						if(set[sum%10] == 0){
							set[sum%10] = 1;
							testSum +=sum%10;
						}

						if((sum/10) == 0){
							carryFwd = 0;
							break;
						}

					}
					if(carryFwd !=0){
						result.insert(result.begin(),1);
						if(set[1] == 0){
							set[1] = 1;
							testSum +=1;
						}
					}
				}
				//Finished adding multiple


			}


			file->printFileContents(result,num);

		} else{
			vector<int> dummy;
			dummy.push_back(0);
			file->printFileContents(dummy,num);

		}
	}


	delete file;

	return 0;
}
