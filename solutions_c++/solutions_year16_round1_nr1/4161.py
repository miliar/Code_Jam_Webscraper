#include <iostream>
#include <fstream>
#include <string.h>
#include <vector>
using namespace std;


int main() {

	int test;

	ifstream myfile;
	myfile.open ("input.txt");
	myfile>>test;

	ofstream myfile2;
	myfile2.open ("output.txt");


	for (int i=0;i<test;i++){
		
		string a;
		myfile>>a;
	
		vector<string> win;

		string temp;
		temp=a[0];
		string temp2;
		win.push_back(temp);
		//iterator it; 
		//it = win.begin();


		for (int j=1; j<a.length(); j++){
			temp=*win.begin();
			temp2=a[j];
			if (temp2>=temp){
				//it = win.insert(it, temp2);
				//it = win.begin();
				win.insert(win.begin(), temp2);
			}
			else{
				win.push_back(temp2);
			}
		}

		myfile2 << "Case #"<< i+1<<": ";

		for (int k=0; k<win.size();k++){
			myfile2<<win[k];
		}
		myfile2 << endl;
	}


	myfile.close();
	myfile2.close();

	return 0;
	
}