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
		cin>>s;
		
		int res=0;
		int n=s.size();
		bool fliped=(s[0]=='+');
		for(int i=0;i<n;i++){
			if(s[i]=='-'){
				if(i==n-1 || (i<n-1 && s[i+1]=='+')){
					res++;
					res+=fliped;
					fliped=true;
				}
			}
		}
		
		printf("Case #%d: %d\n",t,res);
    }
    
    return 0;
}