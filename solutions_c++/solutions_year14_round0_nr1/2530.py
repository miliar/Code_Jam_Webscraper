#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream reader;
	ofstream writer;
	
	reader.open("input.txt");
	writer.open("output.txt");

	int cases;

	reader >> cases;
	int a1, a2, dummy;

	for(int i = 0; i < cases; i++)
	{
		int r1[4], r2[4];
		reader >> a1;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				if(j == a1-1)
					reader >> r1[k];
				else
					reader >> dummy;
			}
		}

		int found = 0, reading, ans;
		reader >> a2;	

		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				if(j == a2-1){
					reader >> reading;
					for(int z = 0; z < 4; z++)
						if(r1[z] == reading)
							{found++; ans = reading;}
				}
				else
					reader >> dummy;
			}
		}

		if(found == 1)
			writer << "Case #" << i + 1 << ": " << ans << endl;
		else if(found > 1)
			writer << "Case #" << i + 1 << ": Bad magician!" << endl;
		else
			writer << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
	}

}
