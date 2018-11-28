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
#include <iterator>

using namespace std;

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int tt;
    scanf("%d", &tt);
    for (int qq=1;qq<=tt;qq++) {
    	printf("Case #%d: ", qq);
    	string str;
    	cin>>str;
    	string::iterator it =unique(str.begin(),str.end());
    	str.resize( distance(str.begin(),it) );
    	int len=str.length();
    	if(str=="-")
    		cout<<1<<endl;
    	else if(str=="+")
    		cout<<0<<endl;	
    	else if(str[0]=='-'&&(len%2==0))
    		cout<<(len-1)<<endl;
    	else if(str[0]=='-'&&(len%2!=0))
    		cout<<(len)<<endl;

    	else if(str[0]=='+'&&(len%2==0))
    		cout<<(len)<<endl;
    	else
    		cout<<(len-1)<<endl;
    }  
    return 0;
}
