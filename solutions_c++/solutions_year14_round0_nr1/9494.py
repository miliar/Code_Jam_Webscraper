#include<fstream>
#include<bitset>
using namespace std;


ifstream in("infile.txt");
ofstream out("outfile.txt");



int M[5][5];

bitset < 17 > possible;

int T;

int main(){
	in >> T;

	int choice, answer, na;
	for(int t = 1; t <= T; ++ t){
		possible.reset();
		answer = na = 0;

		in >> choice;
		for(int i = 1; i <= 4; ++ i){
			for(int j = 1; j <= 4; ++ j){
				in >> M[i][j];
				if(i == choice)
					possible[M[i][j]] = true;
			}
		}
		
		in >> choice;
		for(int i = 1; i <= 4; ++ i){
			for(int j = 1; j <= 4; ++ j){
				in >> M[i][j];
				if(i == choice && possible[M[i][j]]){
					answer = M[i][j];
					na ++;
				}
			}
		}

		if(!na)
			out << "Case #" << t << ": Volunteer cheated!\n";
		else if(na == 1)
			out << "Case #" << t << ": " << answer << '\n';
		else
			out << "Case #" << t << ": Bad magician!\n";
	}

	in.close();
	out.close();

	return 0;
}