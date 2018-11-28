#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
	int my_mote, num;
	int i, j, testcases;
	int *motes;

	int remove[20], k;

	int ADD, REMOVE, EATEN;
	int MIN, pos, LEFT;

	cin>>testcases;
	i = 1;
	k=0;

	while(i <= testcases )
	{
		cin>>my_mote>>num;

		motes = new int[num];

		ADD = REMOVE = 0;

		for (j=0; j<k; j++)
			remove[j] = -1;

		k=0;
		
		for (j=0; j<num; j++)
			cin>>motes[j];

//		cout <<"my_mote = "<<my_mote<<" & num = "<<num<<"\n";
//		for (j=0; j<num; j++)
//			cout<<"mote = "<<motes[j]<<",";

		while(1)
		{
			EATEN = 1;
			while(EATEN == 1)
			{
				EATEN = 0;
			
				for(j=0; j<num; j++)
				{
					if ( motes[j] == -1 )
						continue;
	
					if ( motes[j] < my_mote )
					{
						my_mote += motes[j];
						EATEN = 1;
						motes[j] = -1;
					}
				}
			}

			LEFT = 0;
			for ( j=0; j<num; j++)
			{
				if ( motes[j] != -1 )
					LEFT++;
			}

			if ( LEFT == 0 )
				break;

			MIN = 1000;
			pos = 0;
			for ( j=0; j<num; j++)
			{
				if ( motes[j] == -1 )
					continue;

				if ( motes[j] < MIN )
				{
					MIN = motes[j];
					pos = j;
				}
			}

			if ( my_mote + my_mote - 1  > motes[pos] )
			{
				ADD++;
				my_mote = my_mote + my_mote - 1 + motes[pos];
				motes[pos] = -1;
			}
			else
			{
				remove[k] = LEFT + REMOVE;
				k++;

				if ( my_mote == 1 )
				{
					REMOVE = 1000;
					break;
				}

				while ( my_mote <= motes[pos] )
				{
					my_mote = my_mote + my_mote -1;
					REMOVE++;
				}
				my_mote = my_mote +  motes[pos];
				motes[pos] = -1;
			}
		}

		MIN = 1000;
		for (j=0;j<k;j++)
		{
			if ( remove[j] < MIN )
				MIN = remove[j];
		}

		if ( REMOVE < MIN )
			MIN = REMOVE;
		
		cout<<"Case #"<<i<<": "<<ADD+MIN<<"\n";

		i++;
	}

	return 0;
}
