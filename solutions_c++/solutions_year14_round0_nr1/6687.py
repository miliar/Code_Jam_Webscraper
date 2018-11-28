/*--------------------- Author - Akshit ----------------------*/

#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<stack>
#include<list>
#include<queue>
#include<cstdlib>
#include<numeric>
#include<set>
#include<map>
#include<deque>
#include<climits>
#include<cassert>
#include<cctype>
#include<ctime>
#include<iterator>
#include<iomanip>
#include<functional>
#include<fstream>
#include<ostream>
#include<istream>

using namespace std;

#define sf(n)                scanf("%d",&n) 
#define pf(n)                printf("%d",n)          
#define pfln(n)              printf("%d\n",n)         

#define vi                   vector <int > 
#define pb                   push_back()
#define debug(in)             printf("n = %d\n",n)
#define PI 3.14159265358979
#define LL 1000000007

int a[17][17];
int answers[5];
int main()
{
	std::ios_base::sync_with_stdio(false);
	int t,ans1,ans2;
	int no = 1;
	cin>>t;
	while(no<=t){
		cin>>ans1;
		for(int i = 1 ; i <= 4 ; i++){
			for(int j = 1 ; j <= 4 ;j++){
				cin>>a[i][j];
			}
		}
		for(int j = 1 ; j <=4 ; j++){
			answers[j] = a[ans1][j];
		}
		cin>>ans2;
		for(int i = 1 ; i <= 4 ; i++){
			for(int j = 1 ; j <= 4 ;j++){
				cin>>a[i][j];
			}
		}
		// valid answer
		int flag = 0;
		int col;
		for(int j = 1 ; j<=4 ; j++){
			for(int k =1 ; k<=4 ;k++){
				if(a[ans2][j] == answers[k])
				{
					flag++;
					col = j;
				}

			}
		}
		if (flag == 1){
			cout<<"Case #"<<no<<": "<<a[ans2][col]<<"\n";
		}
		if(flag == 0)
			cout<<"Case #"<<no<<": "<<"Volunteer cheated!"<<"\n";
		if (flag > 1)
			cout<<"Case #"<<no<<": "<<"Bad magician!"<<"\n";


		no++;	

	}
	return 0;
}
