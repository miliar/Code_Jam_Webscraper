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
	 	freopen ("B-large.in","r",stdin);
		
		int n,i,j,k,m,z;
		double c,f,x,d,e,rez;
		int a[4][4],b[4][4];
		
		cin>>n;

		for(m=0;m<n;m++){
			
			cin>>c>>f>>x;
			
			d=2.0;
			e=0;
			
			rez=x/2.0;
			
			while(1){
				
				e+=c/d;
				d+=f;
				
				if(rez>e+x/d)
					rez=e+x/d;
				else
					break;


			}

			
			cout<<"Case #"<<m+1<<": ";
			
			printf("%.7lf\n",rez);
			

		}
		
	//	system("PAUSE");
           return 0;
           }
