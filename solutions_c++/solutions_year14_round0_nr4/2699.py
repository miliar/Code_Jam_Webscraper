    #include <vector>
    #include <list>
    #include <map>
    #include <queue>
    #include <set>
    #include <deque>
    #include <stack>
    #include <bitset>
    #include <algorithm>
    #include <functional>
    #include <numeric>
    #include <utility>
    #include <sstream>
    #include <iostream>
    #include <iomanip>
    #include <cstdio>
    #include <math.h>
    #include <cstdlib>
    #include <ctime>
    #include <stdio.h>
    #include <stdlib.h>
	#include <string>
    using namespace std;
	
    int main(){
        freopen ("myfile.txt","w",stdout);
	 	freopen ("D-large.in","r",stdin);
		
		int n,i,j,k,m,z,rr;
		double c,f,x,d,e,rez;
		double a[1000],b[1000];
		
		cin>>k;

		for(m=0;m<k;m++){
			
			cin>>n;
			
			for(i=0;i<n;i++)
				cin>>a[i];
			z=0;
			for(i=0;i<n;i++){
				cin>>b[i];
				
			}

			sort(a,a+n);
			sort(b,b+n);
			
			

			i=j=0;

			while(i<n){
				
				if(a[i]>b[j]){
					
					i++;
					j++;
				}
				else{
				
					i++;
				
				}

			}
			rr=j;
			i=j=n-1;

			while(i>=0){
				
				if(a[i]>b[j]){
					
					i--;
					z++;
				}
				else{
				
					i--;
					j--;
				}

			}

			cout<<"Case #"<<m+1<<": "<<rr<<" "<<z<<endl;
			
			
			

		}
		
	//	system("PAUSE");
           return 0;
           }
