
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <cstdio>


using namespace std;


vector<float> merge_sort( vector<float> data ){
	if( data.size() <= 1 ){
		return data;
	}
	
	int middle = data.size() / 2;
	vector<float> left( data.begin(), data.begin()+middle );
	vector<float> right( data.begin()+middle, data.end() );

	left = merge_sort( left );
	right = merge_sort( right );

	vector<float> result( data.size() );
	merge( left.begin(), left.end(),
		right.begin(), right.end(),
		result.begin() );

	return result;
}


int play_DWar(vector<float> NB, vector<float> KB ){

	int points = 0;

	for( int i = (KB.size()-1); i >= 0; i-- ){
		
		int j= NB.size()-1;

		while( j >= 0 && NB[j] < KB[i] ){
			j--;
		}

		if( j >=0 ){
			points++;
			NB.erase(NB.begin() + j);
		}

		KB.erase(KB.begin() + i);

	}

	return points;

}



int play_War(vector<float> NB, vector<float> KB ){

	int points = 0;

	for( int i = (NB.size()-1); i >= 0; i-- ){
		if( NB[i] > KB[i] ){
			points++;
			NB.erase( NB.begin() + NB.size() - 1 );
			KB.erase( KB.begin() );
		}
		else{
			NB.erase( NB.begin() + NB.size() - 1 );
			KB.erase( KB.begin() + KB.size() - 1 );
		}
	}

	return points;

}


int main(int argc, char** argv){

	int T, N, WarPoints, DWarPoints;
	float block;
	//vector< float > NB;
	//vector< float > KB;

	cin >> T;

	for( int i=1; i <= T; i++ ){

		vector< float > NB;
		vector< float > KB;

		cin >> N;

		for( int j=0; j < N; j++ ){
			cin >> fixed >> setprecision(5) >> block;
			NB.push_back( block );
		}

		for( int j=0; j < N; j++ ){
			cin >> fixed >> setprecision(5) >> block;
			//cin >> block;
			KB.push_back( block );
		}

		

		NB = merge_sort( NB );
		
		KB = merge_sort( KB );

		WarPoints = play_War( NB, KB );

		reverse( NB.begin(), NB.end() );
		reverse( KB.begin(), KB.end() );
//
		/*for( int j=0; j < N; j++ ){
			cout << NB[j] << "  ";
		}
		cout << endl;*/

		DWarPoints = play_DWar( NB, KB );

		cout << "Case #" << i << ": " << DWarPoints << " " << WarPoints << endl;

		//Next case
		//NB.resize(0);
		//KB.resize(0);

	}

	return 0;
}














