#pragma once

#define _CRT_SECURE_NO_DEPRECATE
#include "targetver.h"

#include <windows.h>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <tchar.h>
#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

using namespace std;

FILE * in, * out;

#define fo(a,b,c) for(int a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )

int ri() { int a; fscanf(in, "%d", &a ); return a; }
double rf() { double a; fscanf(in, "%lf", &a ); return a; }
char sbuf[100005]; 
string rstr() 
{
	//fscanf(in, "%lf", sbuf); 
	char c;
	char * b = sbuf;
	while(c = fgetc(in))
	{
		if(c == '\n' || c == 255) break;
		*b++=c;
	}
	*b = 0;
	return sbuf; 
}
long long rll() { long long a; fscanf(in, "%lld", &a ); return a; }

struct sunduk
{
	int			keytype;
	int			iteration;
	vector<int> keys;
};

bool findCycle(map<int,set<int>> & ways, int start, int end, bool * used, vector<int> & path)
{
	set<int>::iterator ptr = ways[start].begin();
	set<int>::iterator last = ways[start].end();
	used[start] = true;
	path.push_back(start);
	while(ptr != last)
	{
		if(*ptr == end)
		{
			path.push_back(end);
			return true;
		}
		if(!used[*ptr] && findCycle(ways,*ptr,end,used,path)) return true;
		ptr ++;
	}
	path.pop_back();
	used[start] = false;
	return false;
}

void openPath(sunduk * sunduks, int num, map<int, int> & keys, int & iteration, vector<int> & path, int ind)
{
	for(int i = 0; i<num; i++)
	{
		if(sunduks[i].iteration > iteration) continue; // opened
		if(sunduks[i].keytype == path[ind]) 
		{
			fj(sunduks[i].keys.size())
				if(sunduks[i].keys[j] == path[ind+1])
				{
					keys[sunduks[i].keytype] --;
					fk(sunduks[i].keys.size())
						keys[sunduks[i].keys[k]]++;
					sunduks[i].iteration = iteration;
					if(ind < path.size()-2)
						openPath(sunduks,num,keys,iteration,path,ind+1);
					return;
				}
		}
	}
}
bool isPosible(sunduk * sunduks, int num, map<int, int> & keys, int & iteration)
{
	map<int, int>::iterator ptr = keys.begin();

	while(ptr != keys.end())
	{
		if(ptr->second == 0)
		{
			ptr++;
			continue;
		}
		
		int count = 0;
		for(int i = 0; i<num; i++)
		{
			if(sunduks[i].iteration > iteration) continue; // opened
			if(sunduks[i].keytype == ptr->first) count ++;
		}
		
		if(count == 0 || count >= ptr->second)
		{
			ptr++;
			continue;
		}

		for(int i = 0; i<num; i++)
		{
			if(sunduks[i].iteration > iteration) continue; // opened

			if(sunduks[i].keytype == ptr->first) // open it
			{
				keys[sunduks[i].keytype] --;
				fj(sunduks[i].keys.size())
					keys[sunduks[i].keys[j]]++;
				sunduks[i].iteration = iteration+1;
			}
		}
		ptr++;
	}

	ptr = keys.begin();
	while(ptr != keys.end())
	{
		if(ptr->second == 0)
		{
			ptr++;
			continue;
		}
		int count = 0;
		for(int i = 0; i<num; i++)
		{
			if(sunduks[i].iteration > iteration) continue; // opened
			if(sunduks[i].keytype == ptr->first) count ++;
		}
		if(count == 0)
		{
			ptr++;
			continue;
		}

		if(count <= ptr->second) 
		{
			for(int i = 0; i<num; i++)
			{
				if(sunduks[i].iteration > iteration) continue; // opened

				if(sunduks[i].keytype == ptr->first) // open it
				{
					keys[sunduks[i].keytype] --;
					fj(sunduks[i].keys.size())
						keys[sunduks[i].keys[j]]++;
					sunduks[i].iteration = iteration;
				}
			}
			keys.erase(ptr->first);
			iteration--;
			return isPosible(sunduks,num,keys,iteration);
		}
		
		map<int,set<int>> cycles;
		for(int i = 0; i<num; i++)
		{
			if(sunduks[i].iteration > iteration) continue; // opened
			fj(sunduks[i].keys.size())
				cycles[sunduks[i].keytype].insert(sunduks[i].keys[j]);
		}
		bool used[201];
		fj(201) used[j] = false;
		vector<int> path;
		
		if(!findCycle(cycles,ptr->first,ptr->first,used,path)) 
		{
			ptr ++;
			continue;
		}

		openPath(sunduks,num,keys,iteration,path,0);
		iteration --;
		return isPosible(sunduks,num,keys,iteration);
	}

	for(int i = 0; i<num; i++)
		if(sunduks[i].iteration <= iteration) return false; // still unopened
	return true;
}


sunduk sunduks[201];

long _tmain(int argc, _TCHAR* argv[])
{
	in	= fopen("D-small-attempt1 (1).in","rt");
	out	= fopen("small_out.txt","wt");

	int T = ri(); 
	for(int i = 0; i<T; i++)
	{
		int nkeys	= ri(); 
		int chests	= ri(); 

		map<int, int> keys;
		fj(nkeys) keys[ri()] ++;

		fj(chests) 
		{
			sunduks[j].keytype = ri();
			sunduks[j].iteration = 0;
			nkeys = ri();
			sunduks[j].keys.resize(nkeys);
			fk(nkeys) sunduks[j].keys[k] = ri();
		}

		//fj( (numbers.size()) ) if(numbers[j] >= f && numbers[j] <= l) sum ++;
		fprintf(out, "Case #%d:",i+1);
		printf("Case #%d:",i+1);
		
		map<int, int> save = keys;
		int iteration = 0xFFFFFF0;
		if(!isPosible(sunduks, chests, keys, iteration))
		{
			fprintf(out, " IMPOSSIBLE\n");
			printf(" IMPOSSIBLE\n");
		}
		else
		{
			int num = chests;
			while(num > 0)
			{
				fj(chests)
				{
					if(sunduks[j].iteration == 0xFFFFFFF) continue;
					if(save[sunduks[j].keytype] == 0) continue;
					keys = save;
					fk(sunduks[j].keys.size())
						keys[sunduks[j].keys[k]]++;
					keys[sunduks[j].keytype] -- ;

					sunduks[j].iteration = 0xFFFFFFF;
					iteration = 0xFFFFFF0;
					map<int, int> save2 = keys;
					fk(chests)
						if(sunduks[k].iteration < 0xFFFFFFF)
							sunduks[k].iteration = 0;

					if(isPosible(sunduks, chests, keys, iteration))
					{
						save = save2;
						fprintf(out, " %d",j+1);
						printf(" %d",j+1);
						num--;
						break;
					}
					else
						sunduks[j].iteration = 0;
				}
			}
			fprintf(out, "\n");
			printf("\n");
		}
	}

	fclose(in);
	fclose(out);
	return 0;
}

