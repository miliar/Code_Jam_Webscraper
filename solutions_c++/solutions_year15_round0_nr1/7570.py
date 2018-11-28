#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    freopen("f.in","r",stdin);
    freopen("f.out","w",stdout);

    string s;
    int t,n,k,curr_up,s_max,friends;

    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%d",&s_max);
        cin >> s;

        curr_up = friends = 0;
        for(int j=0;j<s.size();j++){
            k = (char)s[j]-(char)'0';
            if(j <= curr_up) curr_up+=k;
            else if(j > curr_up && k>0){
                friends+=j-curr_up;
                curr_up+=j-curr_up+k;
            }
        }

        printf("Case #%d: %d\n",i,friends);
    }
    return 0;
}
