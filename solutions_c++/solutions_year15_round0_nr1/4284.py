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
	ll j,i,cnt,t,n,len,num;
	string s;
	sl(t)
	for(j=1;j<=t;j++)
	{
		sl(n)
		cin>>s;
		cnt=s[0]-48;
		num=0;
		len=s.length();
		for(i=1;i<len;i++)
		{
			if(s[i]-48==0)
				continue;
			if(cnt<i)
			{
				num+=i-cnt;
				cnt=i;
			}
			cnt+=s[i]-48;
		}
		printf("Case #%lld: %lld\n",j,num);
	}
	return 0;
}
