#include<iostream>
#include<cstdio>

using namespace std;

int main(){
	int t,n,arr1[4][4],arr2[4][4],possibleanswers1[4],possibleanswers2[4],answerindex=-1,cases=1;
	scanf( "%d" , &t );
	while( t-- ){
		cin>>n;
		for(int i = 0 ; i < 4 ; i++ )
			for( int j = 0 ; j < 4 ; j++ )
				cin>>arr1[i][j];
		for( int i = 0 ; i < 4 ; i++ )	possibleanswers1[i] = arr1[n-1][i];
		cin>>n;
		for(int i = 0 ; i < 4 ; i++ )
			for( int j = 0 ; j < 4 ; j++ )
				cin>>arr2[i][j];	
		for( int i = 0 ; i < 4 ; i++ )	possibleanswers2[i] = arr2[n-1][i];
		
		
		int flag = 0;
		for( int i = 0 ; i < 4 ; i++ ){
			for(int j = 0 ; j < 4 ; j++ ){
				if(possibleanswers1[i] == possibleanswers2[j] ){
					flag++;
					answerindex = i;
				}
			}
		}
		if( flag == 0 ){
			cout<<"Case #"<<cases++<<": Volunteer cheated!\n";
		}
		else if( flag == 1 ){
			cout<<"Case #"<<cases++<<": "<<possibleanswers1[answerindex]<<endl;
		}
		else{
			cout<<"Case #"<<cases++<<": Bad magician!\n";
		}
	}
	return 0;
}

