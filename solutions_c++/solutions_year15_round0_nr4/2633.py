// 10.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
	FILE *f;
	freopen_s(&f,"in.txt","r",stdin);
	freopen_s(&f,"out.txt","w",stdout);
	int T;
	cin>>T;
	int X,R,C,_min,_max;
	for (int i=0; i<T; i++)
	{
		cin>>X>>R>>C;
		_min=min(R,C);
		_max=max(R,C);
		cout<<"Case #"<<i+1<<": ";
		if ((X/2<_min&&_max>=X&&(R*C)%X==0)||X==2&&_max%2==0)
		{
			cout<<"GABRIEL";
		}
		else
			cout<<"RICHARD";
		cout<<endl;
	}
	return 0;
}

