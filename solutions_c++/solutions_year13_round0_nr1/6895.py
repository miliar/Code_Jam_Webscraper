#include<iostream>
using namespace std;
char ar[5][5];

int checkcross(int hor)
{
	int i;
	int tFound = 0;
	int count = 0;
	int b;
	for(i=0;i<4;i++){
		if(hor){
			b = 3 - i;
		}
		else{
			b = i;
		}
		if(ar[i][b] == 'T'){
			tFound = 1;
		}
		if(ar[i][b] == 'X'){
			count++;
		}
		if(ar[i][b] == 'O'){
			count--;
		}
	}
	if( count == 4 ){
		cout<<"X won\n";
		return 1;
	}
	if( count == -4 ){
		cout<<"O won\n";
		return 1;
	}
	if( count == 3 && tFound == 1 ){
		cout<<"X won\n";
		return 1;
	}
	if( count == -3 && tFound == 1 ){
		cout<<"O won\n";
		return 1;
	}
}

int testh(int hor)
{
	int a, b;
	int i,j;
	int count=0, tFound = 0;
	for(i=0;i<4;i++){
		count = 0;
		tFound = 0;
		for(j=0;j<4;j++){
			if(hor==1){
				a = i;
				b = j;
			}
			else{
				a = j;
				b = i;
			}
			if(ar[a][b] == 'T'){
				tFound = 1;
			}
			if(ar[a][b] == 'X'){
				count++;
			}
			if(ar[a][b] == 'O'){
				count--;
			}
		}
		if( count == 4 ){
			cout<<"X won\n";
			return 1;
		}
		if( count == -4 ){
			cout<<"O won\n";
			return 1;
		}
		if( count == 3 && tFound == 1 ){
			cout<<"X won\n";
			return 1;
		}
		if( count == -3 && tFound == 1 ){
			cout<<"O won\n";
			return 1;
		}
	}
}

int main()
{
	int n;
	int i,j,k;
	int incomplete = 0;
	cin >> n;
	for(i=0;i<n;i++){
		incomplete = 0;
		for(j=0;j<4;j++){
			for(k=0;k<4;k++){
				cin>>ar[j][k];
				if(ar[j][k] == '.'){
					incomplete = 1;
				}
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if( !testh(0) && !testh(1) && !checkcross(1) && !checkcross(0)){
			if(incomplete){
				cout<<"Game has not completed\n";
			}
			else{
				cout<<"Draw\n";
			}
		}
	}
}
