
#include <iostream>
using namespace std;
char broad[4][4];
bool TESTWIN(char cx, int &a, int x, int y, int xx, int yx){
	int i;
	char c;
	for(i=0; i<4; i++){
		c = broad[x+xx*i][y+yx*i];
		if((c!=cx)&&(c!='T')){
			if(c!='.'){
				a++;
			}
			return false;
		}
	}
	return true;
}
int RUN(){
	int	i,
		a=0;
	for(i=0; i<4; i++){
		if(TESTWIN('X',a,i,0,0,1)) return 1;
		if(TESTWIN('O',a,i,0,0,1)) return 2;
	}
	for(i=0; i<4; i++){
		if(TESTWIN('X',a,0,i,1,0)) return 1;
		if(TESTWIN('O',a,0,i,1,0)) return 2;
	}
	if(TESTWIN('X',a,0,0,1,1)) return 1;
	if(TESTWIN('O',a,0,0,1,1)) return 2;
	if(TESTWIN('X',a,0,3,1,-1)) return 1;
	if(TESTWIN('O',a,0,3,1,-1)) return 2;
	if(a==20)return 0;
	else return 3;
}
int main(){
	int	T,
		i, j, k,
		result;
	cin>>T;
	for(k=1; k<=T; k++){
		memset(broad,0,sizeof(broad));
		for(i=0; i<4; i++){
			for(j=0; j<4; j++){
				cin>>broad[i][j];
			}
		}
		cout<<"Case #"<<k<<": ";
		result = RUN();
		switch (result){
			case 0:	cout<<"Draw";
					break;
			case 1:	cout<<"X won";
					break;
			case 2:	cout<<"O won";
					break;
			case 3:	cout<<"Game has not completed";
		}
		cout<<endl;
	}
	return 0;
}
