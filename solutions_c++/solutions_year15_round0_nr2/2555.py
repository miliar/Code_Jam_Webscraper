// Problem 2.cpp : Defines the entry point for the console application.
//

#include<vector>
#include<fstream>
#include<iostream>
#include<algorithm>
using namespace std;

int main(int argc, char* argv[])
{
	string inputfilename="input.txt";
	string outputfilename="output.txt";
	string outputdebugname="debug.txt";
	ifstream infile(inputfilename);
	ofstream OF(outputfilename);
	ofstream DBG(outputdebugname);
	int T;
	infile>>T;

	for(int icase=0;icase<T;icase++){
		int answer;
		int D;  //number of diners
		infile>>D;
		vector<int> p;
		int buf;
		for(int ip=0;ip<D;ip++){
			infile>>buf;
			p.push_back(buf);
		}
		sort(p.begin(),p.end());


		DBG<<"Case #"<<icase+1<<": ";
		for(int i=0;i<p.size();i++){
			DBG<<p[i]<<" ";
		}
		DBG<<":"<<endl;
		int min_iterations=INT_MAX;
		int nspecial=0;
		
		while(true){

			if(*max_element(p.begin(),p.end())>9) throw;

	
			if(min_iterations>*max_element(p.begin(),p.end())+nspecial) 
				min_iterations=*max_element(p.begin(),p.end())+nspecial;  //number of minutes remaining if there are no more special minutes
			


			int subt=0;
			if(p[p.size()-1]==9&&(p.size()>1?(p[p.size()-2]<7&&p[p.size()-2]!=5):true)){
				subt=3;
			}else{
				subt=*max_element(p.begin(),p.end())/2;
						//cout<<subt<<"	"<<*max_element(p.begin(),p.end())<<"	"<<p[p.size()-1]<<endl;
			}
	
			*max_element(p.begin(),p.end())-=subt;
			p.push_back(subt);
			nspecial++;
			if(*max_element(p.begin(),p.end())==1) break;
		}
		if(min_iterations<1||min_iterations>9) throw;

		OF<<"Case #"<<icase+1<<": "<<min_iterations<<endl;
		DBG<<min_iterations<<endl;

	}

		

	infile.close();
	OF.close();
	return 0;
}

