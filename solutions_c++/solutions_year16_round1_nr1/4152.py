

#include <iostream>
#include <string>

using namespace std;

int main(){
	 int T = 0;
	 cin >> T;

	 int i = 1;
	 while ( i <= T){

		cout << "Case #" << i << ": ";

		 string letter = "";
		 cin >> letter;

		 int j = 1;
		 int size = letter.size();
		 string answer = "";
		 answer += letter[0];

		 while(j < size){
			 if (answer[0] <= letter [j] ){
			 	answer = letter [j] + answer;
			 }
			 else{
				 answer = answer + letter [j];
			 }
			 j++;
		 }
	 cout << answer << endl;
	 i++;

	 }

	 return 0;
}


