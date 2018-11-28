#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
int main(){
    int t,n,i,cnd,cn,j,cnd1,c,k;
    double na[1010], ke[1010];
    cin>>t;
    for(int q = 1; q <= t; q++){
        cin>>n;
        cn = 0;
        cnd = 0;
        for(j = 0; j < n; j++)
            cin>>na[j];
        for(j = 0; j < n; j++)
            cin>>ke[j];
        stable_sort(na, na + n);
        stable_sort(ke, ke + n);
        i = 0;
        j = 0;
        k=0;
        c = cnd = cnd1 = 0;
        while (c < n){
        	c++;
        	if(ke[n - 1 - i] < na[n - 1 -j] && (n - 1 - i >= 0) && (n - 1 -j >= 0)){
        		i++;
        		j++;
        	}
        	else if(na[k] < ke[n - 1 - i] && k <n && (n -1 -i) >= 0){
        		k++;
        		i++;
        	}
        	else
        		cnd1++;
        }    
        cnd = j + cnd1;
        for(i = 0; i < n; i++){
            j = i;
            while(na[i] > ke[j] && j < n)
                j++;
            if(j != n){
                ke[j] = 0;
            }
            else
                cn++;
        }
        printf("Case #%d: ",q);
        printf("%d %d\n",cnd,cn);
    }
}
