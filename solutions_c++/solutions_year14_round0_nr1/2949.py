#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t,i,j,k;
	int r1,r2;
	int a[5][5],b[5][5];
	//ofstream myfile("output.txt");
	//ifstream myfile ("input.txt");
       
	vector<int> v1,v2,v;
	k=0;
	scanf("%d",&t);
	while(t--)
	{
		k++;
		scanf("%d",&r1);r1--;
		v.clear();
		v1.clear();v2.clear();
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
			scanf("%d",&a[i][j]);
			if(i==r1){v1.push_back(a[i][j]);}
			}
		}
		cin>>r2;r2--;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
			scanf("%d",&b[i][j]);
			if(i==r2){v2.push_back(b[i][j]);}
			}
		}
		for(i=0;i<v1.size();i++)
		{
			for(j=0;j<v2.size();j++)
			{
				if(v1[i]==v2[j])
				{
					v.push_back(v1[i]);
				}
			}
		}
		if(v.size()==1){printf("Case #%d: %d\n",k,v[0]);}
		if(v.size()>1){printf("Case #%d: Bad magician!\n",k);}
		if(v.size()==0){printf("Case #%d: Volunteer cheated!\n",k);}
	}
	
	return 0;
}
		
		
