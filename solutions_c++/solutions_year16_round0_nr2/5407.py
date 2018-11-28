#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cassert>
#include <vector>
using namespace std;

int main()
{
	FILE *fin = freopen("B-large.in", "r", stdin);
    assert(fin!=NULL);
    FILE *fout = freopen("B-large.out", "w", stdout);
	int num_testcases;
	cin >> num_testcases;
	string input;
	int counter = 0;
	int length;
	for (int i=0;i<num_testcases;i++){
		cin >> input;
		length = input.length();
		if (input[length-1]== '+'){
			
			for (int i=length-2;i>=0;i--){
				if (input[i]!=input[i+1]){
					counter++;
				}
			}
		}
		else if(input[length-1] == '-'){
			counter++;
			for (int i=length-2;i>=0;i--){
				if (input[i]!=input[i+1]){
					counter++;
				}
			}
		}
		cout << "Case #" << i+1 << ": "<< counter << endl;
		counter =0;

	}
}
