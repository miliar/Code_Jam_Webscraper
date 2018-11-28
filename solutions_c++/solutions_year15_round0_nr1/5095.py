#include <cstdio>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <map>
using namespace std;
int main()
{
	freopen("A-large.in", "r" , stdin);
	freopen("l.out", "w", stdout);
	int t,i,j,smax=0,totclap,freq,cases=1;
    string a;
    map<int, int> getvalue;
    getvalue[48]=0;
    getvalue[49]=1;
    getvalue[50]=2;
    getvalue[51]=3;
    getvalue[52]=4;
    getvalue[53]=5;
    getvalue[54]=6;
    getvalue[55]=7;
    getvalue[56]=8;
    getvalue[57]=9;
	scanf("%d",&t);
    while(t--){
        totclap=0;
        freq=0;
        cin>>smax>>a;
        for(i=0;i<=(smax+1);i++) {
            if(getvalue[(int)a[i]]!=0 && totclap>=i){
                totclap=totclap + getvalue[(int)a[i]];
                //cout<<" totclap "<<totclap;
            }
            else if(getvalue[(int)a[i]]!=0 && totclap<i){
                freq=freq+(i-totclap);
                totclap=totclap+(i-totclap)+getvalue[(int)a[i]];
                //cout<<" totclap sec "<<totclap;
            }
        }
        cout<<"Case #"<<cases<<":"<<" "<<freq;
        cout<<endl;
        cases++;
    }
    return 0;
}
