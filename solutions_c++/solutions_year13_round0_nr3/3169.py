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

	bool ispal(int a){
		
		string s;

		while(a){
			
			s+='0'+a%10;
			a/=10;

		}
		int n=s.size();
		for(int i=0;i<n/2;i++)
			if(s[i]!=s[n-1-i])
				return false;
		return true;

	}
     
    int main(){
       freopen ("myfile.txt","w",stdout);freopen ("C-small-attempt0.in","r",stdin);
        int i,j,k;
		int n;
		char c,t='T';
		int  a,b;
		cin>>n;
		
		for(int q=1;q<=n;q++){
			k=0;
			cin>>a>>b;
			for(i=a;i<=b;i++){

				j=sqrt((double)i);
				if(j*j!=i)
					continue;

				if(ispal(i) && ispal(j))
					k++;

			}

			cout<<"Case #"<<q<<": "<<k<<endl;


		}

		


       //    system("PAUSE");
           return 0;
           }
