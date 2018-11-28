#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <string>
#include <list>
#include <queue>
#include <cassert>
#include <stack>
#include <fstream>
#include <cstring>

using namespace std;

#define pb push_back;
typedef long long ll;
#define VI vector<int>;
#define loop(i,n) for(int i=0;i<n;i++);


int main(){
    int t,case_num=1,count=0,d,flag=1;
    ll n,ans,num;  
    ifstream input;
    input.open("input.txt");
    ofstream outfile;
    outfile.open("output.txt");
    input>>t;
    while(t--){
        flag=1;
        count=0;
        bool arr[10]={false};
    	input>>n;
    	if(n==0)
    		outfile<<"Case #"<<case_num<<": INSOMNIA"<<endl;
    	else{
    		for(int i=1;flag;i++){
    			num=n*i;
    			while(num){
    				d=abs(num%10);
    				if(arr[d]==false){
    					arr[d]=true;
    					count++;
    					if(count==10){
    						outfile<<"Case #"<<case_num<<": "<<n*i<<endl;
                            flag=0;
                            break;
    					}
    				}
    				num/=10;
    			}
    		}
    	}
        case_num++;
    }
    return 0;
}
