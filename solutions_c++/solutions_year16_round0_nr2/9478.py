#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <math.h>
using namespace std;
vector<int> charToNum(string input){
	vector<int> out;
	for(int i=0;i<input.size();i++){
		if(input[i]=='+'){
			out.push_back(1);
		}
		else{
			out.push_back(0);
		}

	}
	return out;
}
vector <int> vectorInvers(vector<int> input,int k){
	vector<int> part;
	vector<int> out;
	out=input;
	for(int i=0;i<k;i++){
		out[i]=1-input[k-1-i];
	}
	return out;
}
vector<int> vectorChanger(vector<int> input){
	vector<int> in;
	int count=1;
	vector<int> allOne;
	in=input;
	for(int i=0;i<in.size();i++){
		allOne.push_back(1);
	}
	int turn=0;
	int first=in[0];

	for(int i=1;i<input.size();i++){
		//cout<<"first"<<first<<"input"<<input[i]<<endl;
		if(first==in[i]){
			count++;
			//cout<<"count"<<count<<endl;
		}
		else{
			break;
		}
	}
	for(int j=0;j<count;j++){
		in[j]=1-in[j];
	}
	/*	for(int i=0;i<in.size();i++)
	{
			cout<<in[i];
	}*/
	turn++;
	return in;

}
//return count;


/*vector <int> actionNumber(vector<int>input,int number){
	vector<int>in;
	in=input;
	count=0;
	for(int i=0;i<number;i++){
		for(int j=0;j<in.size();j++){
			vectorInvers(in,j);
		}
	}
}*/
int main() {
	ifstream iFile("/home/mehdi/workspace/binary/src/B-large.in");
	freopen("/home/mehdi/workspace/binary/src/prac.out","w",stdout);
	int numberOfExperiments;
	vector<string>sentence;
	vector<int> in;
	vector<int> output;
	string linebuffer;
	int turn=0;
	while(getline(iFile,linebuffer)){
		if(turn==0){
			numberOfExperiments=atoi(linebuffer.c_str());
			//cout<<numberOfExperiments<<endl;
		}
		else{
			sentence.push_back(linebuffer);
			in=charToNum(linebuffer);
		//	cout<<linebuffer<<endl;
			vector<int> allOne;
			for(int i=0;i<in.size();i++){
				allOne.push_back(1);
			}
			output=in;
			int count=0;
			while(output!=allOne){
				output=vectorChanger(in);
/*				for(int i=0;i<output.size();i++){
					cout<<output[i];
				}*/
				in=output;
				count++;
				//cout<<endl;
			}
			cout<<"Case #"<<(turn)<<": "<<count<<endl;
		}
		turn++;
	}
	return 0;
}

