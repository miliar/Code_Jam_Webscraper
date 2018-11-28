/* ***************************************************************
 * Program Name :Set.Insert()
 * Date:Feb 19, 2016
 * Author:Mahmoud Ismail
 *Copyright:Your copyright notice
 ************************************************************/
#define _CRT_SECURE_NO_WARNINGS 
#include<bits/stdc++.h>
#include<stdio.h>
#include<sstream>
#include <stdlib.h> 
#include<iostream>
#include<string>
#include<algorithm>
#include <limits>
#include<queue>
#include<vector>
#include<set>
#include <cstdio>
#include <cstring>
#include<map>
#include<cmath>
#include<climits>
#include<iomanip>
#include<utility>
#include<set>
#include<iterator>
using namespace std;
bool arr[10] ={};
bool check()
{

for(int i=0;i<10;i++)
{

if(arr[i]==false)
	return false;


}
return true;




}
void gen(long long n) {

	while (n) {
		arr[n % 10] = true;
		n /= 10;
	}

}
int main() {

	long long t;
	scanf("%lld", &t);
	long long c = 1;

	while (t--) {
		long long n, cnt = 0;
		scanf("%lld", &n);
		memset(arr, false, sizeof(arr));

		if (n == 0) {
			printf("Case #%lld: INSOMNIA\n", c);
		} else {

			while(!check())
			{cnt++;
				long long a=cnt*n;

				gen(a);
			}

			printf("Case #%lld: %lld\n",c,(cnt*n));






		}

	c++;
	}

	return 0;
}
