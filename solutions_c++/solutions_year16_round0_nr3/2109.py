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
#define lli unsigned long long int
lli checkPrime=200560490130; 
lli fast_expo(lli base, lli expo){
	lli res=1;
	while(expo>0){
		if(expo%2==1){
			res=(res*base);
		}
		base=(base*base);
		expo/=2;
	}
	return res;
}
lli genrate(lli numbers,lli base){
	lli value=0,it=1;
	while(numbers>0){
		value=value+(numbers%2)*fast_expo(base,it);
		numbers/=2;
		it++;
	}
	return value;
}
lli get_divisor(lli number){
	loop(i,2,number){
		if (number%i==0){
			return i;
		}
	}
}
void print_binary(lli number){
	vi(v);
	while(number>0){
		v.pb(number%2);
		number/=2;
	}
	pool(i,v.size()-1,0){
		cout<<v[i];
	}
	cout<<" ";
}
int main(){
	zyloc(){
		lli n,j;
		cin>>n>>j;
		cout<<"Case #1:"<<endl;
		lli min[11]={0},max[11]={0},counter_j=0,counter_n=0,upto;
		loop(i,2,10){
			min[i]=fast_expo(i,n-1)+1;
			max[i]=fast_expo(i,n)-1;
		}
		upto=fast_expo(2,n-2);
		while(counter_j<j){
			lli test_number[11]={0},flag=0,divisor[11]={0};
			loop(i,2,10){
				test_number[i]=min[i]+genrate(counter_n,i);
				if (__gcd(test_number[i],checkPrime)!=1){
					divisor[i]=get_divisor(test_number[i]);	
				}	
				else {
					flag=1;
					break;
				}
			}
			if (flag==0){
				print_binary(test_number[2]);
				loop(i,2,10){
					cout<<divisor[i]<<" ";
				}
				counter_j++;
				cout<<endl;
			}
			counter_n++;
		}
	}		
    return 0;
}	