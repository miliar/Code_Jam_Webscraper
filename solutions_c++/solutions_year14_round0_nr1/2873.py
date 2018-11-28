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
	 	freopen ("A-small-attempt0.in","r",stdin);
		
		int n,i,j,k,m,z,c,rez=0;
		int a[4][4],b[4][4];
		
		cin>>n;

		for(m=0;m<n;m++){
			
			cin>>k;
			for(i=0;i<4;i++)
				for(j=0;j<4;j++)
					cin>>a[i][j];
			cin>>c;
			for(i=0;i<4;i++)
				for(j=0;j<4;j++)
					cin>>b[i][j];

			z=0;
			k--;c--;
			for(i=0;i<4;i++)
				for(j=0;j<4;j++)
					if(a[k][i]==b[c][j]){
						z++;
						rez=a[k][i];
					//	cout<<rez<<endl;
					}
					cout<<"Case #"<<m+1<<": ";
			
			if(z==0)
				cout<<"Volunteer cheated!"<<endl;

			if(z==1)
				cout<<rez<<endl;
			if(z>1)
				cout<<"Bad magician!"<<endl;
			

		}
		
	//	system("PAUSE");
           return 0;
           }
