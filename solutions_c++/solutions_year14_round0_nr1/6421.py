#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <numeric> 
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
using namespace std;
int main(){
	int t,a,b,arr1[4][4],arr2[4][4],ans,count=0,k;
	freopen("A-small-attempt1.in", "rt", stdin);
  	freopen("outputA-small-attempt1.txt", "wt", stdout);
	cin>>t;
	for(k=0;k<t;k++){
		count=0,ans=0;
		cin>>a;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		cin>>arr1[i][j];
		
		cin>>b;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		cin>>arr2[i][j];
		
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		if(arr1[a-1][i]==arr2[b-1][j])
		{count++;ans=arr1[a-1][i];}
	
	if(count==1)
	cout<<"Case #"<<(k+1)<<": "<<ans<<endl;
	else if (count==0)
	cout<<"Case #"<<(k+1)<<": Volunteer cheated!"<<endl;
	else if(count>1)
	cout<<"Case #"<<(k+1)<<": Bad magician!"<<endl;	
	}
	return 0;
}
	
