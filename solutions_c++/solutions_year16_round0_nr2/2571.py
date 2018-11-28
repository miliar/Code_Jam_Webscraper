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
	lli ans_counter=0;
	zyloc(){
		ans_counter++;
		string s;
		cin>>s;
		lli right_pointer,flag=0,counter=0;
		pool(i,s.length()-1,0){
			if (s[i]=='-'){
				right_pointer=i;
				flag=1;
				break;
			}
		}
		if (flag==0){
			right_pointer=0;
		}
		while(right_pointer!=0 or (right_pointer==0 and s[0]=='-')){
			flag=0;
			pool(i,right_pointer,0){
				if (s[i]=='-'){
					right_pointer=i;
					flag=1;
					break;
				}
			}
			if (flag==0){
				right_pointer=0;
				break;
			}
			if (s[0]=='+'){
				loop(i,0,right_pointer){
					if (s[i]=='+'){
						s[i]='-';
					}
					else{
						break;
					}
				}
				counter++;
			}
			counter++;
			loop(i,0,right_pointer/2){
				if (s[i]=='-'){
					if (s[right_pointer-i]=='-'){
						s[i]='+';
					}
					else{
						s[i]='-';
					}
					s[right_pointer-i]='+';
				}
				else{
					if (s[right_pointer-i]=='-'){
						s[i]='+';
					}
					else{
						s[i]='-';
					}
					s[right_pointer-i]='-';
				}
			}
		}
		cout<<"Case #"<<ans_counter<<": "<<counter<<endl;	
	}	
    return 0;
}	