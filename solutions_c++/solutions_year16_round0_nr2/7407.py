#include <iostream>
#include <bits/stdc++.h>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cassert>
using namespace std;

int main()
{
    freopen ("B-large.in", "r", stdin);
	freopen ("myfile.txt","w",stdout);

    long long n,temp;
    long long visited ;
     int t ;
    scanf("%d",&t);
    for(int a=1;a<=t;a++){
        string s ;
        int counter=0;
        cin>>s ;
        printf("Case #%d: ",a);
        if(s.length()==1&&s[0]=='+'){
            printf("%d\n",0);
        }else if (s.length()==1&&s[0]=='-'){
            printf("%d\n",1);
        }else {
            for(int i=1;i<s.length();i++){
                if(s[i]=='+'&&s[i-1]=='-'){
                    counter++;
                    for(int j=0;j<i;j++){
                        s[j]='+';
                    }
                }else if(s[i]=='-'&&s[i-1]=='+'){
                    counter++;
                    for(int j=0;j<i;j++){
                        s[j]='-';
                    }
                    counter++;
                    int k=i;
                    while(s[k]=='-'&&k<s.length()){
                        k++;
                    }
                    for(int j=0;j<k;j++){
                        s[j]='+';
                    }

                }
            }
            bool flag=false;
            for(int j=0;j<s.length();j++){
                if(s[j]=='+'){
                    flag=true;
                }
            }
            if(!flag){
                            printf("%d\n",counter+1);

            }else{
                                printf("%d\n",counter);

            }
        }

    }

    return 0;
}
