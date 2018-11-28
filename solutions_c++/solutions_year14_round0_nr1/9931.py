#include <iostream>
#include <vector>
#include <cstdio>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;



int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin >> t;
	for(int k=1;k<=t;k++)
	{
		int pos1,pos2,arr1[4],arr2[4],tmp;
		cin >> pos1;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				if(i==pos1)
					cin >> arr1[j-1];
				else
					cin >> tmp;
			}
		}
		cin >> pos2;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				if(i==pos2)
					cin >> arr2[j-1];
				else
					cin >> tmp;
			}
		}
		int cnt=0,num;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(arr1[i] == arr2[j])
				{
					cnt++;
					num =arr1[i];
				}
			}
		}

		if (cnt == 1)
			cout << "Case #" << k << ": " << num << endl;
		else if(cnt ==0)
			cout << "Case #" << k << ": " << "Volunteer cheated!" << endl;
		else if(cnt >1 )
			cout << "Case #" << k << ": " << "Bad magician!" << endl;
	}

}
