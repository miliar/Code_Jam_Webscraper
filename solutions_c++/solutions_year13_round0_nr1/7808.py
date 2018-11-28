#include <iostream>
#include <string> 
#include <queue>
#include <fstream>
using namespace std; 
bool draw = 1; 
int check ( char[4][4]); 
void main (){
ifstream source; 	ofstream target;
string infile ;
cin>>infile; 
string	outfile = "koko.txt" ; 
source.open(infile.c_str());
target.open(outfile.c_str());
queue <string> que ;
int T;
char s,w,p,q;

source.get(s);
source.get(w);
source.get (p);
source.get(q);

T=int (s - 48 )*1000+ int (w-48)*100+int(p-48)*10+int(q-48); 

string str;


char arr [4][4]; 
	while (! source.eof()) {     
		
	for (int u = 0 ; u <4 ; u++){
			source>>str; 
			
		for (int k = 0 ; k <4 ; k++){
			arr[u][k]=str.at(k);
			cout<<arr[u][k]; 
		
			
		
		}
	
	} 
	
	draw = 1; 
		switch (check (arr )){
	case 1 : que.push("X won"); break;
	case 2: que.push ("O won"); break;
	case 3: que.push ("Draw"); break;
	case 4: que.push ("Game has not completed"); break; 
	
	}
		
	
}

string d;
		for (int k=1 ; k<=T;k++){
		
			d=que.front();
			target<<"Case #"<<k<<": "<<d<<endl;
			que.pop();}

}


int check (char arr[4][4]){
	int X =0 , O = 0 , T = 0 ;

	for (int u = 0 ; u < 4; u++){
	if (arr [0][u] == 'X') X++;
	else if (arr [0][u]== 'O') O++;
	else if (arr [0][u]== 'T')T++;
	else if ( arr [0][u] == '.') draw = 0; 
	}

	if (X == 4 ) return 1; 
	else if (O == 4 ) return 2; 
	else if ( T ==1 && X == 3) return 1;
	else if (T==1 && O == 3) return 2;
	
	X=0 ; O = 0 ; T= 0 ; 
	for (int u = 0 ; u < 4; u++){
	if (arr[1][u] == 'X') X++;
	else if (arr [1][u]== 'O') O++;
	else if (arr [1][u]== 'T')T++;
	else if ( arr [1][u] == '.') draw = 0; 
	}
	if (X == 4 ) return 1; 
	else if (O == 4 ) return 2; 
	else if ( T ==1 && X == 3) return 1;
	else if (T==1 && O == 3) return 2;

	X=0 ; O = 0 ; T= 0 ;
	for (int u = 0 ; u < 4; u++){
	if (arr[2][u] == 'X') X++;
	else if (arr [2][u]== 'O') O++;
	else if (arr [2][u]== 'T')T++;
	else if ( arr [2][u] == '.') draw = 0; 
	}
	if (X == 4 ) return 1; 
	else if (O == 4 ) return 2; 
	else if ( T ==1 && X == 3) return 1;
	else if (T==1 && O == 3) return 2;

	X=0 ; O = 0 ; T= 0 ;
	for (int u = 0 ; u < 4; u++){
	if (arr[3][u] == 'X') X++;
	else if (arr [3][u]== 'O') O++;
	else if (arr [3][u]== 'T')T++;
	else if ( arr [3][u] == '.') draw = 0; 
	}
	if (X == 4 ) return 1; 
	else if (O == 4 ) return 2; 
	else if ( T ==1 && X == 3) return 1;
	else if (T==1 && O == 3) return 2;
	
	X=0 ; O = 0 ; T= 0 ;
	for (int u = 0 ; u < 4; u++){
	if (arr[u][0] == 'X') X++;
	else if (arr [u][0]== 'O') O++;
	else if (arr [u][0]== 'T')T++;
	else if ( arr [u][0] == '.') draw = 0; 
	}
	if (X == 4 ) return 1; 
	else if (O == 4 ) return 2; 
	else if ( T ==1 && X == 3) return 1;
	else if (T==1 && O == 3) return 2;
	

	X=0 ; O = 0 ; T= 0 ;
	for (int u = 0 ; u < 4; u++){
	if (arr[u][1] == 'X') X++;
	else if (arr [u][1]== 'O') O++;
	else if (arr [u][1]== 'T')T++;
	else if ( arr [u][1] == '.') draw = 0; 
	}

	if (X == 4 ) return 1; 
	else if (O == 4 ) return 2; 
	else if ( T ==1 && X == 3) return 1;
	else if (T==1 && O == 3) return 2;
	
	
	X=0 ; O = 0 ; T= 0 ;
	for (int u = 0 ; u < 4; u++){
	if (arr[u][2] == 'X') X++;
	else if (arr [u][2]== 'O') O++;
	else if (arr [u][2]== 'T')T++;
	else if ( arr [u][2] == '.') draw = 0; 
	}
	if (X == 4 ) return 1; 
	else if (O == 4 ) return 2; 
	else if ( T ==1 && X == 3) return 1;
	else if (T==1 && O == 3) return 2;
	
	
	X=0 ; O = 0 ; T= 0 ;
	for (int u = 0 ; u < 4; u++){
	if (arr[u][3] == 'X') X++;
	else if (arr [u][3]== 'O') O++;
	else if (arr [u][3]== 'T')T++;
	else if ( arr [u][3] == '.') draw = 0; 
	}
	if (X == 4 ) return 1; 
	else if (O == 4 ) return 2; 
	else if ( T ==1 && X == 3) return 1;
	else if (T==1 && O == 3) return 2;

	
	
	X=0 ; O = 0 ; T= 0 ;
	for (int u = 0 ; u < 4; u++){
	if (arr[u][u] == 'X') X++;
	else if (arr [u][u]== 'O') O++;
	else if (arr [u][u]== 'T')T++;
	else if ( arr [u][u] == '.') draw = 0; 
	}
	if (X == 4 ) return 1; 
	else if (O == 4 ) return 2; 
	else if ( T ==1 && X == 3) return 1;
	else if (T==1 && O == 3) return 2;
	
	X=0 ; O = 0 ; T= 0 ;
	for (int u = 0 ; u < 4; u++){
	if (arr[u][3-u] == 'X') X++;
	else if (arr [u][3-u]== 'O') O++;
	else if (arr [u][3-u]== 'T')T++;
	else if ( arr [u][3-u] == '.') draw = 0; 
	}
	if (X == 4 ) return 1; 
	else if (O == 4 ) return 2; 
	else if ( T ==1 && X == 3) return 1;
	else if (T==1 && O == 3) return 2;

	
	if (draw == 1) return 3;
	else return 4; 
}



	