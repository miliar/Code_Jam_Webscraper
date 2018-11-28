/*
 * test2.cpp
 *
 * Copyright 2016 MiniVont <minivont@minivont-Lenovo-E10-30>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 *
 *
 */


#include <bits/stdc++.h>
int n;
int arr[27];
using namespace std;
string ans = "";
int check(){
	int tot = 0;
	for(int i =0;i<n;i++)tot += arr[i];
	if(tot == 0)return 2;
	for(int i=0 ; i < n ; i++){
		if(arr[i] > tot/2)return 0;
	}
	return 1;
}
bool solve(){
	int chck = check();
	//cout << ans << endl;
	if(chck == 2)return true;
	if(chck == 0)return false;
	ans += " ";
	for(int i= 0 ; i < n ; i ++){
		if(arr[i] == 0)continue;
		arr[i] --;
		ans += (char)('A'+i);
		for(int j = 0; j < n ; j ++){
			if(arr[j] == 0)continue;
			arr[j]--;
			ans += (char)('A'+j);
			if(solve())return true;
			arr[j]++;
			ans.pop_back();
		}
		if(solve())return true;
		ans.pop_back();
		arr[i] ++;
	}
	ans.pop_back();
}
int main()
{
    freopen("A-small-attempt1(2).in","r",stdin);
    freopen("output.out","w",stdout);
	int T;
	cin >> T;
	for(int t = 1 ; t <= T; t++){
		cin >> n;
		for(int i = 0 ; i < n ; i++){
			cin >> arr[i];
		}
		solve();
		cout << "Case #"<<t<<": "<<ans<<endl;
		ans = "";
	}
	return 0;
}

