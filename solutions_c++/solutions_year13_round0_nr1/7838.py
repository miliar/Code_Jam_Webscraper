#include <iostream>
using namespace std;

int n;
string linii[5],lino[5];

bool solveme(string lin[],char ww){
	
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(lin[i][j]=='T') lin[i][j] = ww;
			//cout << lin[i][j];
		}
		//cout << endl;
	}

	

		for(int i=0;i<4;i++)
		{
		
			//Stulbove		
			if(lin[i][0] == ww && lin[i][1] == ww && lin[i][2] == ww && lin[i][3] == ww) return true;
			
			//Redove
			if(lin[0][i] == ww && lin[1][i] == ww && lin[2][i] == ww && lin[3][i] == ww) return true;
					
		}
		
			//Diagonali
			if(lin[0][0] == ww && lin[1][1] == ww && lin[2][2] == ww && lin[3][3] == ww) return true;
			if(lin[0][3] == ww && lin[1][2] == ww && lin[2][1] == ww && lin[3][0] == ww) return true;

 return false;
 
}

string solve(){
		
	//Game has not completed
	bool nc = true;
	for(int i=0;i<4;i++) if(linii[i][3]!='.' || linii[3][i]!='.') nc = false;
	if(nc) return "Game has not completed";
	
	
	//for(int i=0;i<4;i++){ for(int j=0;j<4;j++){ lino[i][j] = linii[i][j]; } }
	for(int i=0;i<4;i++) lino[i] = linii[i];
	

	if(solveme(linii,'X')) return "X won";
	if(solveme(lino,'O')) return "O won";
	
	for(int i=0;i<4;i++){for(int j=0;j<4;j++){if(linii[i][j]=='.') return "Game has not completed";}}
	return "Draw";
}

void read(){
	
	for(int l=0;l<4;l++)
	{
		getline(cin,linii[l]);
	}
	getline(cin,linii[4]);
}


int main(){

cin >> n;
getline(cin,linii[4]);


for(int i=1;i<=n;i++)
{
	read();
	cout << "Case #" << i << ": " << solve() << endl;
}

return 0;
}
