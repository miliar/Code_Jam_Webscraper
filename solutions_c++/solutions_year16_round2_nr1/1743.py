/*input
4
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER
*/
#include <bits/stdc++.h>
#include<stdio.h>
#include<math.h>
using namespace std;
#define pii pair<long long,long long>
#define PI 3.14159265
#define ll long long
#define ff first
#define ss second
#define pb push_back
#define INF 1000000009
#define mod 1000000007
char s[2010];
int main()
 {
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;++k) {
		int x, i, j=0, temp=0;
		int check[30]={0};
		int number[10]={0};
		cin>>s;
		for(i=0;i<strlen(s);i++) {
			x = (int)s[i] - 64;
			check[x]++;
		}
		// ZERO CHECK
		if(check[26] > 0) {
			temp = check[26];
			check[26] = 0;
			number[0] = temp;
			check[5] -= temp;
			check[18] -= temp;
			check[15] -= temp;
		}
		// TWO CHECK
		if(check[23] > 0) {
			temp = check[23];
			check[23] = 0;
			number[2] = temp;
			check[20] -= temp;
			check[15] -= temp;
		}
		// FOUR CHECK
		if(check[21] > 0) {
			temp = check[21];
			check[21] = 0;
			number[4] = temp;
			check[15] -= temp;
			check[18] -= temp;
			check[6] -= temp;
		}
		// CHECK SIX
		if(check[24] > 0) {
			temp = check[24];
			check[24] = 0;
			number[6] = temp;
			check[19] -= temp;
			check[9] -= temp;
		}
		// CHECK EIGHT
		if(check[7] > 0) {
			temp = check[7];
			check[7] = 0;
			number[8] = temp;
			check[5] -= temp;
			check[9] -= temp;
			check[8] -= temp;
			check[20] -= temp;
		}
		// CHECK THREE
		if(check[8] > 0) {
			temp = check[8];
			check[8] = 0;
			number[3] = temp;
			check[20] -= temp;
			check[18] -= temp;
			check[5] -= temp*2;
		}
		// CHECK FIVE
		if(check[6] > 0) {
			temp = check[6];
			check[6] = 0;
			number[5] = temp;
			check[9] -= temp;
			check[22] -= temp;
			check[5] -= temp;
		}
		// CHECK ONE
		if(check[15] > 0) {
			temp = check[15];
			check[15] = 0;
			number[1] = temp;
			check[14] -= temp;
			check[5] -= temp;
		}
		// CHECK SEVEN
		if(check[22] > 0) {
			temp = check[22];
			check[22] = 0;
			number[7] = temp;
			check[19] -= temp;
			check[5] -= temp*2;
			check[14] -= temp;
		}
		// CHECK NINE
		if(check[9] > 0) {
			temp = check[9];
			check[9] = 0;
			number[9] = temp;
			check[5] -= temp;
			check[14] -= temp*2;
		}
		cout<<"Case #"<<k<<": ";
		for(i=0;i<10;i++) 
		{
			if(number[i] !=0) 
			{
				for(j=0;j<number[i];j++)
			 	{
					cout<<i;
				}
			}
		}
		cout<<endl;
	}
	return 0;
}
