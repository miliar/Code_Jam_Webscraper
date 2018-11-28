#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#define pb push_back
using namespace std;
vector<double> nao;
vector<double> ken;

int main()
{
	//freopen("C:\\Users\\Balasubramanian\\Downloads\\D-large.in", "r", stdin);
    //freopen("C:\\Users\\Balasubramanian\\Desktop\\C++progs\\output4L.out", "w", stdout);
	int n,t2; 
	int count=0;
   cin>>t2;
   while(t2--)
   {
   count++;
   
    cin>>n;
    
	double d;
	
	for(int i=0;i<n;++i)
	{
		cin>>d;
		nao.push_back(d);
	}
	for(int i=0;i<n;++i)
	{
		cin>>d;
		ken.push_back(d);
	}
	
	sort(nao.begin(),nao.end());
	sort(ken.begin(),ken.end());
    vector<double> nao1(nao.begin(),nao.end());
    vector<double> ken1(ken.begin(),ken.end());
	
	int count1=0;
	int count2=0;
	int t1=0;
	while(!t1)
	{
	if(nao.empty()){
	t1=1;break;}
	for(int i=0;i<nao.size();++i)
	{
		if(nao[i]<ken[i])
		{
			nao.erase(nao.begin()+i);
			break;
		}
		if(i==nao.size()-1)
		{t1=1;break;}
	}}
	count1=nao.size();
	for(int i=0;i<nao1.size();++i)
	{
		int t=0;
		for(int j=0;j<ken1.size();++j)
		{
			if(ken1[j]>nao1[i])
			{
				t=1;
				ken1.erase(ken1.begin()+j);
				break;
			}
			
		}
        if(!t)
        {
            count2=nao1.size()-i;
            break;
        }
	}
    cout<<"Case #"<<count<<": "<<count1<<" "<<count2<<endl;
   
    nao.erase(nao.begin(),nao.end());
    ken.erase(ken.begin(),ken.end());
}
    return 0;
}
