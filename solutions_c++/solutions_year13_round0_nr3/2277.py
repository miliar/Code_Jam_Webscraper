#include <iostream>
#include <fstream>
using namespace std;



long long FairSquare[39]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("fin.txt");
	fout.open("fout.txt");
	int T;
	fin >> T;
	for(int where=0;where<T;where++){
		long long beg,end;
		fin >> beg >> end;
		int answer=0;
		for(int a=0;a<40;a++){
		   if((beg<=FairSquare[a])&&(end>=FairSquare[a]))	answer++;
		}
		fout << "Case #" << where+1 << ": " << answer << "\n";
	}
}
