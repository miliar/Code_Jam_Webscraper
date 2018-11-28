// Google_CodeJam_2013_Round2_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{

	int t;
	cin>>t;
	for (int ii= 0; ii < t; ii++)
	{
		int now, tedad;
		int arr[101];
		int count = 0;
		cin>>now>>tedad;

		for (int i = 0; i < tedad; i++)
		{
			cin>>arr[i];
		}

		bool barr[101];
		for (int i = 0; i < tedad; i++)
		{
			barr[i] = true;
		}

		while(1)
		{

		for (int i = 0; i < tedad; i++)
		{
			if(barr[i] && now>arr[i])
			{
				now+=arr[i];
				barr[i] = false;
				i= -1;
			}
		}

		bool BREAK = true;
		for (int i = 0; i < tedad; i++)
		{
			if(barr[i])
			{
				BREAK = false;
				break;
			}
		}

		if(BREAK)
			break;

		int Imax = -1;

		int  MAX = 0 , IMAX = -1;

		int ekh = INT_MAX;
		for (int i = 0; i < tedad; i++)
		{
			if(barr[i] && (arr[i] - now < ekh))
			{
				Imax = i;
				ekh = arr[i] - now;
			}
			if(barr[i] && arr[i] >MAX)
			{
				IMAX = i;
				MAX = arr[i];
			}
		}
		

		if(now + (now-1) > arr[Imax])
		{
			count++;
			now += now-1;
		}
		else
		{
			int numoftrues =0;
			for (int i = 0; i < tedad; i++)
			{
				if(barr[i])
					numoftrues++;
			}

			int Tnow= now;
			for (int i = 0; i < numoftrues -1; i++)
			{
				Tnow += Tnow -1;
			}
			if(Tnow > arr[Imax])
			{
				now += now -1;
				count++;
			}
			else
			{
				barr[IMAX] = false;
				count++;
			}


		}
		

		

	}
		cout <<"Case #"<<ii+1<<": "<<count<<"\n";


	}
	return 0;
}

