#include <vector>
#include <list>
#include <map>
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
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

int main() {
    int tt;
    scanf("%d", &tt);
    for (int qq=1;qq<=tt;qq++) {
        printf("Case #%d: ", qq);
        string s,c1,c2;
	string rr="";
	int res;
        cin>>s;
        if(s.length()==1) 
        	cout<<s<<endl;
	else
	{
		for(char i:s){
		       	c1=rr+i;
			c2=i+rr;
			res=c1.compare(c2);
			if(res>0)
				rr=c1;
			else
				rr=c2;
		    }
		cout<<rr<<endl;	
	}        

    }
    return 0;
}
