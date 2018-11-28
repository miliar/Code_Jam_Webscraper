#include<iostream>
#include<vector>
#include<algorithm>


using namespace std;
int main()
{

	freopen("input.txt" , "r" , stdin );
	freopen("output.txt" , "w" , stdout );

	vector<int> first , second ;
	

	int arr[5][5] , arr1[2] ,  test_cases , Vo_num , INDEX ;
	bool check ;

	cin >> test_cases ;

	for( int test=0 ; test< test_cases ; test++ )
	{
		INDEX =0  , check = false ; 

		cin >> Vo_num ;
		for(int index=0 ; index < 4 ; index++ )
			for( int _index= 0 ; _index < 4 ; _index++ )
				cin >> arr[index][_index]; 

		for(int index=0 ; index < 4; index++ ) 
			first.push_back( arr[Vo_num-1][index] ) ;
		//sort( first.begin() , first.end()) ;

		cin >> Vo_num ;
		for(int index=0 ; index < 4 ; index++ )
			for( int _index= 0 ; _index < 4 ; _index++ )
				cin >> arr[index][_index];
		for(int index=0 ; index < 4; index++ ) 
			second.push_back( arr[Vo_num-1][index] );
		//sort( second.begin() , second.end()) ;

		for( int index =0 ; index < 4 ; index++)
		{
			for( int _index=0 ; _index< 4 ; _index++ )
			{
				if( INDEX > 1 ){
					check = true ; break;}

				if( first[index] == second[_index] )
					arr1[INDEX] = first[index] , INDEX++ ;
				
			}
		}

		cout<<"Case #"<<test+1<<": ";
		if( check == true  ) 
			cout<<"Bad magician!"<<endl;
		else
		{
			if ( INDEX == 0 ) 
				cout<<"Volunteer cheated!"<<endl;
			else
				cout<<arr1[0]<<endl;
		}
		
		first.clear() , second.clear();
		arr1[0] = 0 ;
	}


	return 0;
}