#include <bits/stdc++.h>
using namespace std;
int war(vector<double> naomi,vector<double> ken)
{
    sort(naomi.begin(),naomi.end());
    sort(ken.begin(),ken.end());
    int result=0;	
    for(int i=0;i<naomi.size();i++)
	{
		bool done=false;
		for(int j=0;j<ken.size();j++)		
		{
			if(naomi[i]<ken[j])
			{
				ken.erase(ken.begin()+j);
				done=true;
				break;
			}
		}
		if(!done)
		{
			ken.erase(ken.begin());
			result++;
		}
	}
return result;
}
FILE *f1=fopen("sorted.txt","w");
int dwar(vector<double> naomi,vector<double> ken)
{
    vector<double> ken2=ken;
    sort(naomi.begin(),naomi.end());
    sort(ken.begin(),ken.end());
    fprintf(f1,"%d\n",ken.size());
    for(int i=0;i<naomi.size();i++) fprintf(f1,"%.3f ",naomi[i]);
    fprintf(f1,"\n");
    for(int i=0;i<ken.size();i++)  fprintf(f1,"%.3f ",ken[i]);
 fprintf(f1,"\n");
    int result1=0,result2=0,result3=0,result4=0;	
    for(int i=0;i<naomi.size();i++)
	{
		bool done=false;
		double p=ken[ken.size()-1];
		if(p<naomi[i])
			{
				result1++;
				ken.erase(ken.begin());
			}
		else if(p>naomi[i])
			{
				ken.erase(ken.end()-1);
			}
		
	}
    ken=ken2;
    sort(naomi.begin(),naomi.end());
    sort(ken.begin(),ken.end(),greater<double>());
     for(int i=0;i<naomi.size();i++)
	{
		bool done=false;
		double p=ken[ken.size()-1];
		if(p<naomi[i])
			{
				result2++;
				ken.erase(ken.end()-1);
			}
		else if(p>naomi[i])
			{
				ken.erase(ken.begin());
			}
		
	}
     ken=ken2;
    sort(naomi.begin(),naomi.end(),greater<double>());
    sort(ken.begin(),ken.end());
     for(int i=0;i<naomi.size();i++)
	{
		bool done=false;
		double p=ken[ken.size()-1];
		if(p<naomi[i])
			{
				result3++;
				ken.erase(ken.begin());
			}
		else if(p>naomi[i])
			{
				ken.erase(ken.end()-1);
			}
		
	}
     ken=ken2;
    sort(naomi.begin(),naomi.end(),greater<double>());
    sort(ken.begin(),ken.end(),greater<double>());
     for(int i=0;i<naomi.size();i++)
	{
		bool done=false;
		double p=ken[ken.size()-1];
		if(p<naomi[i])
			{
				result4++;
				ken.erase(ken.end()-1);
			}
		else if(p>naomi[i])
			{
				ken.erase(ken.begin());
			}
		
	}
return max(max(result1,result2),max(result3,result4));
}
int main()
{
	int T,N;
	freopen("gcj4input.txt","r",stdin);
	freopen("gcj4outputfinal2.txt","w",stdout);
	cin>>T;
	for(int TC=1;TC<=T;TC++)
	{
		cin>>N;
		vector<double> naomi(N),ken(N);
		for(int i=0;i<N;i++)
			cin>>naomi[i];
		for(int i=0;i<N;i++)
			cin>>ken[i];
		printf("Case #%d: %d %d\n",TC,dwar(naomi,ken),war(naomi,ken));
	}
return 0;
} 