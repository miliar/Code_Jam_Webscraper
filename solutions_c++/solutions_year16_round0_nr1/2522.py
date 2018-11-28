/*
 * Satyam Swarnkar (Zyloc), Nit Silchar
*/
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <stack>
#include <iomanip>
#include <functional>
#include <limits.h>  
using namespace std;
#define loop(i,start,end) for (int i=start;i<=end;i++)
#define pool(i,start,end) for(int i=start;i>=end;i--)
#define zyloc() lli t;cin>>t;while(t--)
#define vi(v) vector <long long  int> v;
#define pb(n) push_back(n)
#define mp(a,b) make_pair(a,b)
#define fill(a,value) memset(a,value,sizeof(a)) 
#define MOD 1000000007
#define PI  3.14159265358979323846
#define MAX 1000002
#define vpi(v) vector <pair <long long int, long long int> > v
#define lli long long int 

int main(){
	lli counter=0;
	zyloc(){
		counter++;
		lli n,temp;
		cin>>n;
		if (n==0){
			cout<<"Case #"<<counter<<": INSOMNIA"<<endl;
		}
		else {
			set<lli> st;
			lli i=1,temp2=0;
			while(true){
				temp=n*i;
				temp2=temp;
				while(temp>0){
					st.insert(temp%10);
					temp/=10;
				}
				if (st.size()==10){
					cout<<"Case #"<<counter<<": "<<temp2<<endl;
					break;		
				}
				i++;
			}
			
		}
	}		
    return 0;
}	