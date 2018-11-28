#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <math.h>
using namespace std;
vector<double> digitNumbers(double input){
	vector<double> output;
	int i=1;
	int denum=1;
	int in=input;
	while (denum>0){
		int rem;
		denum=in/10;
		rem=in-10*denum;
		in=denum;
		output.push_back(rem);
	}
	return output;
}
bool vectorCheck(vector<double> input){
	vector<double> in;
	in=input;
	if (in.size()==10){
		int count=0;
		for(int i=0;i<10;i++){
			for(int j=0;j<10;j++){
				if(in[j]==i){
					count++;
				}
			}
		}
		if(count==10){
			return true;
		}
		else{
			return false;
		}
	}
	else{
		return false;
	}
}
vector<double> diffNumbers(vector <double> input){
	vector<double> in;
	in=input;
	vector<double> output;
	vector<double> count;
	for(int i=0;i<10;i++){
		count.push_back(0);
	}
	for(int i=0;i<in.size();i++){
		if(count[in[i]]==0){
			output.push_back(in[i]);
			count[in[i]]=count[in[i]]+1;
		}
	}
	return output;
}
vector<double> concatVec(vector<double> in1,vector<double> in2){
	vector<double> output;
	output=diffNumbers(in1);
	for(int i=0;i<in2.size();i++){
		output.push_back(in2[i]);
	}
	return diffNumbers(output);

}

int main() {
	/*ifstream iFile("/home/mehdi/workspace/binary/src/Clarge.in");
	freopen("/home/mehdi/workspace/binary/src/prac.out","w",stdout);
	string linebuffer;
	int numberOfExperiments;
	vector<string>sentence;
	int turn=0;
	while(getline(iFile,linebuffer)){
			if(turn==0){
				numberOfExperiments=atoi(linebuffer.c_str());
			}
			else{
				sentence.push_back(linebuffer);
			}
			turn++;
		}
		iFile.close();
		for(int i=0;i<numberOfExperiments;i++){
			cout<<"Case #"<<i+1<<": ";
		    phoneProccess(sentence[i]);
		    cout<<endl;

		}*/
	freopen("/home/mehdi/workspace/binary/src/Alarge.in","r",stdin);
	freopen("/home/mehdi/workspace/binary/src/prac.out","w",stdout);
	int information;
	//vector<int>priceDigits;
	//vector<int>turn;
	int numberOfExperiments;
	int number;
	long input;
	int label;
	int digitNum;
	cin>>numberOfExperiments;
	for(int i=0;i<numberOfExperiments;i++){
		//information.clear();
		cin>>input;
		vector<double> numbers1;
		vector<double> numbers2;
		vector<double> diffnumbers;
		int in=input;
		if(input==0){
			cout<<"Case "<<"#"<<(i+1)<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		int k=1;
		int count=0;
		bool coeffFind=false;
		while(!coeffFind){
		vector<double> numbers1;
		long coeffNum=input*k;
		if(k==1){

		numbers1=digitNumbers(input);
		}
		if(k>1){
			//cout<<"checked second";
			numbers1=diffnumbers;
		}
		numbers2=digitNumbers(coeffNum);
/*		for (int i=0;i<numbers2.size();i++){
			cout<<numbers2[i];
		}
		cout<<endl;
		cout<<"---------------"<<endl;*/
		diffnumbers=concatVec(numbers1,numbers2);
/*		for(int i=0;i<diffnumbers.size();i++){
			cout<<diffnumbers[i];
		}
		cout<<endl;*/
	//	count++;
		k++;
		coeffFind=vectorCheck(diffnumbers);
		}
		cout<<"Case "<<"#"<<(i+1)<<": "<<(k-1)*input<<endl;
		//information.push_back(price);
	//	cin>>number;
		/*information.push_back(number);
		for(int k=0;k<number;k++){
			cin>>label;
			information.push_back(label);*/
		}

int a=42115;
int b=137;
/*vector<double> numbers1;
vector<double> numbers2;

vector<double> diffnumbers;
numbers1=digitNumbers(a);
numbers2=digitNumbers(b);
diffnumbers=concatVec(numbers1,numbers2);*/
/*for(int i=0;i<diffnumbers.size();i++){
	cout<<diffnumbers[i]<<endl;
}*/
//cout<<vectorCheck(numbers);
	return 0;
}

