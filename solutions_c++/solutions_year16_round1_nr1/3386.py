#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;

int main() {
	// your code goes here
	ofstream outfile;
	ifstream infile ("A.in");
	outfile.open("A.out");
    //cout << "BB" << endl;
	int T;
	infile >> T;
	//cout << T << endl;
	string temp;
	getline (infile, temp);
	//cout << "BB" << endl;
	for (int i = 0; i < T; i++){
        string input;
        string ans;
        infile >> input;
        getline(infile,temp);
        outfile << "Case #" << i+1 << ": ";
        //cout << input << endl;
        char first, last;
        //cout << "AA" << endl;
        first = input[0];
        //last = input[0];
        ans = first;
        //cout <<"ANS: " << ans << endl;
        for (int j = 1; j < input.length(); j++){
            //cout << input[j] << endl;
            char temp2 = input[j];
            if (temp2 >= first){
                ans = temp2 + ans;
            }
            else{
                ans = ans + temp2;
            }
            //cout << temp2<< endl;
            //cout << ans << endl;
            first = ans[0];
            //last = input[ans.length()-1];
        }
        outfile << ans << endl;
	}
	outfile.close();
	infile.close();
	return 0;
}
