#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define MAX 55
using namespace std;
int t,p,n,i,k,j,ans1,ans2,c;
double a[1005],b[1005],e[1005],d[1005];
int main(){
    ifstream fin;
    ofstream fout;
    fout.open("DeceitfulWaroutputLarge.txt");
    fin.open("inp.txt");
    fin>>t;
    p=1;
    while(t--){
    	ans1=0;
    	ans2=0;
    	fin>>n;
    	c=n;
    	for(i=0;i<n;i++){
    		fin>>a[i];
    	}
    	sort(a,a+n);
    	for(i=0;i<n;i++){
    		e[i]=a[i];
    	}
    	for(i=0;i<n;i++){
    		fin>>b[i];
    	}
    	sort(b,b+n);
    	for(i=0;i<n;i++){
    		d[i]=b[i];
    	}
    	for(i=0;i<n;i++){
    		for(j=0;j<n;j++){
			  if(a[i]<b[j]){
    		     ans2++;
    		     b[j]=0;
    		     break;
    		  }	
    		}
    	}
    	i=0;
        j=0;
        k=n-1;
        while(i!=n){
        	if(e[i]>d[j]){
        		ans1++;
        		i++;
        		j++;
        	}
        	else{
			   if(e[i]>d[k]) ans1++;	
        	   i++;
        	   k--;
        	}
        }
    	fout<<"Case #"<<p<<": "<<ans1<<" "<<c-ans2<<endl;
    	p++;
    }
    fout.close();
    return 0;
}
