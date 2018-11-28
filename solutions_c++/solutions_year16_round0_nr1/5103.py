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
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int tt;
    scanf("%d", &tt);
    for (int qq=1;qq<=tt;qq++) {
        printf("Case #%d: ", qq);
        bool num[10];
        string digits="";
        string ns;
        int multi=0;
        unsigned long long int n;
        cin>>n;
        if(n==0) 
        	cout<<"INSOMNIA\n";
	else
	{
		for (int i = 0; i <= 9; i++) num[i] = true;
        	while(digits.length()!=10){
		    multi++;
		    ns=to_string(n*multi);
		    for(char i:ns){
		        if(digits.find(i)==string::npos)
		            digits=digits+i;
		    }
		}
		cout<<ns<<endl;	
	}        

    }
    return 0;
}
