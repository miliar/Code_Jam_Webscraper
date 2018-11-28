//
//  main.cpp
//  EleProInter
//
//  Created by lhdgriver on 14-4-3.
//  Copyright (c) 2014年 lhdgriver. All rights reserved.
//

#include<stdio.h>
#include<iostream>
#include<vector>
#include<iomanip>
using namespace std;


int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;
    int n;
    cin >> T;
    
    
	for(int i = 1;i <= T;i ++)
	{
		
        cin >> n;
        vector<double> a, b;
        a.resize(n);
        b.resize(n);
        for(int j = 0; j < n; j++)
            cin >> a[j];
        for(int j = 0; j < n; j++)
            cin >> b[j];
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        int war = 0, dwar = 0;
        int b_index = 0;
        for(int j = 0; j < n; j++) {
            while(b_index < n) {
                if (b[b_index] > a[j]) {
                    b_index++;
                    break;
                }
                b_index++;
            }
            if(b_index == n) {
                war = n - j - 1;
                break;
            }
        }
        
        int a_index = 0;
        for (int j = 0; j < n; j++) {
            while(a_index < n) {
                if (a[a_index] > b[j]) {
                    dwar++;
                    a_index++;
                    break;
                }
                a_index++;
            }
        }
        cout << "Case #" << i << ": " << dwar << " " << war << endl;
	}
	fclose(stdin);
	fclose(stdout);
}