#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;


int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
	
    int t2;
    cin >> t2;
	int r1=0,r2=0;
	int data1[16],data2[16],seldata;
	int num=0;
	int index1=0,index2=0;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);
        cin >> r1;
		for( int i=0;i<16;++i)cin>>data1[i];
		cin >> r2;
		for( int i=0;i<16;++i)cin>>data2[i];
		index1=(r1-1)*4;
		index2=(r2-1)*4;
		num=0;
		for( int i=0;i<4;++i)
		{
			for( int j=0;j<4;++j)
			{
				if(data1[index1+i]==data2[index2+j])
				{
					num++;
					seldata=data1[index1+i];
				}
			}
		}
		if(num==0)cout <<"Volunteer cheated!";
		else if(num==1)cout << seldata;
        else cout << "Bad magician!";
        printf("\n");
    }
    
    return 0;
}
