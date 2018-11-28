#include <iostream>
#include <fstream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int T, S;
	char aud[6];
	int i, j, result;
    int count; 

	ifstream in("A-small-attempt1.in");
	ofstream out("A-small-attempt1.out");

	in >> T;

	for(i=1; i<=T; ++i) {
		in >> S >> aud;
		result = 0;
		count = 0;

		for(j=0; j<S; ++j) {
			count += aud[j] - 48;
			//printf("%d of Count : %d\n",j, count);
			if(count > j) {
				continue;
			}
			else {
				result++;
				count++;
			}
		}
		out << "Case #" << i << ": " << result << endl;
		//printf("Case #%d: %d\n", i, result);
	}

	//getchar();
	in.close();
	out.close();
	
	return 0;
}
