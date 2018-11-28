#include <algorithm>
#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>

using namespace std;

void sort1 (int* tmp, int length ) {
	int i,j;
	int index,buffer;
	for ( i = 0; i < length; i++ ){
		index=i;
		for ( j = i; j < length; j++ ){
			if ( tmp[index] >= tmp[j] ) {
				index=j;
				// printf("index = %d\n",index);
			}
		}
		buffer=tmp[i];
		tmp[i]=tmp[index];
		tmp[index]=buffer;
	}
}

bool make_mote ( int a, int* b, int* c, int remaining) {
	int add_counter=0;
	int buffer=*b;
	while (buffer <= a) {
		add_counter++;
		buffer += buffer-1;
		// cout << "buffer=" << buffer << " add_counter=" << add_counter << endl;
	}
	// cout << "remaining=" << remaining << " add_counter=" << add_counter << endl;
	if (remaining > add_counter) {
		*b=buffer;
		*c+=add_counter;
		return true;
	}
	else {
		*c+=remaining;
		return false;
	}
}

void main( int argc, char** argv) {
	int T,Trun = 1;
	int i,j;
	int A,N,counter,total;
	cin >> T;
	while ( Trun <= T ) {
		cin >> A >> N;
		total = A;
		counter = 0;
		int* d = new int[N];
		for ( i = 0; i < N; i++ )
			cin >> d[i];
		sort1 (d,N);
		// for ( i = 0; i < N; i++ )
		// 	cout << d[i] << " ";
		// cout << endl;
		if (total == 1) 
			counter = N;
		else
			for ( i = 0; i < N; i++ ) {
				// cout << total << " > " << d[i] << endl;
				if ( total <= d[i] ) {
					// cout << "d[i]=" <<d[i] << " total=" << total << " counter=" << counter << " reminaing=" << N-i << endl;
					if ( !make_mote(d[i],&total,&counter,N-i) ) {
						// cout << "out" << endl;
						break;
					}
				}
				total += d[i];
			}
		delete[] d;
		cout << "Case #" << Trun++ << ": " << counter << endl;
	}
}

