#include<iostream>
#include<vector>
#include<fstream>
#include<string>
int comp(char ch);
using namespace std;
	ofstream fout("D:/q.txt");
    ifstream fin("t.in");
string q="ONE";
void test();
int main()
{

int cs,ct=0;
fin>> cs;

while(cs--)
{   ct++;
	fin>>q;
	fout <<"Case #"<<ct<<": ";
    test();
	
	
}

fin.close();
fout.close();
return 0;
}


void test()
{
	int a[11];
	char b[]={'Z','O','W','H','U','F','X','V','G','N'};
	for(int i=0;i<10;i++) {a[i]=comp(b[i]);}
	a[1]-=a[0]+a[2]+a[4];

	//a[9]-=a[1];
	// 0 2 6  8
	a[3]-=a[8];
	//3 4 1 5 7
	a[5]-=a[4];
	a[7]-=a[5];
	
	a[9]=(a[9]-a[1]-a[7])/2;
	
	for(int i=0;i<10;i++) if(a[i]>0) {for(int j=0;j<a[i];j++) fout <<i;}
	fout <<endl;
	
	
	
	

	
}

int comp(char ch)
{int n=0;
	for(int i=0;i<q.length();i++)
	if(q[i]==ch) n++;
	return n;
	
	
}
