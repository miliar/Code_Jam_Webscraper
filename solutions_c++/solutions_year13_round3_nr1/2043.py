
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <map>
#include <cstdlib>
#include <vector>
#include <iterator>
#include <fstream>
#include <list>
#include <queue>
#include <stdlib.h>
#include <cstring>
#include <sstream>
using namespace std;

#define N 1000000007
char vol[] = {'a' , 'e' , 'i' , 'o' , 'u'};

bool notvol(char a)
{
	for(int i = 0 ; i < 5 ; i ++)
	{
		if(a == vol[i])
			return false;
	}
	return true;
}



int find(string &a ,string &c ,  map<string , vector<int> > &t , int e)
{
	int i = e;
	int beg = e - c.size();
	int ans = 0;
	int n = c.size();
	string b(c);
	for(int j = beg ; j >= 0 ; j --)
	{
		string k = a.substr(j , n);
		map<string , vector<int> >::iterator it = t.find(k); 
		if(it == t.end())
		{
			t[k].push_back(e);
			ans ++;
		}
		else
		{
			vector<int>::iterator nit = it->second.begin();
			bool flag = true;
			for(;nit != it->second.end() ; nit ++)
			{
				if(*nit == e)
				{
					flag = false;
					break;
				}
			}
			if(flag)
			{
				t[k].push_back(e);
				ans ++;
			}
		}
		for(i = e; i < a.size() ; )
		{
			k.push_back(a[i]);
			i ++;
			map<string , vector<int> >::iterator it = t.find(k); 
			if(it == t.end())
			{
				t[k].push_back(i);
				ans ++;
			}
			else
			{
				vector<int>::iterator nit = it->second.begin();
				bool flag = true;
				for(;nit != it->second.end() ; nit ++)
				{
					if(*nit == i)
					{
						flag = false;
						break;
					}
				}
				if(flag)
				{
					t[k].push_back(i);
					ans ++;
				}
			}

		}
		
		n ++;
	}
	
	


	return ans;
}


int main()
{
	ifstream in("1.in");
	ofstream out("ans.out");
	int casen , index = 0;
	in >> casen;
	
	while(index < casen)
	{
		index ++;
		string a ;
		int ans = 0;
		int n;
		in >> a >> n;
		map<string , vector<int> > t;
		int i = 0;
		int l = a.size() - n + 1;
		while(i < l)
		{
			int j = i;
			string b;
			for(; j < i + n ; j ++ )
			{
				if(notvol(a[j]))
				{
					b.push_back(a[j]);
				}
				else
				{
					break;
				}
			}
			if(j == i + n)
			{
				//я╟ур
				ans += find(a , b , t , j);
				while(j < a.size() && notvol(a[j]))
				{
					b.erase(b.begin());
					b.push_back(a[j]);
					//я╟ур
					j ++;
					ans += find(a , b , t , j);
					
				}
				j ++;
				i = j;
			}
			else
			{
				j ++;
				i = j;
			}
		}
		out << "Case #" << index << ": " << ans << endl;
	}
	return 0;
}