#include <algorithm>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int arr[4][4] = {{1,2,3,4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1}};
char str[10020], str1[10020];
int iarr[10010], karr[10010], ia, ka;

void revarr(int A[], int size)
{
	int temp;
	for (int i=0, j=size-1 ; i<j ; ++i, --j)
	{
		temp = A[i];
		A[i] = A[j];
		A[j] = temp;
	}
}

int get_num (char ch)
{
	if (ch == '1') return 1;
	return ch-'i'+2;
}

bool ispresent (int A[], int start, int end, int num)
{
	int mid;
	if (start>end) return false;
	if (start == end)
	{
		if (A[start] == num) return true;
		return false;
	}
	mid = (start+end)/2;
	if (A[mid] == num) return true;
	if (num < A[mid]) return ispresent (A, start, mid-1, num);
	return ispresent (A, mid+1, end, num);
}

int product (int num1, int num2)
{
	bool minus;
	if (num1 > 0 && num2 > 0) minus = false;
	else if (num1 < 0 && num2 < 0)
	{
		minus = false;
		num1 *= -1;
		num2 *= -1;
	}
	else
	{
		minus = true;
		if (num1<0) num1 *= -1;
		else num2 *= -1;
	}
	if (minus) return (-1*arr[num1-1][num2-1]);
	return arr[num1-1][num2-1];
}

bool gives_j_bf (int start, int end)
{
	int p2 = 1, i, j;
	for(i=start ; i<=end ; ++i)
	{
		p2 = product (p2, get_num(str[i]));
		//cout << p2 << " ";
	}
	//cout << " ::p2 = " << p2 << "\n";
	if (p2 == 3) return true;
	return false;
}

bool gives_j (int start, int end)
{
	//cout << "checking " << start << " to " << end << "\n";
	int p2 = 1, i, j, I=-1, J=-1;
	for(i=0 ; i<ia ; ++i)
		if (iarr[i]>start)
		{
			I = iarr[i];	
			break;
		}
	for(j=ia-1 ; j>=0 ; --j)
		if (iarr[j]<end)
		{
			J = iarr[j];
			break;
		}
	if (I<=J && I!=-1 && J!=-1)
	{
		for(i=start ; i<=I ; ++i)
			p2 = product (p2, get_num(str[i]));
		for(i=J+1 ; i<=end ; ++i)
			p2 = product (p2, get_num(str[i]));
		if (p2 == 3)
			return true;
		return false;
	}
	else return gives_j_bf(start, end);
	/*for(i=start ; i<end ; ++i)
	{
		p2 = product (p2, get_num(str[i]));
		if (p2 == 2)
		{
			cout <<"going";
			if(ispresent(iarr, 0, ka-1, i))
			{cout <<"came ";
			break;}
			else cout << "came ";
		}
	}
	//cout << "i="<<i<<"\n";
	if (i == end)
	{
		p2 = product (p2, get_num(str[i]));
		if (p2 == 3) { //cout << "++";
		 return true; }
		return false;
	}
	j=ia-1;
	while(iarr[j]>=end) --j;
	//cout << "-->" << iarr[j] << "\n";
	if (iarr[j]<end && iarr[j]>=i)
		i = iarr[j]+1;
	else i++;
	for(; i<=end ; ++i)
		p2 = product (p2, get_num(str[i]));
	if (p2 == 3)
	{ 
		//cout << "88";
		return true;
	}
	return false;*/
}

int main(int argc, char const *argv[])
{
	int iend, jend, kend, p1, p2, p3, a, b, c, t, L, X, T, pause, prev;
	bool done, ff;
	ifstream fin;
	ofstream fout;

	fin.open("input.txt");
	fout.open("output.txt");

	fin >> T;
	t = 0;
	while (++t <= T)
	{
		cout << "Case: " << t << "\n";
		iend = -1;
		p1 = 1; p2 = 1; p3 = 1;
		ia = 0; ka = 0;	// array size
		done = false;
		fin >> L >> X;
		fin >> str1;			// not using L, X
		str[0] = '\0';
		for (a=0 ; a<X ; ++a) strcat (str, str1);
		//cout << L << X << str << "\n";

		for (a=0 ; a<strlen(str) ; ++a)
		{
			p1 = product (p1, get_num(str[a]));
			if (p1 == 2) iarr[ia++] = a;
		}
		//for (a=0 ; a<ia ; ++a) cout << iarr[a] << " "; cout << "\n\n\n";

		for(c=strlen(str)-1 ; c>=0 ; --c)
		{
			p3 = product (get_num(str[c]), p3);
			if (p3 == 4) karr[ka++] = c;
		}
		revarr(karr, ka);
		//for (c=0 ; c<ka ; ++c) cout << karr[c] << " "; cout << "\n\n\n";

		prev = 0;
		for(a=0 ; a<ia && (!done) ; ++a)
		{
			for(c=prev ; c<ka && (!done) ; ++c)
				if(karr[c] - iarr[a] > 1)
				{
					prev = c;
					break;
				}
			for(c=prev ; c<ka && (!done) ; ++c)
			{
				if(karr[c] - iarr[a] > 1)
				{
					done = gives_j(iarr[a]+1, karr[c]-1);
					/*ff = gives_j_bf(iarr[a]+1, karr[c]-1);
					if (done != ff) 
					{
						cout <<" prob in " << iarr[a]+1 << " to " << karr[c]-1 << "\n";
						cout << done << " " << ff << "\n";
						cin >> pause; 
					}*/
				}
			}
		}

		if (done)
		{
			fout << "Case #" << t << ": YES" << "\n";
			cout << "Case #" << t << ": YES" << "\n";
		}
		else
		{
			fout << "Case #" << t << ": NO" << "\n";
			cout << "Case #" << t << ": NO" << "\n";
		}
	}
	
	return 0;
}