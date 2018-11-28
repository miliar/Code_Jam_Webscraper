#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <unordered_map>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;
int count = 0;
int p(string n) {
	string temp = n;
	int flipcount = 0;
	int unhappy = true;
	while(unhappy) {
		int pos = temp.find('-');
		//cout << pos << endl;
		if(pos > 0)	
		{	
			string t2 = "";
			//flip all minus before -
			flipcount++;
			for ( int i = 0; i < pos; i ++)
			{
				t2+= "-";	
				
			}
			t2 = t2 + n.substr(pos);
			//flip beginning + to -
			pos = t2.find('+');
			if(pos < 0) {flipcount ++; unhappy = false; break;}
			t2 = "";
			flipcount++;
			for ( int i = 0; i < pos; i ++)
			{
				t2+= "+";	
				
			}
			t2 = t2 + n.substr(pos);
			temp = t2;
		} 
		else {
			// all +
			return flipcount;

		}

	}
	return flipcount;
	

}

int m (string n) {
	string temp = n;
	int flipcount = 0;
	int unhappy = true;
	while(unhappy) {
		int pos = temp.find('+');
		
		//break;
		if(pos > 0)	
		{	
			string t2 = "";
			//flip all minus before +
			flipcount++;
			for ( int i = 0; i < pos; i ++)
			{
				t2+= "+";	
				
			}
			t2 = t2 + n.substr(pos);
		
			
			//flip beginning - to +
			pos = t2.find('-');
			
			
			
			if(pos < 0) {unhappy = false; break;}
			t2 = "";
			flipcount++;
			for ( int i = 0; i < pos; i ++)
			{
				t2+= "-";	
			
			}
			
			t2 = t2 + n.substr(pos);
			temp =t2;
			
		} 
		else {
			// all minuses so flip once to plus
			flipcount++;
			return flipcount;

		}
	}	
	return flipcount;	

}

int main() {
	ifstream input("B-large.in");
  	string n;
	int t;
 	input >> t;  // read t. cin knows that t is an int, so it reads it as such.	
	ofstream f("output.txt");
  	for (int i = 1; i <= t; ++i) {
		input >> n;
		if(n[0] == '+')  f << "Case #" << i << ": " << p(n) << endl;
		else f << "Case #" << i << ": " << m(n) << endl;
  	}
	f.close();
	input.close();
	return 0;
}
