#include <string>
#include <set>
#include <iostream>
#include <vector>
#include <typeinfo>
#include <algorithm>
#include <functional>
#include <numeric>
#include <list>
#include <sstream>
#include <map>
#include<unordered_map>
#include<fstream>
using namespace std;


 typedef vector<int> vi; 
 typedef vector<vi> vvi; 
 typedef pair<int,int> ii; 
 typedef vector<pair<int,int> > vii;
 #define sz(a) int((a).size()) 
 #define pb push_back 
 #define all(c) (c).begin(),(c).end() 
 #define tr(c,i)  for(auto i = (c).begin(); i != (c).end(); i++) 
 #define tre(c,i)  for(auto i = (c).rbegin(); i != (c).rend(); i++) 
 #define present(c,x) ((c).find(x) != (c).end()) 
 #define cpresent(c,x) (find(all(c),x) != (c).end()) 
 
 typedef vector<pair<pair<int,int>,int> > viii; 
 
template<class T>
vector<T> split(string& str)
{

	T word;
	istringstream iss(str, istringstream::in);
	vector<T> v;
	while( iss >> word )     
	{

		v.push_back(word);

	}
	return v;
}

string res;


string mower_solve(vector<vector<int> > &mower_matrix,int m,int n)
{
	vi row_max(m,0);
	vi col_max(n,0);

	for(int i=0;i<m;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(mower_matrix[i][j]>row_max[i])
			{
				row_max[i]=mower_matrix[i][j];
			}
		}
	}

	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(mower_matrix[j][i]>col_max[i])
			{
				col_max[i]=mower_matrix[j][i];
			}
		}
	}

	for(int i=0;i<m;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(mower_matrix[i][j]==col_max[j] || mower_matrix[i][j]==row_max[i])
			{
				continue;
			}
			else
			{
				return "NO";
			}
		}
	}

	return "YES";
}

int main()
{

	string givenS;
	
	int testcases;
	cin>>testcases;
	int x;
	int testcase_no=1;
	while(testcases--)
	{
		int m,n;
		cin>>m>>n;
		vector<vector<int> > mower_matrix(m,vector<int>(n));
	
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			{
				cin>>x;
				mower_matrix[i][j]=x;
			}
		}


		cout<<"Case #"<<testcase_no<<": "<<mower_solve(mower_matrix,m,n)<<endl;
		testcase_no++;
	}
	return 0;
}