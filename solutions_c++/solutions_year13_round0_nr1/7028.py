#include <fstream>
#include <iostream>

using namespace std;

ofstream out;

int diagonal1(char mat[4][4], char c){
	return (mat[0][0] == 'T' || mat[0][0] == c) 
		&& (mat[1][1] == 'T' || mat[1][1] == c) && (mat[2][2] == 'T' || mat[2][2] == c)
			&& (mat[3][3] == 'T' || mat[3][3] == c);
}
int diagonal2(char mat[4][4], char c){
	return (mat[3][0] == 'T' || mat[3][0] == c) 
		&& (mat[2][1] == 'T' || mat[2][1] == c) && (mat[1][2] == 'T' || mat[1][2] == c)
			&& (mat[0][3] == 'T' || mat[0][3] == c);
}

int hori(char mat[4][4], char c){
	int flag = 0;
	for(int i = 0 ; i < 4 ; i++){
		for(int j = 0 ; j < 4 ; j++){
			if(mat[i][j] == c || mat[i][j] == 'T'){
				flag++;
			}else{
				continue;	
			}
		}
		if(flag == 4)
			return 1;
		flag = 0;
	}	
	return flag==4;
}

int vert(char mat[4][4], char c){
	int flag = 0;
	for(int i = 0 ; i < 4 ; i++){
		for(int j = 0 ; j < 4 ; j++){
			if(mat[j][i] == c || mat[j][i] == 'T'){
				flag++;
			}else{
				continue;	
			}
		}
		if(flag == 4)
			return 1;
		flag = 0;
	}	
	return flag==4;
}

void solve(char mat[4][4], int cs){
	
	//1st diagonal
		//for X
	if(diagonal1(mat, 'X')){
		out<<"Case #"<<cs<<": X won"<<endl;		
		return;		
	}
		//for 'O'
	if(diagonal1(mat, 'O')){
		out<<"Case #"<<cs<<": O won"<<endl;		
		return;		
	}
	//2nd diagonal
	if(diagonal2(mat, 'X')){
		out<<"Case #"<<cs<<": X won"<<endl;		
		return;		
	}
	if(diagonal2(mat, 'O')){
		out<<"Case #"<<cs<<": O won"<<endl;		
		return;		
	}
	
	if(hori(mat, 'X')){
		out<<"Case #"<<cs<<": X won"<<endl;		
		return;		
	}
	if(hori(mat, 'O')){
		out<<"Case #"<<cs<<": O won"<<endl;		
		return;		
	}
	if(vert(mat, 'X')){
		out<<"Case #"<<cs<<": X won"<<endl;		
		return;		
	}
	if(vert(mat, 'O')){
		out<<"Case #"<<cs<<": O won"<<endl;		
		return;		
	}
	
	for(int i = 0 ; i < 4 ; i++){
		for(int j = 0 ; j < 4 ; j++){
			if(mat[i][j] == '.'){
				out<<"Case #"<<cs<<": Game has not completed"<<endl;		
				return;
			}

		}
	}

	out<<"Case #"<<cs<<": Draw"<<endl;		
		
}



int main ( int argc, char *argv[] )
{
	int lp = -1;
	char mat[4][4];
	if ( argc != 2 ) 
		out.open(argv[2]);
	else
		out.open("output.txt");

	if( !out.is_open()){
		cout<<"Could not open output file";
		return -1;
	}
	
    // We assume argv[1] is a filename to open
    ifstream the_file ( argv[1] );
    // Always check to see if file opening succeeded
    if ( !the_file.is_open() )
      out<<"Could not open file\n";
    else {
      
	char y ='1';
	int i = 0;
      // the_file.get ( x ) returns false if the end of the file
      //  is reached or an error occurs
	the_file.get(y);
	while(y != '\n'){
		i = i*10 + (y - 48);
		//out<<y;
		the_file.get(y);
	}
//	out<<endl<<i<<endl;
	for(int j = 1 ; j <= i ; j++){
		for(int k = 0 ; k < 4 ; k++){
			for(int z = 0 ; z < 4 ; z++){
				the_file.get(mat[k][z]);
				//out<<"mat["<<k<<"]["<<z<<"]: "<<mat[k][z]<<endl;	
			}
			

			
		the_file.get(y);
		}
		solve(mat, j);
		the_file.get(y);
	}
    }
    // the_file is closed implicitly here

	the_file.close();
	out.close();
  
}
