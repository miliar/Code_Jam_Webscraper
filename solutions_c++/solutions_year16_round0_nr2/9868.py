#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <cstdlib>
#include <stack>
using namespace std;
char ch[110] ;
stack<char> S;
void f(char ch[] , int Len){
	//cout << ch << " " << Len << endl;
	while(!S.empty()){
		S.pop() ;
	}
	//cout << ch << endl;
	for(int i = 0 ; i < Len ; ++i){ // ru zhan
		S.push(ch[i]) ;
	}
	char a ;
	for(int i = 0 ; i < Len ; ++i){ // fan zhuan
		a = S.top() ;
		S.pop() ;
		a == '+' ? ch[i] = '-' : ch[i] = '+' ;
	}
	//cout << ch << endl;
}
int main(){
	//freopen("B-large.in","r",stdin) ;
	//freopen("B-large.out","w",stdout);
	int t , cas = 1 ;
	cin >> t ;
	while(t--)	{
		memset(ch,0,sizeof(ch));
		cin >> ch ;
		int len = strlen(ch) , i = 1;
		int ans = 0 ;
		int pot = len-1;
		while(pot>=0&&ch[pot]=='+'){   // the first -  , 
			pot--;
		}  
		int l = 0 , r = pot ; //  r=='-'  
		while(r>=0 && ch[r]=='-'){
			l = 0 ;
			if(ch[0]=='+') {   	              // l == '+' 
				while(l<=r&&ch[l]=='+'){	 // the farthest '+' 
					ch[l++] = '-' ;
				}
				if(l<=r)		// have '-' ;
				ans++;				
			}						
			if(l > pot) break ;	// no '-' break ;
			int temp = l ;		// --- -++--
			while(temp<=r&&ch[temp]=='-')temp++;   
			temp--;			// the farthest '-' 
			f(ch,r+1) ;		// fan zhuan    --+  --- +--+++ , tmp '-' r-tmp ;    
			ans++;
			r = r-temp-1 ;		// +++----++    --+--+++- 
		}
		printf("Case #%d: ",cas++) ;
		cout << ans << endl;
	}
	//fclose(stdin) ;
	//fclose(stdout) ;
	return 0;
}

