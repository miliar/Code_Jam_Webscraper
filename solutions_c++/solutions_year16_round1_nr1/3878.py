#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
string calculate(string temp){
	string solution = "";
	solution = solution + temp[0];
	for (int i=1;i<temp.length();i++){
		if (temp[i]>=solution[0]){
			solution = temp[i] + solution;
		}
		else if(temp[i]<solution[0]){
			solution = solution + temp[i];
		}
	}
	return solution;
}

int main(){
	FILE *fin = freopen("A-large.in", "r", stdin);
    assert(fin!=NULL);
    FILE *fout = freopen("A-large.out", "w", stdout);

    int test_cases;
    string temp;
    cin >> test_cases;
    for (int i = 0; i < test_cases; i++)
    {
    	cin >> temp;
    	cout << "Case #" << i+1 << ": " << calculate(temp) << endl;
    }
}