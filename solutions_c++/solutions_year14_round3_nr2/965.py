#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std; 

#define ccMAX(a, b) ((a > b) ? a : b)
#define ccMIN(a, b) ((a < b) ? a : b)
#define LEN1 100

static vector<string*> trains;
static int num=0;
static	int c_map[256] = {0};

void swap(string*& a, string*& b)  
{  
    string* temp;  
    temp = a; a = b; b = temp;  
}

bool validtrain()
{
	memset(c_map, 0, sizeof(c_map));
	char oc = 0;
	char nc = 0;
	
	for (int i= 0; i < trains.size(); i++)
	{
		string& car = *(trains[i]);
		//cout << car;
		
#if 1
		for (int j = 0; j < car.length(); j++)
		{
			nc = car[j];
			if ((c_map[nc] > 0) && (nc != oc))
			{
				return false;
			}
			
			c_map[nc]++;
			oc = nc;
		}
#endif
	}
	
	//cout << endl;
	return true;
}

void recursion_Full_Array(int t)  
{  
    int i;  
    //output
    if (t >= trains.size() - 1)
    {  
  			if (validtrain())
  			{
  				num++;
  			}
        return;
    }  
    for (i = t;i < trains.size();i++)  
    {  
        swap(trains[i],trains[t]);  
        recursion_Full_Array(t+1);  
        swap(trains[i],trains[t]);  //»Ö¸´µ½½»»»Ç°×´Ì¬   
    }
}

int main (void)
{
	int t = 0;
	cin >> t;
	
	for (int ti = 1; ti < t+1; ti++)
	{
		num = 0;
		int N = 0;
		cin >> N;

		for(int i = 0; i < trains.size(); i++)
		{
			string * ptr = trains[i];
			if (NULL != ptr)
				delete ptr;
		}
		trains.clear();

		for (int ni=0; ni < N; ni++)
		{
			string* s= new string;
			cin >> *s;
			trains.push_back(s);
		}
		
		recursion_Full_Array(0);
		printf ("Case #%d: %d\n", ti, num);
	}  
	return 0;
}
