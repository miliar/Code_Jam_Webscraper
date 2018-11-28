#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int main(){
	int T ;
	ifstream cin("input1.txt");
	ofstream cout("output1.txt");
	cin >> T ;
	
	for( int f = 0 ; f < T ; f++ ){
		string word;
		vector<char> arr;
		cin >> word;
		for( int i = 0 ; i < word.size() ; i++ ){
		
			if( arr.size() == 0 ){
				arr.push_back( word[i] );
			}
			else if( word[i] >= arr[0] ){
				arr.insert( arr.begin() , word[i] );
			}
			else{
				arr.push_back( word[i] );
			}
			
		}
		cout << "Case #" << f+1 << ": " ;
		for( int i = 0 ; i < arr.size() ; i++ ){
			cout << arr[i] ;
		}
		cout << endl;
	}
	
}
