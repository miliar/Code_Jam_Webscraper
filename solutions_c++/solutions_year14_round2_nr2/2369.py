#pragma warning(disable:4996)
#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC, T, i,j, n, m, o;
    int num=0;
	scanf("%d", &TC);
	for (T = 1; T <= TC; T++){
		printf("Case #%d: ", T);
		scanf("%d%d%d", &n, &m, &o);
        num =0;
		for (i = 0; i < n; i++){
			for (j = 0; j < m; j++){
                if ((i&j) < o) {
                    num++;
                }
            }
		}
        cout<<num<<endl;
	}
}