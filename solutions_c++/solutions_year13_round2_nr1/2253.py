#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>
#include <map>
#include <iostream>

using namespace std;
int motes[100];

int main(){
    int cases,total;
    int armin,n,aux,tmp;
    scanf("%d",&cases);
    for ( int i=1 ; i <= cases ; i++ ) {
    	total = 0;
        scanf("%d %d",&armin,&n);
        for ( int j = 0; j < n; j++ ) {
        	scanf("%d",&motes[j]);
        }
        sort(motes,motes+n);
        for ( int z = 0; z < n; z++ ) {
        	if ( armin > motes[z] ) {
        		armin += motes[z];
        	} else if ( armin == motes[z] ) {
        		if ( motes[z] == 1 ) {
        			total++;
        		} else {
        			armin += (armin-1)+motes[z];
        			total++;
        		}
        	} else {
        		if ( z == n-1 ) {
        			total++;
        		} else {
        			if ( armin == 1 ) {
        				total++;
        			} else {
        				tmp = armin;
        				aux = 0;
        				while ( tmp <= motes[z] ) {
        					tmp += (tmp-1);
        					aux++;
        				}
        				if ( aux < n ) {
        					armin = tmp;
        					armin += motes[z];
        					total += aux;
        				} else {
        					total++;
        				}
        			}
        		}
        	}
        }
        printf("Case #%d: %d\n",i,total);
    }   
}

