#include<iostream>
#include<math.h>
#include<vector>
using namespace std;
bool ispal(int nm)
{
	int l=0,d=1;
	while(nm/d)
	{
		l++;
		d*=10;
	}
	d/=10;
vector<int> pal;
pal.clear();
int a=1;
if(l==1){return true;}
for(int u=0;u<l;u++)
{
	int o1=pow(10,a),o2=pow(10,a-1),o3=pow(10,l-a);	
	pal.push_back(nm%o1/o2);
	a++;
}
vector<int>::iterator it;
vector<int>::iterator it2=pal.end()-1;
for( it = pal.begin(); it!=pal.end(); ++it)
{
//	cout<<*it<<" "<<*it2<<endl;
	if(*it!=*it2){//cout<<nm<<"ni en pedo es palindrome"<<endl;
			 return false;}
	
	
	--it2;

}
//	int a=1;
//	while (a<(l+1)/2)
//	{
	//	int o1=pow(10,a),o2=pow(10,a-1),o3=pow(10,l-a);	
	//	if (((nm%o1)/(o2)!=nm%o3)/(o2))
	//	{cout<<nm<<"ni en pedo es palindrome"<<endl; return false;}
//		a++;		
//	}
//cout<<nm<<"fija es palindrome"<<endl;
	return true;
}
int main ()

{
	int T;
	cin>>T;
	int A,B;
	for (int f=0;f<T;f++)
	{
		cin>>A>>B;
		char ans='N';int c=0;
		for (int m=A;m<=B;m++)
		{
bool cond=sqrt(m)==((( int )sqrt(m))/1); if(cond){//cout<<sqrt(m)<<"igual a"<<sqrt(m)/1<<endl;
 if (ispal(m)){if(ispal(sqrt(m))){ans='Y';c++;}} //cout<<numcaso<<ans;
		}}
		cout<<"Case #"<<f+1<<": "<<c<<endl;
	}


	return 0;
}
