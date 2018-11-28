#include<iostream>
#include<vector>
#include<algorithm>
#include <string>
using namespace std;
 
string arr[5];

bool check(char p)
{
	for(int i=0;i<4;i++)
	{
		bool f = true;
		for(int j=0;j<4;j++)
			if(arr[i][j] != p && arr[i][j] != 'T')
				f = false;
		if(f)
			return true;
	}

	for(int i=0;i<4;i++)
	{
		bool f = true;
		for(int j=0;j<4;j++)
			if(arr[j][i] != p && arr[j][i] != 'T')
				f = false;
		if(f)
			return true;
	}
	bool f = true;

	for(int i=0;i<4;i++)
		if(arr[i][i] != p && arr[i][i] != 'T')
			f = false;
	
	if(f)
		return true;
	else
		f = true;

	for(int i=0;i<4;i++)
		if(arr[i][3-i] != p && arr[i][3-i] != 'T')
			f = false;
	return f;
}


string solve()
{
	if(check('X'))
		return "X won";
	if(check('O'))
		return "O won";
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(arr[i][j] == '.')
				return "Game has not completed";
	return "Draw";
}

 
int main() {
 
	freopen("input.txt","r",stdin);

	freopen("output.txt", "w", stdout);


	int k;
	cin>>k;

	for(int i=0;i<k;i++)
	{
		for(int j=0;j<4;j++)
			cin>>arr[j];

		cout<<"Case #"<<i+1<<": "<<solve()<<endl;
	}


    return 0;
}