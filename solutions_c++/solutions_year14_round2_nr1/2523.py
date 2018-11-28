//
//  main.cpp
//  testB
//
//  Created by 李博 on 14-5-4.
//  Copyright (c) 2014年 Libo. All rights reserved.
//

#pragma warning(disable:4996)
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
char p1[101];
char p2[101];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T,TC,n,num,i,j;
    bool isWin = false;
    
	scanf("%d", &TC);
	for (T = 1; T <= TC; T++){
		num = 0;
        printf("Case #%d: ", T);
		scanf("%d", &n);
        
        scanf("%s", p1);
        scanf("%s", p2);
        isWin =false;
        
        if (p1[0] != p2[0]) {
            printf("Fegla Won\n");
            continue;
        }
        i =0;
        j=0;
        while (p1[i]!='\0' && p2[j]!='\0') {
                if (p1[i]!=p2[j]) {
                    num++;
                    if (p1[i-1]==p1[i])
                        i++;
                    else if(p2[j-1] == p2[j])
                        j++;
                    else{
                        isWin = true;
                        break;
                    }
                }
                else{
                    i++;
                    j++;
                }
        }
        if (p1[i]=='\0') {
            while (p2[j]!='\0') {
                if (p2[j-1] == p2[j]) {
                    num++;
                    j++;
                }
                else{
                    isWin = true;
                    break;
                }
            }
        }
        else{
            while (p1[i]!='\0') {
                if (p1[i-1] == p1[i]) {
                    num++;
                    i++;
                }
                else{
                    isWin = true;
                    break;
                }
            }
        }
        if(isWin)
            printf("Fegla Won\n");
        else
            printf("%d\n",num);
	}
    
}

