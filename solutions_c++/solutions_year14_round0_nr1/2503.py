/*Author: Vasile Mihail-Raul, Romania
  Mail: vasile.raul@webmonsters.ro */

#include <fstream>

using namespace std;

//Making the intersection of 2 rows and find out the card or,
//if there are more cards or no cards, return the specific error
int check(int row1, int row2, int v1[16], int v2[16]) {
	int app = 0, number;

	for(int i = (row1 - 1) * 4 ; i < row1 * 4 ; i++)
		for(int j = (row2 - 1) * 4 ; j < row2 * 4 ; j++)
			if(v2[j] == v1[i]) {
				app++;
				number = v2[j];
			}//close for

	if(app == 1)
		return number; //Number of card
	if(app == 0)
		return -1; //Volunteer cheated!
	return -2; //Bad magician!
}//close function

//Reading function
void reading(ifstream& in, int &row, int v[16]) {
	in >> row;
	for(int i = 0 ; i < 16 ; i++)
		in>>v[i];
}//close function

int main(int argc, char* argv[]) {

	ifstream in("magictrick.in");
	ofstream out("magictrick.out");

	int T, noCase = 0;

	in >> T;

	while(T--) {
		noCase++;
		int v1[16], v2[16], row1, row2;

		//Reading
		reading(in, row1, v1);
		reading(in, row2, v2);

		int x = check(row1, row2, v1, v2);

		if(x > 0)
			out<<"Case #"<<noCase<<": "<<x<<"\n";
		if(x == -1)
			out<<"Case #"<<noCase<<": Volunteer cheated!\n";
		if(x == -2)
			out<<"Case #"<<noCase<<": Bad magician!\n";
	}//close while

	//Close input/output files
	in.close();
	out.close();

	return 0;
}//close main