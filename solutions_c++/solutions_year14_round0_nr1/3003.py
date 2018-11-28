#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <functional>

using namespace std;

int main()
{
    int i,j,k,l,m,n;
    int T,M,N,K,t1,t2,t3,t4,t5;
    long long ans,out;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A_output.txt","w",stdout);
    int arr1[5][5],arr2[5][5];
    cin>>T;
    for(t1=1;t1<=T;++t1)
    {
    	cout<<"Case #"<<t1<<": ";
    	cin>>m;
    	for(i=1;i<=4;++i)
    		for(j=1;j<=4;++j)
    			cin>>arr1[i][j];

    	cin>>n;
    	for(i=1;i<=4;++i)
    		for(j=1;j<=4;++j)
    			cin>>arr2[i][j];

    	for(k=0,l=0,i=1;i<=4;++i)
    		for(j=1;j<=4;++j)
    		{
    			if (arr1[m][i]==arr2[n][j])
    			{
    				k++;
    				l=arr1[m][i];
    			}
    		}
    	if(k==1)
    		cout<<l<<endl;
    	else if(k==0)
    		cout<<"Volunteer cheated!"<<endl;
    	else
    		cout<<"Bad magician!"<<endl;
    }

    return 0;
}
