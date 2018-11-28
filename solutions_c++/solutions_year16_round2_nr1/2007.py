#include <iostream>
#include <fstream>
#include <cstdlib>
#include<string>
#include<vector>
#include<cmath>
#include <sstream>
#include <bitset>

using namespace std;

#define lp(i,n) for(i=0; i<n ; i++)
#define lp1(i,n) for(i=0; i<n ; i++)
#define lpI(i,a,b) for(i = a; )

#define lp(i,n) for (i=0; i<n; i++)
#define lp1(i,n) for (i=1; i<=n; i++)
#define lpi(i,a,b) for (i=a; i<=b; i++)
#define lpr(i,n) for (i=(n)-1; i>=0; i--)
#define lpr1(i,n) for (i=n; i>0; i--)
#define lpri(i,a,b) for (i=b; i>=a; i--)
#define lop(i, n)  for(int i=0; i<n ; i++)
#define lop1(i, n)  for(int i=1; i<n ; i++)
#define Min(a,b) a=min(a,b)
#define Max(a,b) a=max(a,b)
#define ull unsigned long long 

const int MAXNUM = 10000000; 

ull temp;

string word;

int track[10000];

int num[10000];

int tnum;

void s(int arr[], int size) {
	bool not_sorted = true;
	int j = 1, tmp;

	while (not_sorted) {
		not_sorted = false;
		j++;
		for (int i = 0; i < size - j; i++) {
			if (arr[i] > arr[i + 1]) {
				tmp = arr[i];
				arr[i] = arr[i + 1];
				arr[i + 1] = tmp;
				not_sorted = true;

			}//end of if

		}//end of for loop
	}//end of while loop
}//end of bubble_sort

void bubbleSort(int arr[], int n) {
	bool swapped = true;
	int j = 0;
	int tmp;
	while (swapped) {
		swapped = false;
		j++;
		for (int i = 0; i < n - j; i++) {
			if (arr[i] > arr[i + 1]) {
				tmp = arr[i];
				arr[i] = arr[i + 1];
				arr[i + 1] = tmp;
				swapped = true;
			}
		}
	}
}

void docase()
{
	
	tnum = 0;
	cin >> word;
	lop(a, 27)
	{
		track[a + 65] = 0;
	}
	lop(a, word.length())
	{
		track[(int)word[a]]++;
	}

	lop(a, word.length())
	{
		if (word[a] == 'Z')
		{
			track[(int)'Z']--;
			track[(int)'E']--;
			track[(int)'R']--;
			track[(int)'O']--;
			num[tnum] = 0;
			tnum++;
		}
		else if (word[a] == 'W')
		{
			track[(int)'O']--;
			track[(int)'T']--;
			track[(int)'W']--;
			num[tnum] = 2;
			tnum++;
		}

		else if (word[a] == 'U')
		{
			track[(int)'F']--;
			track[(int)'O']--;
			track[(int)'U']--;
			track[(int)'R']--;
			num[tnum] = 4;
			tnum++;
		}

		else if (word[a] == 'X')
		{
			track[(int)'S']--;
			track[(int)'I']--;
			track[(int)'X']--;
			num[tnum] = 6;
			tnum++;
		}
		else if (word[a] == 'G')
		{
			track[(int)'E']--;
			track[(int)'I']--;
			track[(int)'G']--;
			track[(int)'H']--;
			track[(int)'T']--;
			num[tnum] = 8;
			tnum++;
		}

	}
	
		lop(k, track[(int)'O'])
		{
			num[tnum] = 1;
			tnum++;
		}
		lop(k, track[(int)'F'])
		{
			track[(int)'I']--;
			num[tnum] = 5;
			tnum++;
		}
		lop(k, track[(int)'S'])
		{
			num[tnum] = 7;
			tnum++;
		}
		lop(k, track[(int)'I'])
		{
			num[tnum] = 9;
			tnum++;
		}
		lop(k, track[(int)'H'])
		{
			num[tnum] = 3;
			tnum++;
		}


	
}




int main()
{
	void s(int arr[], int size);
	int cases = 0;
	freopen("a.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> cases;
	

	for (int i = 0; i < cases; i++)
	{
				
		cout << "Case #" << i + 1 << ": ";
		docase();

		bubbleSort(num, tnum);

		lop(r, tnum)
		{
			cout << num[r];
		}
		cout << endl;
	


	}

	



	return 0;
}
