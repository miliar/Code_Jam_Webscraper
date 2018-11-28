#include <iostream>
#include <fstream>

using namespace std;
int main(){

	ofstream output;
  	output.open ("output");

  	ifstream input;
	input.open ("input");

	int n;
	input >> n;

	for(int test_case=0;test_case<n;test_case++){

		int sentados = 0;
		int levantados = 0;
		int amigos = 0;

		int max_shyness_level;
		input >> max_shyness_level;

		char s[max_shyness_level+1];
		input >> s;

		int S[max_shyness_level+1];
		for (int i = 0; i < max_shyness_level+1; i++)
		{
			S[i] = s[i] - '0';
			sentados+= S[i];

		}
		// cout << "sentados: " << sentados <<endl;

		while(sentados > 0){
			bool mudou = false;
			for (int shyness_level = 0; shyness_level < max_shyness_level + 1; shyness_level++)	{
				if(levantados >= shyness_level){
					sentados -= S[shyness_level];
					levantados += S[shyness_level];
					S[shyness_level] = 0;
					mudou = true;
				}				
			}
			if( (sentados > 0) ){
					amigos++;
					levantados++;
			}

		}

		output <<"Case #" <<test_case+1<<": "<< amigos <<endl;


		// for (int i = 0; i < max_shyness_level+1; ++i)
		// {
		// 	cout << S[i];
		// }


	}

	return 0;
}