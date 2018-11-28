#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	// freopen("1.in","r",stdin);
	// freopen("1.out","w",stdout);
	int T;
	int ans1,ans2,ans;
	int num[17] = {false};
	int tmp,flag;
	cin >> T;
	for (int tt = 0; tt<T; tt++){
		memset(num,0,sizeof(num));
		flag = 0;
		cin >> ans1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (i+1==ans1){
					cin >> tmp;
					num[tmp] ++;
				}else
					cin >> tmp;
		cin >> ans2;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (i+1==ans2){
					cin >> tmp;
					num[tmp] ++;
				}else
					cin >> tmp;
		for (int i = 1; i <=16; i++){
			if (num[i] == 2){
				flag ++;
				ans = i;
			}
		}
		//--------------------- print -----------------
		cout << "Case #" << tt+1 << ": ";
		if (flag == 1)
			cout << ans;
		else if (flag > 1)	
			cout << "Bad magician!";
		else if (flag == 0)
			cout << "Volunteer cheated!";
		cout << endl;
	}
	
}