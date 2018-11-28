#include <iostream>
#include <stdio.h>
using namespace std ;
int main ()
{

    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);


	int tstCases , firstRowChoice , secondRowChoice , arr1[4][4] , arr2[4][4] , count = 0  , out = 0 ;

	cin >> tstCases ;



	for ( int z = 0 ; z < tstCases ; ++z)
	{

	cin >> firstRowChoice;

    --firstRowChoice;

	for ( int i = 0 ; i < 4 ; ++i)
		for ( int j = 0 ; j < 4 ; ++j)
				cin >> arr1[i][j];

	cin >> secondRowChoice;

	--secondRowChoice;

	for ( int i = 0 ; i < 4 ; ++i)
		for ( int j = 0 ; j < 4 ; ++j)
				cin >> arr2[i][j];



	for (int i = 0 ; i < 4 ; ++i)
		for ( int j = 0 ; j < 4 ; ++j)
		{
			if (arr1[firstRowChoice][i] == arr2[secondRowChoice][j])
			{
				out = arr2[secondRowChoice][j];
				cout << out << endl;
				++count ;
			}
        }

		    if ( count == 1 )
				 printf("Case #%i: %d\n", (z+1) , out  );

	 		else if (count == 0 )
	 				printf("Case #%i: Volunteer cheated!\n", (z+1)  );

	 		else
	 				printf("Case #%i: Bad magician!\n", (z+1)  );

	 			count = 0 ;

	}
	return 0 ;
}
