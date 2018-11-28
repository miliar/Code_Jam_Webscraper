/*input
100
0
1
2
11
200
54
19
65
164
32
151
84
197
88
145
173
7
181
76
166
55
148
106
122
97
25
82
34
116
66
132
28
186
123
40
193
3
139
14
24
4
46
129
157
124
73
5
195
31
43
9
86
154
17
149
159
68
150
108
96
187
171
6
93
35
60
162
161
45
125
49
72
13
136
89
18
175
48
191
30
112
131
44
111
183
20
41
10
192
152
198
172
182
117
160
194
184
53
8
81

*/
#include <bits/stdc++.h>
#include<stdio.h>
#include<math.h>
using namespace std;
#define pii pair<long long,long long>
#define PI 3.14159265
#define ll long long
#define ff first
#define ss second
#define pb push_back
#define INF 1000000009
#define mod 1000000007

int main() 
{
    std::ios::sync_with_stdio(false);
    ll t,n,d,a[10],b,co=0,ans;
	cin>>t;
	for(ll j=1;j<=t;j++)
	{
		for(int i=0;i<10;i++) 
			a[i]=0;
		co=0;
		cin>>n;
		for(ll i=1;co!=10;i++)
		{	
			d=i*n;
			ans=d; 
			while(d!=0&&n!=0)
			{
				b=d%10;
				if(a[b]==0) 
				{
					a[b]++; 
					co++;
				}
				d=d/10;
			}
			if(co==10||n==0) 
			{ 
				co=10;
				cout<<"Case #"<<j<<": ";
				if(n!=0) 	
					cout<<ans<<"\n";
				else 
					cout<<"INSOMNIA"<<"\n";
	  		}
		}
	}
    return 0;
}