#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;

int main()
{
   // freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	string s;
	cin>>T;
	for(int i = 0; i < T; i++)
    {
        vector<int> ltr(26, 0);
		vector<int> digit;
		cin >> s;
		//cout<<s<<endl;
		for(int i = 0; i < s.length();i++)
        {
            ltr[s[i] - 'A']+= 1;
        }
        if(ltr['Z' - 'A'] != 0)
        {
            while(ltr['Z' - 'A'])
            {
                digit.push_back(0);
                ltr['Z' - 'A']--;
                ltr['E' - 'A']--;
                ltr['R' - 'A']--;
                ltr['O' - 'A']--;
            }
        }
        if(ltr['W' - 'A'] != 0)
        {
            while(ltr['W' - 'A'])
            {
                digit.push_back(2);
                ltr['T' - 'A']--;
                ltr['W' - 'A']--;
                ltr['O' - 'A']--;
            }
        }
        if(ltr['G' - 'A'] != 0)
        {
            while(ltr['G' - 'A'])
            {
                digit.push_back(8);
                ltr['E' - 'A']--;
                ltr['I' - 'A']--;
                ltr['G' - 'A']--;
                ltr['H' - 'A']--;
                ltr['T' - 'A']--;
            }
        }
        if(ltr['X' - 'A'] != 0)
        {
            while(ltr['X' - 'A'])
            {
                digit.push_back(6);
                ltr['S' - 'A']--;
                ltr['I' - 'A']--;
                ltr['X' - 'A']--;
            }
        }
        if(ltr['H' - 'A'] != 0)
        {
            while(ltr['H' - 'A'])
            {
                digit.push_back(3);
                ltr['T' - 'A']--;
                ltr['H' - 'A']--;
                ltr['R' - 'A']--;
                ltr['E' - 'A']-=2;
            }
        }
        if(ltr['R' - 'A'] != 0)
        {
            while(ltr['R' - 'A'])
            {
                digit.push_back(4);
                ltr['F' - 'A']--;
                ltr['O' - 'A']--;
                ltr['U' - 'A']--;
                ltr['R' - 'A']--;
                //ltr['T' - 'A']--;
            }
        }
        if(ltr['F' - 'A'] != 0)
        {
            while(ltr['F' - 'A'])
            {
                digit.push_back(5);
                ltr['F' - 'A']--;
                ltr['I' - 'A']--;
                ltr['V' - 'A']--;
                ltr['E' - 'A']--;
               // ltr['T']--;
            }
        }
        if(ltr['V' - 'A'] != 0)
        {
            while(ltr['V' - 'A'])
            {
                digit.push_back(7);
                ltr['S' - 'A']--;
                ltr['E' - 'A']-=2;
                ltr['V' - 'A']--;
                ltr['N' - 'A']--;
                //ltr['T' - 'A']--;
            }
        }
        if(ltr['G' - 'A'] != 0)
        {
            while(ltr['G' - 'A'])
            {
                digit.push_back(8);
                ltr['E' - 'A']--;
                ltr['I' - 'A']--;
                ltr['G' - 'A']--;
                ltr['H' - 'A']--;
                ltr['T' - 'A']--;
            }
        }
        if(ltr['O' - 'A'] != 0)
        {
            while(ltr['O' - 'A'])
            {
                digit.push_back(1);
                ltr['O' - 'A']--;
                ltr['N' - 'A']--;
                ltr['E' - 'A']--;
            }
        }
        if(ltr['I' - 'A'] != 0)
        {
            while(ltr['I' - 'A'])
            {
                digit.push_back(9);
                ltr['N' - 'A']-=2;
                ltr['I' - 'A']--;
                ltr['E' - 'A']--;

            }
        }

        sort(digit.begin(), digit.end());

  		printf("Case #%d: ", i + 1);
  		for(int i = 0; i < digit.size(); i++)
        {
            cout<<digit[i];
        }
		cout << endl;
    }


    return 0;
}
