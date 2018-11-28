#include <fstream>
#include <iostream>

using namespace std;

 int checkwin(int insum) {
	 if (insum == 4 || insum == 100 )
		 return 1;
	 else if (insum == -4 || insum ==94)
		 return -1;
	 else
		 return 0;
 }

int main(int argc, char* argv[])
{
	if ( argc != 2 )
		cout<<"usage: "<< argv[0] <<" <filename>\n";
	else {
		ifstream the_file ( argv[1] );
		ofstream out_file ("output.out");
		if ( !the_file.is_open() || !out_file.is_open())
			cout<<"Could not open file\n";
		else {
			char x;
			int ntest;
			int tt;
			the_file>> tt;
			ntest = tt;
			while (ntest > 0) {
				int gameboard[4][4] = {0};
				bool gamefull = true;
				for (int i=0;i<16;) {
					the_file.get(x);
					switch (x) {
						case 'X':
						case 'x':
							gameboard[(int)i/4][i%4] = 1;
							i++;
							break;
						case 'O':
						case 'o':
							gameboard[(int)i/4][i%4] = -1;
							i++;
							break;
						case '.':
							gamefull = false;
							gameboard[(int)i/4][i%4] = 0;
							i++;
							break;
						case 'T':
						case 't':
							gameboard[(int)i/4][i%4] = 97;
							i++;
							break;
						default:
							//everything else - dont care
							break;
					}
				}
				//game loaded
				int retval[10] = {0};
				bool resultdone = false;
				retval[0] = checkwin(gameboard[0][0]+gameboard[0][1]+gameboard[0][2]+gameboard[0][3]);
				retval[1] = checkwin(gameboard[1][0]+gameboard[1][1]+gameboard[1][2]+gameboard[1][3]);
				retval[2] = checkwin(gameboard[2][0]+gameboard[2][1]+gameboard[2][2]+gameboard[2][3]);
				retval[3] = checkwin(gameboard[3][0]+gameboard[3][1]+gameboard[3][2]+gameboard[3][3]);
				retval[4] = checkwin(gameboard[0][0]+gameboard[1][0]+gameboard[2][0]+gameboard[3][0]);
				retval[5] = checkwin(gameboard[0][1]+gameboard[1][1]+gameboard[2][1]+gameboard[3][1]);
				retval[6] = checkwin(gameboard[0][2]+gameboard[1][2]+gameboard[2][2]+gameboard[3][2]);
				retval[7] = checkwin(gameboard[0][3]+gameboard[1][3]+gameboard[2][3]+gameboard[3][3]);
				retval[8] = checkwin(gameboard[0][0]+gameboard[1][1]+gameboard[2][2]+gameboard[3][3]);
				retval[9] = checkwin(gameboard[0][3]+gameboard[1][2]+gameboard[2][1]+gameboard[3][0]);

				for(int i=0;i<10;i++) {
					if(retval[i] != 0){
						if (retval[i] == 1)
							out_file << "Case #"<<(tt - ntest + 1)<<": X won"<<endl;
						else if (retval[i] == -1)
							out_file << "Case #"<<(tt - ntest + 1)<<": O won"<<endl;
						else
							out_file << "Case #"<<(tt - ntest + 1)<<": unknown retval: " << retval<<endl;
						resultdone = true;
						break;
					}
				}
				if(!resultdone) {
					if (gamefull == true)
						out_file << "Case #"<<(tt - ntest + 1)<<": Draw"<<endl;
					else
						out_file << "Case #"<<(tt - ntest + 1)<<": Game has not completed"<<endl;
				}
				ntest--;
			}
		}
		the_file.close();
		out_file.flush();
		out_file.close();
	}
	return 0;
}

