#include<iostream>
#include<fstream>
#include<string>
using namespace std;
const int MAXN=4;
class magic{
private:
	int first[MAXN][MAXN];
	int second[MAXN][MAXN];
	int first_choice;
	int second_choice;
public:
	void set(ifstream &fin);
	string result();
};

void magic::set(ifstream &fin){
	fin>>first_choice;
	int i,j;
	for( i=0; i<MAXN; i++ )
		for( j=0; j<MAXN; j++ )
			fin>>first[i][j];
	fin>>second_choice;
	for( i=0; i<MAXN; i++ )
		for( j=0; j<MAXN; j++ )
			fin>>second[i][j];
	first_choice--;
	second_choice--;
}

string magic::result(){
	int res=0;
	int i,j;
	int num=0;
	for( i=0; i<MAXN; i++ )
		for( j=0; j<MAXN; j++ ){
			if( first[first_choice][i] == second[second_choice][j] ){
				num++;
				res=first[first_choice][i];			
			}
		}

		if( num == 0 )
			return "Volunteer cheated!";
		else if( num == 1 ){
			char buffer[6];
			itoa(res,buffer,10);		
			return string(buffer);
		}
		else
			return "Bad magician!";
}

void main(){
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt1.in");
	fout.open("A-small-attempt1.out");
	magic solve;
	int T;
	fin>>T;
	for( int i=0; i<T; i++){
		solve.set(fin);
		fout<<"Case #"<<i+1<<": "<<solve.result()<<endl;
	}
	fin.close();
	fout.close();
}