/*
 * A.cxx
 * 
 * Copyright 2013 aras <aras@aras-Satellite-C645D>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char **argv)
{
	long long T,a,b,X,Y,test = 1,answer[] = { 0 , 1 , 4 , 9 , 121 , 484 , 10201 , 12321 , 14641 , 
	                   40804 , 44944 , 1002001 , 1234321 , 4008004 , 
	                   100020001 , 102030201 , 104060401 , 121242121 , 
	                   123454321 , 125686521 , 400080004 , 404090404 , 
	                   10000200001 , 10221412201 , 12102420121 , 
	                   12345654321 , 40000800004 , 1000002000001 , 
	                   1002003002001 , 1004006004001 , 1020304030201 , 
	                   1022325232201 , 1024348434201 , 1210024200121 , 
	                   1212225222121 , 1214428244121 , 1232346432321 , 
	                   1234567654321 , 4000008000004 , 4004009004004 , 999999999999999};

	ifstream IN("C-large-1.in");
	ofstream OUT("Fair and Square.out");
	IN >> T;
	
	while(T--)
	{
		IN >> a >> b;		

		X = Y = 0;
		
		for(long long i = 0;i < 41;i++)
			if(answer[i] >= a)
			{
				X = i;
				break;
			}
			
		for(long long i = 40;i >= 0;i--)
			if(answer[i] <= b)
			{
				Y = i;
				break;
			}

		cout << "Case #" << test << ": " << Y-X+1 << endl;
		OUT << "Case #" << test++ << ": " << Y-X+1 << endl;
	}
	
	return 0;
}

/*
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

bool Fair(long long x)
{
	string str = "";
	do str += ('0' + x%10) , x/= 10; while(x);
	
	string str2 = str;
	reverse(str.begin() , str.end());
	
	return str == str2;
}

int main(int argc, char **argv)
{	
	for(long long i = 1;i <= 10000000;i++)
		if(Fair(i) && Fair(i*i))
			cout << i*i << " , ";
	return 0;
}
*/

