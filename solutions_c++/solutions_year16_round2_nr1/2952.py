/*   ARSHEYA RAJ   */

#include <iostream>
#include <bits/c++io.h>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <string.h>
#include <algorithm>
#include <iomanip>
#include <exception>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <iterator>
 
#define ll long long int
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) a>b?b:a
#define FOR(i,n) for(int i=0;i<n;i++)
#define FOR_X(i,x,n) for(i=x;i<n;i++)
#define BACK(i,n) for(i=n;i>=0;i--)
#define BACK_X(i,n,x) for(i=n;i>=x;i--)
#define fill(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define pp pair<int,int>
#define mod 1000000007

using namespace std;

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t=100,c0=0,c1=0,c2=0,c3=0,c4=0,c5=0,c6=0,c7=0,c8=0,c9=0,testcounter=1,i,j,n;
	string s;
	scanf("%d",&t);
	while(t--){
		cin>>s;
		n=s.size();
		for(i=0;i<n;i++){
			if(s.at(i)=='Z'){
				c0++;
			}
			if(s.at(i)=='W'){
				c2++;
			}
			if(s.at(i)=='U'){
				c4++;
			}
			if(s.at(i)=='X'){
				c6++;
			}
			if(s.at(i)=='G'){
				c8++;
			}
		}
		for(i=1;i<=c0;i++){
			for(j=0;j<n;j++){
				if(s.at(j)=='Z'){
					s.at(j)=' ';
					break;
				}
			}
			for(j=0;j<n;j++){
				if(s.at(j)=='E'){
					s.at(j)=' ';
					break;
				}
			}
			for(j=0;j<n;j++){
				if(s.at(j)=='R'){
					s.at(j)=' ';
					break;
				}
			}
			for(j=0;j<n;j++){
				if(s.at(j)=='O'){
					s.at(j)=' ';
					break;
				}
			}
		}
		for(i=1;i<=c2;i++){
			for(j=0;j<n;j++){
				if(s.at(j)=='T'){
					s.at(j)=' ';
					break;
				}
			}
			for(j=0;j<n;j++){
				if(s.at(j)=='W'){
					s.at(j)=' ';
					break;
				}
			}
			for(j=0;j<n;j++){
				if(s.at(j)=='O'){
					s.at(j)=' ';
					break;
				}
			}
		}
		for(i=1;i<=c4;i++){
			for(j=0;j<n;j++){
				if(s.at(j)=='F'){
					s.at(j)=' ';
					break;
				}
			}
			for(j=0;j<n;j++){
				if(s.at(j)=='O'){
					s.at(j)=' ';
					break;
				}
			}
			for(j=0;j<n;j++){
				if(s.at(j)=='U'){
					s.at(j)=' ';
					break;
				}
			}
			for(j=0;j<n;j++){
				if(s.at(j)=='R'){
					s.at(j)=' ';
					break;
				}
			}
		}
		for(i=1;i<=c6;i++){
			for(j=0;j<n;j++){
				if(s.at(j)=='S'){
					s.at(j)=' ';
					break;
				}
			}
			for(j=0;j<n;j++){
				if(s.at(j)=='I'){
					s.at(j)=' ';
					break;
				}
			}
			for(j=0;j<n;j++){
				if(s.at(j)=='X'){
					s.at(j)=' ';
					break;
				}
			}
		}
		for(i=1;i<=c8;i++){
			for(j=0;j<n;j++){
				if(s.at(j)=='E'){
					s.at(j)=' ';
					break;
				}
			}
			for(j=0;j<n;j++){
				if(s.at(j)=='I'){
					s.at(j)=' ';
					break;
				}
			}
			for(j=0;j<n;j++){
				if(s.at(j)=='G'){
					s.at(j)=' ';
					break;
				}
			}
			for(j=0;j<n;j++){
				if(s.at(j)=='H'){
					s.at(j)=' ';
					break;
				}
			}
			for(j=0;j<n;j++){
				if(s.at(j)=='T'){
					s.at(j)=' ';
					break;
				}
			}
		}
		//printf("c0=%d c2=%d c4=%d c6=%d c8=%d\n",c0,c2,c4,c6,c8);
		for(i=0;i<n;i++){
			if(s.at(i)=='O'){
				for(j=0;j<n;j++){
					if(s.at(j)=='N'){
						c1++;
						s.at(j)=' ';
						s.at(i)=' ';
						break;
					}
				}
			}
		}
		for(i=0;i<n;i++){
			if(s.at(i)=='T'){
				for(j=0;j<n;j++){
					if(s.at(j)=='R'){
						c3++;
						s.at(j)=' ';
						s.at(i)=' ';
						break;
					}
				}
			}
		}
		for(i=0;i<n;i++){
			if(s.at(i)=='F'){
				for(j=0;j<n;j++){
					if(s.at(j)=='I'){
						c5++;
						s.at(j)=' ';
						s.at(i)=' ';
						break;
					}
				}
			}
		}
		for(i=0;i<n;i++){
			if(s.at(i)=='S'){
				for(j=0;j<n;j++){
					if(s.at(j)=='E'){
						c7++;
						s.at(j)=' ';
						s.at(i)=' ';
						break;
					}
				}
			}
		}
		for(i=0;i<n;i++){
			if(s.at(i)=='N'){
				for(j=0;j<n;j++){
					if(s.at(j)=='I'){
						c9++;
						s.at(j)=' ';
						s.at(i)=' ';
						break;
					}
				}
			}
		}
		//cout<<s<<endl;
		//printf("c1=%d c3=%d c5=%d c7=%d c9=%d\n",c1,c3,c5,c7,c9);
		printf("Case #%d: ",testcounter);
		for(i=1;i<=c0;i++){
			printf("0");
		}
		for(i=1;i<=c1;i++){
			printf("1");
		}
		for(i=1;i<=c2;i++){
			printf("2");
		}
		for(i=1;i<=c3;i++){
			printf("3");
		}
		for(i=1;i<=c4;i++){
			printf("4");
		}
		for(i=1;i<=c5;i++){
			printf("5");
		}
		for(i=1;i<=c6;i++){
			printf("6");
		}
		for(i=1;i<=c7;i++){
			printf("7");
		}
		for(i=1;i<=c8;i++){
			printf("8");
		}
		for(i=1;i<=c9;i++){
			printf("9");
		}
		printf("\n");
		c0=0;c1=0;c2=0;c3=0;c4=0;c5=0;c6=0;c7=0;c8=0;c9=0;
		testcounter++;
	}
return 0;
}