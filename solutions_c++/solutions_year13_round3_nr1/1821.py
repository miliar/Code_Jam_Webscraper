#include<iostream>
#include<fstream>
#include<math.h>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;

bool IsVowel(char c){
	if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
		return true;
	return false;
}

bool HasNConsecutiveConsonants(string temp, int n)
{
	if(temp.length()<n)
		return false;
	bool flag= false;
	for(int i=0; i<temp.length(); ++i){
		if(IsVowel(temp[i]))
			continue;
		int j;
		for(j=1; j<n && i+j < temp.length(); j++){
			if(IsVowel(temp[i+j]))
				break;
		}
		if(j==n)
			return true;
	}
	return false;
}


int main()
{
	ifstream inpFile;
	inpFile.open("input.txt");
	ofstream outFile;
	outFile.open("output.txt");
	unsigned int T;
	inpFile>>T;
	unsigned int N, sum;
	string word, temp;

	for(unsigned int i=0; i<T; i++)
	{
		sum = 0;
		bool flag = false;
		inpFile>>word>>N;

		/*for(int j=0; j+N <= word.length(); ++j)
		{
			temp = word.substr(0,N+j);
			if(flag){
				sum++;
			}
			else{
				if(HasNConsecutiveConsonants(temp, N)){
					sum++;
					flag = true;
				}
			}
		}

		flag = false;
		for(int j=0; j+N < word.length(); ++j)
		{
			temp = word.substr(word.length()-N-j);
			if(flag){
				sum++;
			}
			else{
				if(HasNConsecutiveConsonants(temp, N)){
					sum++;
					flag = true;
				}
			}
		}*/

		for(int i=0; i<=word.length()-N; ++i){
			for(int j=1; i+j<=word.length(); j++){
				temp = word.substr(i,j);
				if(HasNConsecutiveConsonants(temp, N))
					sum++;
			}
		}

		

		outFile<<"Case #"<<i+1<<": "<<sum<<endl;
	}
	

	

}