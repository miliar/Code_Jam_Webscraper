#include<iostream>
#include<string>
#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
    int t;
    //char s[100];
    scanf("%d\n",&t);

    for (int z = 0; z<t; z++){

    int A, B, K;
    scanf("%d %d %d",&A, &B, &K);
    int cnt = 0;

    for(int i = 0; i< A; i++){
        for(int j = 0; j < B; j++){
            if((i&j) < K)   cnt ++;
        }
    }

        cout<<"Case #"<<z+1<<": "<<cnt<<endl;
    }
    return 0;
}
