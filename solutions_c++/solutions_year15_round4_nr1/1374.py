#include <iostream>

using namespace std;

int Mapa[200][200];

bool SprawdzWszystko(int r,int c,int x,int y){
	bool czy;
	int x1,y1;
	czy = false;	
	x1 = x+1;
	while(x1<r){
		if(Mapa[x1][y] != 0 ) czy = true;
		x1++;
	}
	x1 = x-1;
	while(x1 >= 0){
		if(Mapa[x1][y] != 0 ) czy = true;
		x1--;
	}
	y1 = y+1;
	while(y1<c){
		if(Mapa[x][y1] != 0 ) czy = true;
		y1++;
	}
	y1 = y-1;
	while(y1 >= 0){
		if(Mapa[x][y1] != 0 ) czy = true;
		y1--;
	}
	return czy;
}

bool SprawdzKierunek(int r,int c,int x,int y,int p){
	bool czy;
	int x1,y1;
	czy = false;	
	if(p == 3){
		x1 = x+1;	
		while(x1<r){
			if(Mapa[x1][y] != 0 ) czy = true;
			x1++;
		}
	}
	if(p == 1){
		x1 = x-1;
		while(x1 >= 0){
			if(Mapa[x1][y] != 0 ) czy = true;
			x1--;
		}
	}
	if(p == 2){
		y1 = y+1;
		while(y1<c){
			if(Mapa[x][y1] != 0 ) czy = true;
			y1++;
		}
	}
	if( p == 4 ){
		y1 = y-1;
		while(y1 >= 0){
			if(Mapa[x][y1] != 0 ) czy = true;
			y1--;
		}
	}
	return czy;
}

int main(){
	char znak;
	int w;
	bool czy1,czy;
	int t,i,j,k,r,c;
	cin >> t;
	for(i=0; i<t; i++){
		cin >> r >> c;
		for(j=0; j<r; j++){
			for(k=0; k<c; k++){
				cin >> znak;
				if(znak == '.') Mapa[j][k] = 0;
				if(znak == '^') Mapa[j][k] = 1;
				if(znak == '>') Mapa[j][k] = 2;
				if(znak == 'v') Mapa[j][k] = 3;
				if(znak == '<') Mapa[j][k] = 4;
			}
		}
		czy1 = true;
		w = 0;
		for(j=0; j<r; j++){
			for(k=0; k<c; k++){
				if(Mapa[j][k] != 0){
					czy = SprawdzKierunek(r,c,j,k,Mapa[j][k]);
					if(!czy && !SprawdzWszystko(r,c,j,k)) {
						czy1 = false;
						break;
					}
					else{
						if(!czy) w++;
					}
				}
			}
			if(!czy1) break;
		}
		if(!czy1) cout << "Case #" << i+1 << ": IMPOSSIBLE" << "\n";
		else  cout << "Case #" << i+1 << ": " << w << "\n";
	}
	return 0;
}
