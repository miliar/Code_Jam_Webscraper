/**************************************************
**  Author:  Aditya Goel                          *
**  NIT, Kurukshetra                              *  
**  INDIA                                         *  
**************************************************/

#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007  //NA
#define N 211111
#define ll long long int
#define dt ll
#define all(c) c.begin(), c.end()
#define dcl(a) memset(a,0,sizeof(a))
#define rep(i,a,b) for(dt i=a;i<=(dt)(b);i++)
#define tr(container, it) for(vector<dt> ::iterator it= container.begin(); it!=container.end(); it++)
#define trp(container, it) for(vector<pair<dt,dt> >::iterator it = container.begin(); it!=container.end(); it++)
#define tra(container, it) for(typeof(container.begin()) it = container.begin(); it!=container.end(); it++)
#define cc1(a)cout<<#a<<": "<<a<<endl;
#define cc2(a,b)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<< endl;
#define cc3(a,b,c)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<endl;
#define cc4(a,b,c,d)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<" , "<<#d<<": "<<d<<endl;
#define pr pair<dt,dt>  //NA
#define mp(a,b) make_pair(a,b)
#define pb push_back  //NA
#define gc getchar  //NA
#define F first
#define S second
#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",&mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define print(tt, a) printf("Case #%lld: %lld\n",tt,a)
        
bool flipPie(string &str)
{
	ll pos = -1;
	rep(i, 0, str.length() - 1)
	{
		if(str.at(i) == '+' && pos == -1)
		{
			while(i < str.length() && str.at(i) == '+')
			{
				i++;
			}
			pos = i - 1;
			break;
		}
		if(str.at(i) == '-')
		{
			pos = i;
		}
//		cout << "str inside rep of fun : " << str.at(i) << "\t";	
	}
//	cout << "\npos : " << pos << "\n";
	if(pos == -1 || ((pos == str.length() - 1) && str.at(pos) == '+'))
	{
		return false;
	}
	queue<char> que;
	rep(i, 0, pos)
	{
		que.push(str.at(i));	
	}
	while(!que.empty())
	{
		if(que.front() == '-')
			str.at(pos) = '+';
		if(que.front() == '+')
			str.at(pos) = '-';
		que.pop();
//		cout << "\nqueue : " << str.at(pos) << '\n';
		pos--;
	}
	return true;
}
int main()
{
	freopen("inLarge2.txt","r",stdin);
    freopen("outLarge2.txt","w",stdout);
	int test, tt;
	sd(test);
	rep(tt, 1, test)
	{
		string str;
		cin >> str;
//		cout << str << '\n';
		ll count = 0;
		while(1)
		{
//			cout << "String : " << str << '\n';
			if(flipPie(str))
				count++;
			else
				break;	
//			cout << "Count " << count << '\n' << "String After : " << str << '\n';
		}
		print(tt, count);	
	}
	return 0;
}

