#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <set>

using namespace std;


ifstream fin("large.in");
ofstream fout("large.out");

int compareFunc (const void * a, const void * b)
{
	return ( (*(int*)a) - (*(int*)b) );
}

int main(){
	int nt;
	fin >> nt;
	for(int t=0;t<nt;t++){
		int n,x;
		int sizes[10000];
		fin >> n >> x;
		for(int i=0;i<n;i++){
			fin >> sizes[i];
		}
		qsort(sizes,n,sizeof(int),compareFunc);//assuming big at end
		int i, j, count;
		count = 0;
		i = 0;
		j = n-1;
		while(j >= i){
			if(i==j){
				count++;
				i++;
			}
			else{
				if(sizes[i]+sizes[j] <= x){
					i++;
					j--;
					count++;
				}
				else{
					j--;
					count++;
				}
			}
		}
		fout << "Case #" << t+1 << ": " << count  << endl;
	}
	return 0;
}