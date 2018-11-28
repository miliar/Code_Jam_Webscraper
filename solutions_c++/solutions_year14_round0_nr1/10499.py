#include <fstream>
#include <iostream>

using namespace std;

ofstream out;


void solve(int n1, int mat1[4][4], int n2, int mat2[4][4], int nCase){

	int count = 0;
	int val = 0;
	for(int i = 0 ; i < 4 ; i++)
		for(int j = 0 ; j < 4 ; j++) {
			if(mat1[n1-1][i] == mat2[n2-1][j]){
				val = mat1[n1-1][i];	
				count++;
			}
		}
	
	//cout<<"n1: "<<n1<<" n2: "<<n2<<endl;

	if(count == 1){
		out<<"Case #"<<nCase<<": "<<val<<endl;		
		return;		
	}

	if(count < 1){
		out<<"Case #"<<nCase<<": Volunteer cheated!"<<endl;		
		return;		
	}

	if(count > 1){
		out<<"Case #"<<nCase<<": Bad magician!"<<endl;		
		return;		
	}
}





int main ( int argc, char *argv[] )
{
	int lp = -1;
	int mat1[4][4], mat2[4][4];
	int n1, n2, temp, j, k, z;
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
	for(j = 1 ; j <= i ; j++){
		
		the_file.get(y);
		n1 = y - 48;
		
		the_file.get(y);
		for(k = 0 ; k < 4 ; k++){
			for(z = 0 ; z < 4 ; z++){
				the_file.get(y);
				temp = 0;
				while(y != '\n' && y != ' ') {
					temp = temp*10 + (y - 48);
					the_file.get(y);
				}
				mat1[k][z] = temp;
				
			}
			

			
		
		}
		the_file.get(y);
		n2 = y - 48;
		
		the_file.get(y);
		for(k = 0 ; k < 4 ; k++){
			for(z = 0 ; z < 4 ; z++){
				the_file.get(y);
				temp = 0;
				while(y != '\n' && y != ' ') {
					temp = temp*10 + (y - 48);
					the_file.get(y);
				}
				mat2[k][z] = temp;
				

			}
			
		}
		solve(n1, mat1, n2, mat2, j);
		
	}
    }
    // the_file is closed implicitly here

	the_file.close();
	out.close();
  
}

