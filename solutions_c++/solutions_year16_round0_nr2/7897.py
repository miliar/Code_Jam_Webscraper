#include "iostream"
#include "vector"
#include "string"
using namespace std;
vector <int>  arr;
vector <int>  reff;
int  temparr[100];
int flip_pan(int c)
{

	if (arr != reff)
	{	
		if (arr[0] == 1) //top +
		{
			int i = 0;
			while (arr[i])
			{ 
				arr[i] = 0;
				i++;
			}
			c = flip_pan(++c);
		}
		else   // top -
		{
			//if (arr != reff)
			//{
				int l = arr.size();
				l--;
				while (arr[l]==1)
				{
					l--;
				}

				//use l 
				for (int i = 0; i <= l; i++)    //reverse
				     temparr[i] = arr[l-i];
				for (int i = 0; i <= l; i++)    //flip
					arr[i] = (temparr[i] == 1) ? 0 : 1;
				
				    
				c = flip_pan(++c);
			//}
			//else
			//	return c;

		}


	}
	else 
	  return c;
}
int main(){
	int T,out;
	string s;
	//freopen("input.txt", "r", stdin);
	//freopen("outputBlarge.txt", "w", stdout);
	cin >> T;
	int t = 0;
	while (T--)
	{
		cin >> s;
		arr.assign(s.length(), 0);
		reff.assign(s.length(), 1);
		for (int i = 0; i < s.length(); i++)
		{
			arr[i] = (s[i] == '+') ? 1 : 0;
		}
		out = flip_pan(0);
		cout << "Case #" << ++t << ": " << out << endl;
	}
	return 0;
}