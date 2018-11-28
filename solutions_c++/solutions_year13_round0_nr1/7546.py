/*NAME: Jose Manriquez
  DATE: 4/13/2013
  Problem A. Tic-Tac-Toe-Tomek
 */


#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main(){
	string count;

	ifstream input_file;
	ofstream output_file;
	output_file.open ("output.txt", ios::in);
	input_file.open ("input.txt", ios::out);
	string line1;
	string line2;
	string line3;
	string line4;
	string space;

	if (input_file.is_open()) { 
		
		//GET THE NUMBER OF GAME CASES
		getline (input_file,count);
		int value = atoi(count.c_str());

		//algorithm that determins the winner for each Case
		for (int i=1; i<value+1;i++){
		
			//SEPARATE EACH GAME CASE
			getline(input_file, line1);
			getline(input_file, line2);
			getline(input_file, line3);
			getline(input_file, line4);
			getline(input_file, space);

			//PRINT EACH LINE
			//cout<<"\nLINE Case#"<<i<<endl;
			//cout<<"Line1:"<<line1<<"\nLine2:"<<line2<<"\nLine3:"<<line3<<"\nLine4:"<<line4<<endl;

			//SEPARATE THE LINES INTO CHAR
			char *lc1=new char[line1.size()+1];
			lc1[line1.size()]=0;
			memcpy(lc1,line1.c_str(),line1.size());
			
			char *lc2=new char[line2.size()+1];
			lc2[line2.size()]=0;
			memcpy(lc2,line2.c_str(),line2.size());
			
			char *lc3=new char[line3.size()+1];
			lc3[line3.size()]=0;
			memcpy(lc3,line3.c_str(),line3.size());
			
			char *lc4=new char[line4.size()+1];
			lc4[line4.size()]=0;
			memcpy(lc4,line4.c_str(),line4.size());


			/*
			//PRINT CHARS
			cout<<"TEST CHARS"<<endl;
			for (int k=0; k<4;k++ ){
				cout<<lc1[k]<<" ";
			}
			cout<<"\n\n";
			for (int k=0; k<4;k++ ){
				cout<<lc2[k]<<" ";
			}
			cout<<"\n\n";
			for (int k=0; k<4;k++ ){
				cout<<lc3[k]<<" ";
			}
			cout<<"\n\n";
			for (int k=0; k<4;k++ ){
				cout<<lc4[k]<<" ";
			}
			cout<<"\n\n";
			*/

			
			//STATE ALGORITHM
				//X WINS
				if (
					  ((lc1[0]=='X'||lc1[0]=='T')&&(lc1[1]=='X'||lc1[1]=='T')&&(lc1[2]=='X'||lc1[2]=='T')&&(lc1[3]=='X'||lc1[3]=='T'))//line1 
					||((lc2[0]=='X'||lc2[0]=='T')&&(lc2[1]=='X'||lc2[1]=='T')&&(lc2[2]=='X'||lc2[2]=='T')&&(lc2[3]=='X'||lc2[3]=='T'))//line2
					||((lc3[0]=='X'||lc3[0]=='T')&&(lc3[1]=='X'||lc3[1]=='T')&&(lc3[2]=='X'||lc3[2]=='T')&&(lc3[3]=='X'||lc3[3]=='T'))//line3
					||((lc4[0]=='X'||lc4[0]=='T')&&(lc4[1]=='X'||lc4[1]=='T')&&(lc4[2]=='X'||lc4[2]=='T')&&(lc4[3]=='X'||lc4[3]=='T'))//line4
					
					||((lc1[0]=='X'||lc1[0]=='T')&&(lc2[0]=='X'||lc2[0]=='T')&&(lc3[0]=='X'||lc3[0]=='T')&&(lc4[0]=='X'||lc4[0]=='T'))//column1 
					||((lc1[1]=='X'||lc1[1]=='T')&&(lc2[1]=='X'||lc2[1]=='T')&&(lc3[1]=='X'||lc3[1]=='T')&&(lc4[1]=='X'||lc4[1]=='T'))//column2
					||((lc1[2]=='X'||lc1[2]=='T')&&(lc2[2]=='X'||lc2[2]=='T')&&(lc3[2]=='X'||lc3[2]=='T')&&(lc4[2]=='X'||lc4[2]=='T'))//column3
					||((lc1[3]=='X'||lc1[3]=='T')&&(lc2[3]=='X'||lc2[3]=='T')&&(lc3[3]=='X'||lc3[3]=='T')&&(lc4[3]=='X'||lc4[3]=='T'))//column4

					||((lc1[0]=='X'||lc1[0]=='T')&&(lc2[1]=='X'||lc2[1]=='T')&&(lc3[2]=='X'||lc3[2]=='T')&&(lc4[3]=='X'||lc4[3]=='T'))//backdiagonal
					||((lc4[0]=='X'||lc4[0]=='T')&&(lc3[1]=='X'||lc3[1]=='T')&&(lc2[2]=='X'||lc2[2]=='T')&&(lc1[3]=='X'||lc1[3]=='T'))//frontdaigonal
				){
					cout<<"\Case #"<<i<<": X won\n";
					output_file<<"\Case #"<<i<<": X won\n";
				}

				//O WINS
				else if (
					  ((lc1[0]=='O'||lc1[0]=='T')&&(lc1[1]=='O'||lc1[1]=='T')&&(lc1[2]=='O'||lc1[2]=='T')&&(lc1[3]=='O'||lc1[3]=='T'))//line1 
					||((lc2[0]=='O'||lc2[0]=='T')&&(lc2[1]=='O'||lc2[1]=='T')&&(lc2[2]=='O'||lc2[2]=='T')&&(lc2[3]=='O'||lc2[3]=='T'))//line2
					||((lc3[0]=='O'||lc3[0]=='T')&&(lc3[1]=='O'||lc3[1]=='T')&&(lc3[2]=='O'||lc3[2]=='T')&&(lc3[3]=='O'||lc3[3]=='T'))//line3
					||((lc4[0]=='O'||lc4[0]=='T')&&(lc4[1]=='O'||lc4[1]=='T')&&(lc4[2]=='O'||lc4[2]=='T')&&(lc4[3]=='O'||lc4[3]=='T'))//line4

					||((lc1[0]=='O'||lc1[0]=='T')&&(lc2[0]=='O'||lc2[0]=='T')&&(lc3[0]=='O'||lc3[0]=='T')&&(lc4[0]=='O'||lc4[0]=='T'))//column1 
					||((lc1[1]=='O'||lc1[1]=='T')&&(lc2[1]=='O'||lc2[1]=='T')&&(lc3[1]=='O'||lc3[1]=='T')&&(lc4[1]=='O'||lc4[1]=='T'))//column2
					||((lc1[2]=='O'||lc1[2]=='T')&&(lc2[2]=='O'||lc2[2]=='T')&&(lc3[2]=='O'||lc3[2]=='T')&&(lc4[2]=='O'||lc4[2]=='T'))//column3
					||((lc1[3]=='O'||lc1[3]=='T')&&(lc2[3]=='O'||lc2[3]=='T')&&(lc3[3]=='O'||lc3[3]=='T')&&(lc4[3]=='O'||lc4[3]=='T'))//column4
					
					||((lc1[0]=='O'||lc1[0]=='T')&&(lc2[1]=='O'||lc2[1]=='T')&&(lc3[2]=='O'||lc3[2]=='T')&&(lc4[3]=='O'||lc4[3]=='T'))//backdiagonal
					||((lc4[0]=='O'||lc4[0]=='T')&&(lc3[1]=='O'||lc3[1]=='T')&&(lc2[2]=='O'||lc2[2]=='T')&&(lc1[3]=='O'||lc1[3]=='T'))//frontdaigonal
				){
					cout<<"\Case #"<<i<<": O won\n";
					output_file<<"\Case #"<<i<<": O won\n";
						
				}

				else if (
					  ((lc1[0]=='.'||lc1[1]=='.'||lc1[2]=='.'||lc1[3]=='.'))//line1 
					||((lc2[0]=='.'||lc2[1]=='.'||lc2[2]=='.'||lc2[3]=='.'))//line2 
					||((lc3[0]=='.'||lc3[1]=='.'||lc3[2]=='.'||lc3[3]=='.'))//line3 
					||((lc4[0]=='.'||lc4[1]=='.'||lc4[2]=='.'||lc4[3]=='.'))//line3 
				){
					cout<<"\Case #"<<i<<": Game has not completed\n";
					output_file<<"\Case #"<<i<<": Game has not completed\n";
				}

				else {
					cout<<"\Case #"<<i<<": Draw\n";
					output_file<<"\Case #"<<i<<": Draw\n";
				}

						
		
		}
		input_file.close();
	}

	 

	 output_file.close();
	

	getchar();
    return 0;
	



}