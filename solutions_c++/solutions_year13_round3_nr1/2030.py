#include<iostream>
#include <vector>
#include<memory.h>
#include<string>
#include<ctype.h>
#include<iostream>
#include<cmath>
#include <cstdlib>
#include<fstream>
#include <cstring>
#include<algorithm>
#include<sstream>
using namespace std;
using std::ifstream;
using std::ofstream;
#define size 100000

template<class out_type,class in_value>
out_type convert(const in_value & t)
{
	stringstream stream;
	stream<<t;
	out_type result;
	stream>>result;
	stream.str("");
	stream.clear();
	return result;
}



bool cont(string word, int start, int end, int n){
	int m=start+1, key=1;
	while(m<=end){
		if(word[m]=='a' || word[m]=='e' || word[m]=='i' || word[m]=='o' || word[m]=='u')
			break;
		key++;
		m++;
	}
	if(key>=n) return true;
	else return false;
}

long long answer(string word, int start, int end, int n,int  key){
	int m=start+1;
	if(n==1)
		m=start;
	long long ans=0;
	while(m<=end){
		if(key>=n){
			ans++;
			m++;
		}else
		{
		if(word[m]=='a' || word[m]=='e' || word[m]=='i' || word[m]=='o' || word[m]=='u'){
			key=0;
			m++;
			continue;
		}
		else{
			key++;
			if(key>=n)
				ans++;
			m++;}
		}
	}
	if(key>=n)
		return ans;
	else return 0;
}

int main()
{
	ofstream out;
	//out.open("output.txt");

	int T;
	string word;
	int n, length, m, end;
	long long ans;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cin>>word>>n;
		length=word.length();
		end = length-n;
		m=0;
		ans=0;
		for(int j=0;j<=end;j++){
			if(word[j]=='a' || word[j]=='e' || word[j]=='i' || word[j]=='o' || word[j]=='u')
				ans+=answer(word, j, length-1, n, 0);	
			else
			ans+=answer(word, j, length-1, n, 1);			
		}
		//ans
		cout<<"Case #"<<i<<": "<<ans<<endl;
	//	out<<"Case #"<<i<<": "<<ans<<endl;
	}

//	out.close();

	return(0);
}