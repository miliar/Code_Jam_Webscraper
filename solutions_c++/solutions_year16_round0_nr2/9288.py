#include<iostream>
#include<string>
#include<cstdlib>
#include<cstdio>
#include <vector>
#include <iostream>
#include <iterator>
#include <algorithm>
using namespace std;

string cake,copycake;

int result()
{
	int r = 0, total;
	total = cake.size();
	int v = 0;
	for (int i = 0; i<total; i++)
	{
		if (cake[i] == '+')
		{
			v++;
		}
	}
	int flip, i;
	char tag;
	while (v < total && r<1000)
	{
		tag = cake[0];
		flip = 0;
		while (cake[flip] == tag)
		{
			flip++;
		}
		for (i = 0; i < flip; i++)
		{
			if (tag == '+')
			{
				v--;
				cake[flip - i-1] = '-';
			}
			else
			{
				cake[flip - i-1] = '+';
				v++;
			}
		}
		r++;
		//cout << cake << "\t" << r << endl;
	}
	return r;
}


int main()
{
	int t;
	//freopen("B-large.in","r",stdin);
    //freopen("Boutput.out","w",stdout);
	cin >> t;
	int i = 0;
	int sol1, sol2,m,n;
	char temp;
	while (i<t)
	{
		i++;
		cin >> cake;
		copycake = cake;
		sol1 = result();
		cake = copycake;
		m=0;n=cake.size()-1;
		while(m<n)
        {
            temp = cake[m];
            cake[m] = cake[n];
            cake[n] = temp;
            m++;
            n--;
        }
//		reverse(std::begin(cake),std::end(cake));
		//cout << "Reversed: " << cake << endl;;
		sol2 = result() + 1;
		//cout << sol1 << " \t" << sol2 << endl;
		if (sol1 > sol2)
			sol1 = sol2;
		cout<<"Case #"<<i<<": "<< sol1 << endl;
	}
	return 0;
}
