#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
#include<stdio.h>
#include"string.h"
#include <map>
#include <iomanip>
#include <cmath>
#include <sstream>
#include<deque>
#include<stack>
#include <list>
#include<cstring>

using namespace std;

#define MAX 100000
struct node
{
  long long summa, add;
} t[4*MAX];

void Push(int v, int LeftPos, int Middle, int RightPos)
{
  if (t[v].add)
  {
    t[2*v].add += t[v].add;
    t[2*v].summa += (Middle - LeftPos + 1) * t[v].add;
    t[2*v+1].add += t[v].add;
    t[2*v+1].summa += (RightPos - Middle) * t[v].add;
    t[v].add = 0;
  }
}

void AddValue(int v, int LeftPos, int RightPos, int L, int R, int Value)
{
  if (L > R) return;

  if ((LeftPos == L) && (RightPos == R))
  {
    t[v].add += Value;
    t[v].summa += (R - L + 1) * Value;
    return;
  }

  int Middle = (LeftPos + RightPos) / 2;


  Push(v,LeftPos,Middle,RightPos);

  AddValue(2*v, LeftPos, Middle, L, min(Middle,R), Value);
  AddValue(2*v+1, Middle+1, RightPos, max(L,Middle+1), R, Value);
  
  t[v].summa = t[2*v].summa + t[2*v+1].summa;
}

long long Summa(int v, int LeftPos, int RightPos, int L, int R)
{
  if (L > R) return 0;

  if ((LeftPos == L) && (RightPos == R)) return t[v].summa;

  int Middle = (LeftPos + RightPos) / 2;

  Push(v,LeftPos,Middle,RightPos);

  return Summa(2*v, LeftPos, Middle, L, min(Middle,R)) + 
         Summa(2*v+1, Middle+1, RightPos, max(L,Middle+1), R); 
}


int mas[11];

int main()
{
	ifstream f("c://A-large.in");
	ofstream o("c://ASmall.OUT");
    int t,n;

	f >>t;

	for(int i=1; i<=t; i++)
	{
		set<int> s;
		f >> n;
		if(n==0) 
		{
			cout << "Case #" << i << ": INSOMNIA" <<endl; 
			o << "Case #" << i << ": INSOMNIA" <<endl;
			continue;
		}


		int d = n;

		while(d)
		{
			s.insert(d%10);
			d/=10;
		}

		if(s.size() == 10)
		{
			cout << "Case #" << i << ": " << n<<endl; 
			o << "Case #" << i << ": " << n<<endl;  
			break;
		}


		int j = 1; 
		int te = n;
		while(true)
		{
			te = n*j;
			int p = te;
			
			
			while(p)
			{
				s.insert(p%10);
				p/=10;
			}
			if(s.size() == 10)
			{
				cout << "Case #" << i << ": " << te<<endl; 
				o << "Case #" << i << ": " << te<<endl;
				break;
			}
			j++;
			
			

		}
	}
	return 0;
}