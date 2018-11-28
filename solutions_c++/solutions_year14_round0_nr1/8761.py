// codejam1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

void main()
{
	int n;
	fstream fin, fout;
	fin.open("A-small-attempt2.in");
	fout.open("A-small-attempt1.out.txt", ios::out);

	fin>>n;
	int nums1[4];
	int nums2[4];
	int temp[4];

	for(int i = 0; i<n; i++)
	{
		int line1;
		fin>>line1;

		for(int j = 1; j<line1; j++)
			fin>>temp[0]>>temp[1]>>temp[2]>>temp[3];

		fin>>nums1[0]>>nums1[1]>>nums1[2]>>nums1[3];

		for(int j = line1+1; j<=4; j++)
			fin>>temp[0]>>temp[1]>>temp[2]>>temp[3];

		int line2;
		fin>>line2;

		for(int j = 1; j<line2; j++)
			fin>>temp[0]>>temp[1]>>temp[2]>>temp[3];

		fin>>nums2[0]>>nums2[1]>>nums2[2]>>nums2[3];

		for(int j = line2+1; j<=4; j++)
			fin>>temp[0]>>temp[1]>>temp[2]>>temp[3];

		int result = -1;
		int cnt = 0;
		for(int k = 0; k<4; k++)
		{
			for(int l = 0; l<4; l++)
			{
				if(nums1[k] == nums2[l])
				{
					result = nums1[k];
					cnt++;
				}
			}
		}

		if(cnt == 1)
		{
			fout<<"case #"<<i+1<<": "<<result<<endl;
			cout<<"case #"<<i+1<<": "<<result<<endl;
		}
		else if (cnt == 0)
		{
			fout<<"case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
			cout<<"case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
		}
		else
		{
			fout<<"case #"<<i+1<<": "<<"Bad magician!"<<endl;
			cout<<"case #"<<i+1<<": "<<"Bad magician!"<<endl;
		}
	}

	fin.close();
	fout.close();
}

