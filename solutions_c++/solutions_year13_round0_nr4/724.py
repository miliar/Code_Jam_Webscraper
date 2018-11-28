//File: main.cpp
//Autor: Vukasin Rankovic
#pragma comment(linker, "/STACK:268435456")

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <map>
#include <bitset>
#include <math.h>
#include <stdio.h>
#include <limits.h>
#include <stack>

using namespace std;

ifstream myin("D-small-attempt3.in");
ofstream myout("A-large.out");

typedef struct chest{
	int key;
	int keys[5000];
	int keysNb;
	bool visited;
}Chest;

Chest chests[200];
int keys[200];

int visitedList[200];
int point = 0;

bool dfs(int n,int lv){
	if(lv==n){
		for(int i=0 ; i<n ; i++)
		{
			myout << visitedList[i];
			if(i!=n-1) myout << " ";
		}
		return true;
	}
	int pomKey[200];
	int tempKey[200];
	for(int i=0 ; i<200 ; i++){
		pomKey[i] = 0;
		tempKey[i] = 0;
	}
	for(int i=0 ; i<n ; i++){
		if(chests[i].visited == false){
			pomKey[chests[i].key]++;
			for (int j = 0; j < chests[i].keysNb; j++)
			{
				pomKey[chests[i].keys[j]]--;
				tempKey[chests[i].keys[j]]++;
			}
		}
	}
	for(int i=0 ; i<n ; i++){
		if(chests[i].visited == false){
			if(keys[chests[i].key] == 0 && tempKey[chests[i].key]!=0){
				int cnt = 0;
				for (int j = 0; j < chests[i].keysNb; j++)
				{
					if(chests[i].keys[j]==chests[i].key){
						cnt++;
					}
				}
				if(cnt == tempKey[chests[i].key]){
					return false;
				}
			}
		}
	}
	for(int i=0 ; i<200 ; i++){
		if(keys[i] < pomKey[i]){
			return false;
		}
	}
	for (int i = 0; i < n; i++)
	{
		if(keys[chests[i].key]>0 && chests[i].visited == false){
			chests[i].visited = true;
			keys[chests[i].key]--;
			for (int j = 0; j < chests[i].keysNb ; j++)
			{
				keys[chests[i].keys[j]]++;
			}
			visitedList[point++] = i+1;
			if(dfs(n,lv+1))
			{
				return true;
			}
			chests[i].visited = false;
			keys[chests[i].key]++;
			for (int j = 0; j < chests[i].keysNb ; j++)
			{
				keys[chests[i].keys[j]]--;
			}
			point--;
		}
	}
	return false;
}

void main2(){
	int n,k;
	myin >> k >> n;
	int tmp;
	for(int i=0 ; i<200 ; i++){
		keys[i] = 0;
	}
	for(int i=0; i<k ; i++){
		myin >> tmp;
		keys[tmp-1]++;
	}
	for(int i=0 ; i<n ; i++){
		int ti,ki;
		myin >> ti >> ki;
		chests[i].key = ti-1;
		chests[i].keysNb = ki;
		chests[i].visited = false;
		for(int j=0 ; j< ki ; j++)
		{
			myin >> tmp;
			chests[i].keys[j] = tmp-1;
		}
	}
	if(!dfs(n,0)){
		myout << "IMPOSSIBLE";
	}
	point = 0;
}

//Multiple test cases
int main(){
	int t;
	myin >> t;
	for(int i=1 ; i<=t ; i++){
		myout << "Case #" << i << ": ";
		main2();
		myout << endl;
	}
}