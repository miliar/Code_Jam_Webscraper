#include <iostream>
#include <cmath>
#include <list> 
#include<cstring>
#include<string>
#include<fstream>

using namespace std;

int main(){
	string str;
	string bstr;
	
	list <char>  thelist;
	int c; 
	int count = 1;
	ifstream openfile;
	fstream out;

	openfile.open("A-large.in");
	out.open("2.txt", ios::out);

	openfile >> c;
	while (c){
		out << "Case #" << count << ": ";
		openfile>> str;
		thelist.push_front(str[0]);
		for (int i = 1; i < str.length(); i++){
			if (thelist.front() <= str[i]){
				thelist.push_front(str[i]);
			}
			else{
				thelist.push_back(str[i]);
			}
		}
		for (list<char>::iterator it = thelist.begin(); it != thelist.end(); ++it){
			out << *it;
		}
		out << '\n';
		thelist.clear();
		count++;
		c--;
	}
	openfile.close();
}
