//
//  main.cpp
//  codejam2
//
//  Created by XiaDsh on 4/13/14.
//  Copyright (c) 2014 XiaDsh. All rights reserved.
//

#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;


int cmp(const void *a, const void *b)
{
    int *pa = (int*)a;
    int *pb = (int*)b;
    return (*pa )- (*pb);  //¥”–°µΩ¥Û≈≈–Ú
}


int main(void)
{
	ifstream in("/Users/Tony/Documents/D-small-attempt0.in.txt");
	ofstream out("/Users/Tony/Documents/D-outfile");
    
	if (!in.is_open() || !out.is_open())
	{
		cout<<"Error Filepath!!"<<endl;
	}
    
	int t = 0,n = 0;
	float nao[10],ken[10];
    
	int d = 0, w =0;
    
	in >> t;
    
	for(int i = 0; i < t; i++)
	{
		in >> n;
		for( int j = 0; j < n; j++)
		{
			in >> nao[j];
		}
		for( int j = 0; j < n; j++)
		{
			in >> ken[j];
		}
		qsort(nao,n,sizeof(float),cmp);
		qsort(ken,n,sizeof(float),cmp);
		d = 0;
		int k = 0, m = 0;
		for(;k<n;k++)
		{
			if(nao[k] > ken[m])
			{
				d++;
				m++;
			}
		}
		w = 0;
		for(int p = n-1; p >= 0 ; p--)
		{
			//compare the t
			int q = n -1 ;
			int fl1 = n -2 -p;
			for( int q = n -1; q >= n-1 -p;q--)
			{
				if(nao[p] > ken [q])
				{
					fl1 = q;
					break;
				}
			}
			if( fl1 == n-1)
			{
				w ++;
				ken[n-1-p] = 0;
			}
			else
			{
				ken[fl1 +1] =0;
				for( int s = fl1 +1; s > n-1-p;s--)
				{
					ken[s] = ken[s-1];
				}
			}
		}
		out<<"Case #"<<i+1<<": "<<d<<" "<<w<<endl;
		
	}
	
    
	return 0;
    
}

