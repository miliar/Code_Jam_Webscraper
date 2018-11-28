#include <iostream.h>
#include <stdlib.h>

void main()
{
	char *audPtr;
	unsigned int sMax=0, caseNum=0, T=0, indx=0, stoodUp=0, friendsReq=0;

	cin>>T;

	while(T--)
	{
		++caseNum;

		cin>>sMax;
		audPtr = (char*)calloc(sMax+1, sizeof(char));

		for(indx=0 ; indx<(sMax+1) ; ++indx)
			cin>>audPtr[indx];

		stoodUp = friendsReq = 0;

		stoodUp = audPtr[0]-'0';		//with zero Shyness Level
		for(indx=1 ; indx<(sMax+1) ; ++indx)
		{	if(audPtr[indx] == '0')
				continue;

			if(stoodUp >= indx)
				stoodUp += audPtr[indx]-'0';
			else
			{
				friendsReq += indx - stoodUp;
				stoodUp += friendsReq + audPtr[indx]-'0';
			}
		}

		free(audPtr);

		cout<<"Case #"<<caseNum<<": "<<friendsReq<<endl;
	}

}