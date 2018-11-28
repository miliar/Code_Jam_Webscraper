/*
 * =====================================================================================
 *
 *       Filename:  a.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  Saturday 11 April 2015 11:10:35  IST
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Shounak Dey (), dylandey1996@gmail.com
 *   Organization:  
 *
 * =====================================================================================
 */

#include<bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t=0;t<T;t++)
	{
		int x;
		string a;
		cin >> x >> a;
		int sum[x];
		int ans=0;
		x++;
		sum[0]=a[0]-'0';
		ans = (sum[0]<1);
		for(int i=1;i<x;i++)
			sum[i]=sum[i-1]+(a[i]-'0');
		for(int i=0;i<x;i++)
		{
			if(ans+sum[i-1] < i)
				ans += (i-(ans+sum[i-1]));
		}
		cout << "Case #"<< t+1 << ": " << ans << endl;
	}
	return 0;
}
