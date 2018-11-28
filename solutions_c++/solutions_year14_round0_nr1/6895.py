// a_magic_trick.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <sstream>
#include<fstream>
#include<vector>
#include <iterator>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream myReadFile;
	myReadFile.open("A-small-attempt1.in",std::ifstream::in);

	ofstream outputFile;
    outputFile.open("out.txt");


	string output;
	int numberTC = 0 ;
	int answerTC = 0 ;
	int line = 0 ;
	int indexTC = 1 ;
	vector<string> tokens1;
	vector<string> tokens2;
	char * pEnd;
	if(myReadFile.is_open()){
		while(!myReadFile.eof()){
			//cout<<"test"<<endl;
			//myReadFile >> output;
			std::getline(myReadFile,output);
			//cout<<output<<endl;
			if (numberTC == 0){
				numberTC = atoi(output.c_str());
			}else if (answerTC == 0 ){
				   answerTC = (int)strtol(output.c_str(),&pEnd,10);
					//cout<<"answer of tc is "<<answerTC<<endl;
					//cout<<">>>>>line is "<<line<<endl;
					continue;
			}else{
				line++;
				//cout<<"line is "<<line<<endl;
				if ( (line % 4) == (answerTC%4)){ 
					//cout<<"answer line "<<endl;
					if( line<=4 ){
						 stringstream temp(output);
						 copy(istream_iterator<string>(temp),
								istream_iterator<string>(),
								back_inserter<vector<string> >(tokens1));
					}
					else{
						   stringstream temp(output);
						   copy(istream_iterator<string>(temp),
								istream_iterator<string>(),
								back_inserter<vector<string> >(tokens2));

						 //  vector<string>::iterator tokenIterator1;
						 //  vector<string>::iterator tokenIterator2;
						  vector<string>::iterator answerToken;
						  bool answerFound = false;
						  bool duplicate = false ;
						   for (auto tokenIterator1 = tokens1.begin(); tokenIterator1 != tokens1.end(); ++ tokenIterator1){
							   for (auto tokenIterator2 = tokens2.begin(); tokenIterator2 != tokens2.end(); ++ tokenIterator2){
								   if( * tokenIterator1 == *tokenIterator2  ){
									   if ( !answerFound){
									       answerToken = tokenIterator1;
										   answerFound = true;
									   }
									   else{
										   duplicate = true ;
										   break;
									   }										   
									 //  cout<<"Case #"<<indexTC<<": "<<*tokenIterator1<<endl;
								   }
							   }				     
						   }
						   if(duplicate )
						       outputFile<<"Case #"<<indexTC<<": Bad magician!"<<endl;
						   else if(answerFound)
						       outputFile<<"Case #"<<indexTC<<": "<<*answerToken<<endl;
						   else
							   outputFile<<"Case #"<<indexTC<<": Volunteer cheated!"<<endl;
					}
				}
				if ( line % 4 == 0 )
					answerTC = 0 ;
			    if (line /4 == 2){
					line = 0 ;
					indexTC++;
					tokens1.clear();
					tokens2.clear();
			    }
		   }
			
		}
	}
	system("pause");
	return 0;
}
