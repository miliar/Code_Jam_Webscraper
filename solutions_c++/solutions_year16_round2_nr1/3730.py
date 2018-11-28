#include <iostream>
#include <vector>
#include <string>


using namespace std;

std::string m1[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};


bool findWord(std::vector<int> &cset,int num){
	int temp[26];

	for(int i=0;i<cset.size();++i){
		temp[i] = cset[i];
 	}
	
 	std::string &word = m1[num]; 

	for(int i=0;i< word.size();++i){
		if(temp[word[i] - 'A'] <= 0)
			return false;
		temp[word[i] - 'A']--;
 	}

 	for(int i=0;i<26;++i){
 		cset[i] = temp[i];
 	}
 	return true;
}

void convertStr2Hash(std::vector<int> &cset,std::string &a){
	for(int i=0;i<a.size();++i){
		cset[i]=0;
 	}

	for(int i=0;i<a.size();++i){
		cset[a[i] - 'A']++;
 	}
}

void addtoCset(std::vector<int> &cset,int num){
	 std::string &word = m1[num]; 

	for(int i=0;i< word.size();++i){
		cset[word[i] - 'A']++;
 	}	
}

bool allZero(std::vector<int> &cset){
	for (int i = 0; i < cset.size(); ++i)
	{
		if(cset[i] != 0)
			return false;
		/* code */
	}

	return true;
}


void compScan(std::vector<int> &cset,int num,string &out){
	if (allZero(cset)){
		return;
	}
	else if(num < 10){
		if(findWord(cset,num)){
			out.push_back('0'+num);
			compScan(cset,num,out);
		}
		else{
			compScan(cset,++num,out);
		}
	}
	else {//if(num > 9 && !allZero(cset))
		char ch = out.back();
		out.pop_back();
		addtoCset(cset,ch-'0');
		compScan(cset,ch-'0'+1,out);
	}
}


int main(){
	int T;
	std::string str;
	cin>>T;
	const int CT = T;

	while(T--){
		std::vector<int> cset(26);
		cin >> str;
		convertStr2Hash(cset,str);
		
		cout<<"Case #"<<CT-T<<": ";
		// for(int i=0;i<10;){
		// 	if(!findWord(cset,i))
		// 		++i;
		// 	else
		// 		cout<<i;
		// }
		std::string out1;
		compScan(cset,0,out1);
		cout<<out1<<"\n";
	}

	return 0;
}