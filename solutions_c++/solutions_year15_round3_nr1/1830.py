// 1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	FILE *f;
	freopen_s(&f,"in.txt","r+",stdin);
	freopen_s(&f,"out.txt","w+",stdout);
	int t,r,c,w;
	cin>>t;
	int ans;
	for (int it=0; it<t; it++)
	{
		ans=0;
		cin>>r>>c>>w;
		switch (c)
		{
		case 1:
			ans=0;
			break;
		case 2:
			{
				switch (w)
				{
				case 1:
					ans=1;
					break;
				case 2:
					ans=0;
					break;
				default:
					break;
				}}
			break;
		case 3:
			{
				switch (w)
				{
				case 1:
					ans=2;
					break;
				case 2:
					ans=1;
					break;
				case 3:
					ans=0;
					break;
				default:
					break;
				}}
			break;
		case 4:
			{
				switch (w)
				{
				case 1:
					ans=3;
					break;
				case 2:
					ans=1;
					break;
				case 3:
					ans=1;
					break;
				case 4:
					ans=0;
					break;
				default:
					break;
				}}
			break;
		case 5:
			{
				switch (w)
				{
				case 1:
					ans=4;
					break;
				case 2:
					ans=2;
					break;
				case 3:
					ans=1;
					break;
				case 4:
					ans=1;
					break;
				case 5:
					ans=0;
					break;
				default:
					break;
				}}
				break;
		case 6:
			{
				switch (w)
				{
				case 1:
					ans=5;
					break;
				case 2:
					ans=2;
					break;
				case 3:
					ans=1;
					break;
				case 4:
					ans=1;
					break;
				case 5:
					ans=1;
					break;
				default:
					ans=0;
					break;
				}}
				break;
		case 7:
			{
				switch (w)
				{
				case 1:
					ans=6;
					break;
				case 2:
					ans=3;
					break;
				case 3:
					ans=2;
					break;
				case 4:
					ans=1;
					break;
				case 5:
					ans=1;
					break;
				case 6:
					ans=1;
					break;
				default:
					ans=0;
					break;
				}}
				break;
		case 8:
			{
				switch (w)
				{
				case 1:
					ans=7;
					break;
				case 2:
					ans=3;
					break;
				case 3:
					ans=2;
					break;
				case 4:
					ans=1;
					break;
				case 5:
					ans=1;
					break;
				case 6:
					ans=1;
					break;
				case 7:
					ans=1;
					break;
				default:
					ans=0;
					break;
				}}
				break;
		case 9:
			{
				switch (w)
				{
				case 1:
					ans=8;
					break;
				case 2:
					ans=4;
					break;
				case 3:
					ans=2;
					break;
				case 4:
					ans=2;
					break;
				case 5:
					ans=1;
					break;
				case 6:
					ans=1;
					break;
				case 7:
					ans=1;
					break;
				case 8:
					ans=1;
					break;
				default:
					ans=0;
					break;
				}}
				break;
		case 10:
			{
				switch (w)
				{
				case 1:
					ans=9;
					break;
				case 2:
					ans=4;
					break;
				case 3:
					ans=3;
					break;
				case 4:
					ans=2;
					break;
				case 5:
					ans=1;
					break;
				case 6:
					ans=1;
					break;
				case 7:
					ans=1;
					break;
				case 8:
					ans=1;
					break;
				case 9:
					ans=1;
					break;
				default:
					ans=0;
					break;
				}}
				break;
		default:
			break;
			}
			if (r>1&&ans==0)
			{
				ans=r-1;
			}
			else if (r>1)
			{
				ans=(ans+1)*(r-1)+ans;
			}
			cout<<"Case #"<<it+1<<": "<<ans+w<<endl;
			}
	return 0;
}

