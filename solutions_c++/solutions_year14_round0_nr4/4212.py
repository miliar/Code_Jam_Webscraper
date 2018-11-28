#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;

ifstream fin;
ofstream fout;

//vector<double> v1;
//vector<double> v2;

bool cmp( double a , double b )
{
	return a > b;
}

int main()
{
	fin.open("D_large.in");
	fout.open("d_large.out");
	
	int T = 0 , N = 0;;
	int i , j , k;
	int deceitful , war;
	double input;
	double v1[1010];
	double v2[1010];
	
	fin >> T;
	for( int t = 1 ; t <= T ; ++t )
	{
		fin >> N;
		for( i = 0 ; i < N ; ++i )
		{
			fin >> input;
			//v1.push_back(input);
			v1[i] = input;
		}
		//sort( v1.begin() , v1.end() , cmp );
		sort( v1 , v1+N , cmp );
		for( i = 0 ; i < N ; ++i )
		{
			fin >> input;
			//v2.push_back(input);
			v2[i] = input;
		}
		//sort( v2.begin() , v2.end() , cmp);
		sort( v2 , v2+N , cmp );
		/*
		for( i = 0 ; i < N ; ++i )
		{
			cout << v1[i] << "  " << v2[i] << endl;
		}
		*/
		
		//count deceitful war point
		deceitful = 0;
		war = 0;
		for( i = 0 , j = 0 ; j < N ; )
		{
			if( v1[i] > v2[j] )
			{
				++deceitful;
				++i;
				++j;
			}
			else //if( v1[i] < v2[j])
			{
				++j;
			}
		}
		//count original war point
		for( i = 0 , j = 0 ; j < N ; )
		{
			if( v2[i] > v1[j] )
			{
				++i;
				++j;
			}
			else //if( v1[i] < v2[j])
			{
				++war;
				++j;
			}
		}
		
		fout << "Case #" << t << ": " << deceitful << " " << war << endl;
		//v1.clear();
		//v2.clear();
	}
	
	return 0;
}
