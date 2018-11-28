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
    using namespace std;
		
	int a[100][100];
	bool b[100][100];
	int n,f;
	bool isrow(int i){
		
		int j,r=0;
		bool c=false;
		
		for(j=0;j<f;j++){
			if(!b[i][j]){
				c=true;
				r=a[i][j];
				break;

		}
		}

		if(!c)
			return false;

		for(j=0;j<f;j++)
			if(!b[i][j] && a[i][j]!=r)
				return false;
		return true;
		

	}


	bool iscol(int i){
		
		int j,r=0;
		bool c=false;
		
		for(j=0;j<n;j++){
			if(!b[j][i]){
				c=true;
				r=a[j][i];
				break;

		}
		}

		if(!c)
			return false;

		for(j=0;j<n;j++)
			if(!b[j][i] && a[j][i]!=r)
				return false;
		return true;
		

	}
	
    int main(){
       freopen ("myfile.txt","w",stdout);freopen ("B-large.in","r",stdin);
        int i,j,k,l,o,p;
		int m;
		cin>>m;
		bool d,e,s;
		
		

		for(int q=1;q<=m;q++){
			cin>>n>>f;
			for(i=0;i<n;i++)
				for(j=0;j<f;j++){
					cin>>a[i][j];
					b[i][j]=false;
				}
				
				

				
					s=false;
				for(i=0;i<n;i++)
					for(j=0;j<f;j++){
						p=a[i][j];
							d=true;e=true;
							for(k=0;k<f;k++)
								if(a[i][k]>p)
									e=false;

							for(k=0;k<n;k++)
								if(a[k][j]>p)
									d=false;

											
							if(e==false && d==false)
								s=true;


						}
			
				if(s)
			cout<<"Case #"<<q<<": NO"<<endl;
				else
					cout<<"Case #"<<q<<": YES"<<endl;


		}

		


       //    system("PAUSE");
           return 0;
           }
