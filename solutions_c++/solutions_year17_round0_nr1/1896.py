#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <functional>
#include <set>
#include <sstream>
#include <map>
#include <queue>
#include <stack>

using namespace std;

int main()
{
		
    int T;
    cin>>T;
	
    for(int t=1;t<=T;t++){
		string s;
		int k;
		cin>>s>>k;

		int n=s.size();

		int res=0;
		for(int i=0;i<=n-k;i++){
			if(s[i]=='-'){
				res++;
				for(int j=0;j<k;j++){
					if(s[i+j]=='-') s[i+j]='+';
					else s[i+j]='-'; 
				}
			}
		}

		bool ok=true;
		for(int i=n-k+1;i<n;i++) if(s[i]!='+') ok=false;

		if(!ok) printf("Case #%d: IMPOSSIBLE\n",t);
		else printf("Case #%d: %d\n",t,res);

    }
    
    return 0;
}