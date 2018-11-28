#include<iostream>
#include<vector>
#include<fstream>
#include<string>
using namespace std;
	vector<char> word;
	ofstream fout("D:/q.txt");
    ifstream fin("A-large.in");
void test(string w);
int main()
{

int cs,ct=0;
fin>> cs;
string w;
while(cs--)
{   ct++;
	fin >> w;
	test(w);
	fout <<"Case #"<<ct<<": ";
	for(int i=0;i<word.size();i++) fout << word[i];
	fout<<endl;
	
	
	
}

fin.close();
fout.close();
return 0;
}



void test(string w)
{
	int n=w.size(),m=1;
	char st,en;
	word.clear();
	word.push_back(w[0]);
	st=en=w[0];
	while(m<n)
	{
		if(w[m]>=st) word.insert(word.begin(),w[m]), st=w[m];
		else word.push_back(w[m]), en=w[m];
     m++;
	}
    
    
    
    
    
    
	
}
