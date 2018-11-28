#include<stdio.h>
#include<iostream>
#include<algorithm>
#include <string.h>
#include <math.h>


using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	int x = 0;
	while (t--) {
		string str;
		int n,ans =0,count =0,i,j;
		cin>>n;
		cin>>str;
	     count  =0;
		for(i = 0; i <=n;i++) {
			if(i > count && str[i] != '0') {
				ans  = ans + i - count;
				count = count + i - count;
				count = count + str[i] - 48;
			}
			else {
				count = count + str[i] - 48; 
			}
			
			
		
		}
		x++;
		cout<<"Case #"<<x<<":"<<" "<<ans<<endl;
		
	}


return 0;
}

