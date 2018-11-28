#include<bits/stdc++.h>
#define intMAX 1123456789LL
#define MAX intMAX * intMAX
#define F first
#define S second
#define mp make_pair
#define ll long long
#define pb push_back
#define pv(v,b,a) v.insert(v.begin()+b,a)
#define all(c) c.begin(),c.end()
#define sf(a) scanf("%d",&a);
#define sl(a) scanf("%lld",&a);
#define MAXCR 1000000000
#define mem(arr,a) memset(arr, a, sizeof arr)
#define er(vec,a,b) vec.erase(vec.begin() + a, vec.begin() + b+1)
#define traverse(a) for()
#define pii pair<int ,int>
#define mod 1000000007
#define LIM 100
using namespace std;
/*
list as pop_front();push_front(ELEMENT);
list as pop_front();push_back(ELEMENT);
to see first element stack=q.front()
to see last element queue=q.back()
*/
//str.insert(6,str3,3,4); to insert 4 words from str3 starting from 3rd position(0 based indexing) to str from 6th position (0 based indexing)
//str.find("live");//finds first occurance of string and returns its 0 based indes
//string str1=str.substr (a,n);//a=0 based start index,n=length of words//if length not given substring till end is formed
//auto bound_=upper_bound (v.begin(), v.end(), 20); //Returns an iterator pointing to the first element in the range [first,last) which compares greater than val.
//auto bound_=lower_bound (v.begin(), v.end(), 20);//Returns an iterator pointing to the first element in the range [first,last) which does not compare less than val.
//for(???<???>:iterator itr;itr!=???.end();itr++) or for(auto &tt : t.edges)
//getline(cin,s,'\n');  to get input terminating at'\n';excluding '\n'
//(a/b)%m = ((a%m)(b^(m-2)%m))%m.
//(a^b)%m=
int main()
{
	freopen ("input.txt","r",stdin);
	freopen("output.txt","w",stdout);	
	int t,j,r,c,x;
	sf(t)
	for(j=1;j<=t;j++)
	{
		sf(x)
		sf(r)
		sf(c)
		if(x==1)
		{
			printf("Case #%d: GABRIEL\n",j);
		}
		else if(x>=7)
		{
			printf("Case #%d: RICHARD\n",j);
		}
		else if(r*c-x<0)
		{
			printf("Case #%d: RICHARD\n",j);
		}
		else if((r*c-x)%x!=0)
		{
			printf("Case #%d: RICHARD\n",j);
		}
		else if(x-min(r,c)-1>=min(r,c))
		{
			printf("Case #%d: RICHARD\n",j);
		}
		else if(x>max(r,c))
		{
			printf("Case #%d: RICHARD\n",j);
		}
		else if(x-min(r,c)-2>=0)
		{
			printf("Case #%d: RICHARD\n",j);
		}
		else
		{
			printf("Case #%d: GABRIEL\n",j);
		}
	}
	return 0;
}
/*
64
1 1 1
1 1 2 
1 1 3 
1 1 4
1 2 1
1 2 2
1 2 3
1 2 4
1 3 1
1 3 2
1 3 3
1 3 4
1 4 1
1 4 2
1 4 3
1 4 4
2 1 1
2 1 2 
2 1 3 
2 1 4
2 2 1
2 2 2
2 2 3
2 2 4
2 3 1
2 3 2
2 3 3
2 3 4
2 4 1
2 4 2
2 4 3
2 4 4
3 1 1
3 1 2 
3 1 3 
3 1 4
3 2 1
3 2 2
3 2 3
3 2 4
3 3 1
3 3 2
3 3 3
3 3 4
3 4 1
3 4 2
3 4 3
3 4 4
4 1 1
4 1 2 
4 1 3 
4 1 4
4 2 1
4 2 2
4 2 3
4 2 4
4 3 1
4 3 2
4 3 3
4 3 4
4 4 1
4 4 2
4 4 3
4 4 4
*/
