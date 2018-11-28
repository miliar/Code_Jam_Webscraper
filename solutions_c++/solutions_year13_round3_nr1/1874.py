#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

bool isVowel(char c)
{
	if(c=='a' || c=='e'|| c=='i'|| c=='o'|| c=='u'){
		return true;
	}
	else
		return false;

}

int count_cons(string s)
{
	int c=0;
	bool isvowel=false;
	int max=0;
	if(isVowel(s[0]))
	{
		isvowel=true;
	}
	else{
		c=1;
		max=1;
	}
	for(int i=1;i<s.length();i++){
		if(isVowel(s[i])){
			c=0;
			continue;
		}
		else{
			c++;
			if(max < c){
				max=c;
			}
		}
	}
	return max;
} 

int check_consonants(vector<string> strings,int n)
{
	vector<string>::iterator itr;
	int counter=0;
	for(itr=strings.begin();itr<strings.end();itr++){
		if(count_cons(*itr) >=n)
			counter++;
	}
	return counter;
}

void generate_substrings(string s,int lim,vector<string> &strings)
{
int n=s.length();

//vector<string> strings;
for(int L=lim;L<=n;L++){
	for(int i=0;i<n-L+1;i++){
		int j=i+L-1;
		strings.push_back(s.substr(i,L));
		//cout<<s.substr(i,L)<<endl;
	}

	}
}

int main()
{
	int testcases;
	cin>>testcases;
	int count=1,n;
	ofstream fout("test.out");
	string str;
	while(testcases--){
		cin>>str;
		cin>>n;
		vector<string> strings;
		generate_substrings(str,n,strings);
		fout<<"Case #"<<count<<": "<<check_consonants(strings,n)<<endl;
		//cout<<count_cons("c")<<endl;
		
		count=count+1;

	}


}